import json
import shutil
import unittest
import subprocess
import sys
import tempfile
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]

class TestSkillPackValidation(unittest.TestCase):
    def run_validator(self, root):
        return subprocess.run(
            [sys.executable, str(root / 'scripts' / 'validate_pack.py')],
            capture_output=True,
            text=True
        )

    def run_mutated_pack(self, mutate):
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir) / 'pack'
            shutil.copytree(ROOT, root)
            mutate(root)
            return self.run_validator(root)

    def test_validate_pack_script(self):
        result = self.run_validator(ROOT)
        self.assertEqual(
            result.returncode, 0,
            f"validate_pack.py failed with exit {result.returncode}:\n{result.stdout}\n{result.stderr}"
        )
        self.assertIn('"status": "PASS"', result.stdout)
        self.assertIn('"atomic_skills_validated": 9', result.stdout)

    def test_rejects_manifest_graph_membership_drift(self):
        def add_manifest_only_skill(root):
            path = root / 'manifest.json'
            manifest = json.loads(path.read_text(encoding='utf-8'))
            manifest['skills'].append({
                'name': 'manifest-only',
                'path': 'skills/manifest-only/SKILL.md',
                'role': 'Unmapped Skill',
            })
            path.write_text(json.dumps(manifest), encoding='utf-8')

        result = self.run_mutated_pack(add_manifest_only_skill)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("manifest skill 'manifest-only' missing from graph.yaml nodes", result.stdout)

    def test_rejects_unknown_targets_in_every_edge_field(self):
        edge_values = {
            'precursors': ['missing-node'],
            'continuations': ['missing-node'],
            'lateral_peers': ['missing-node'],
            'on_pass': ['missing-node'],
            'on_fail': ['missing-node'],
            'recovery': 'missing-node',
        }
        for field, value in edge_values.items():
            with self.subTest(field=field):
                def set_unknown_target(root, field=field, value=value):
                    path = root / 'neural-links' / 'graph.yaml'
                    graph = yaml.safe_load(path.read_text(encoding='utf-8'))
                    graph['nodes']['source-intake'][field] = value
                    path.write_text(yaml.safe_dump(graph, sort_keys=False), encoding='utf-8')

                result = self.run_mutated_pack(set_unknown_target)
                self.assertNotEqual(result.returncode, 0)
                self.assertIn('references unknown target', result.stdout)

    def test_rejects_unknown_top_level_recovery_target(self):
        def set_unknown_recovery(root):
            path = root / 'neural-links' / 'graph.yaml'
            graph = yaml.safe_load(path.read_text(encoding='utf-8'))
            graph['recovery']['stale_source'] = 'missing-node'
            path.write_text(yaml.safe_dump(graph, sort_keys=False), encoding='utf-8')

        result = self.run_mutated_pack(set_unknown_recovery)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("graph recovery 'stale_source' references unknown target 'missing-node'", result.stdout)

    def test_static_evals_script(self):
        result = subprocess.run(
            [sys.executable, str(ROOT / 'scripts' / 'run_static_evals.py')],
            capture_output=True,
            text=True
        )
        self.assertEqual(
            result.returncode, 0,
            f"run_static_evals.py failed with exit {result.returncode}:\n{result.stdout}\n{result.stderr}"
        )
        self.assertIn('"status": "PASS"', result.stdout)

if __name__ == '__main__':
    unittest.main()

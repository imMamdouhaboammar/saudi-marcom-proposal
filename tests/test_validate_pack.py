import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
import yaml

ROOT = Path(__file__).resolve().parents[1]

class TestSkillPackValidation(unittest.TestCase):
    def run_validator(self, root):
        return subprocess.run([sys.executable,str(root/'scripts'/'validate_pack.py')],capture_output=True,text=True)

    def run_mutated_pack(self, mutate):
        with tempfile.TemporaryDirectory() as temp:
            root=Path(temp)/'pack'
            shutil.copytree(ROOT,root)
            mutate(root)
            return self.run_validator(root)

    def test_validate_pack_script(self):
        result=self.run_validator(ROOT)
        self.assertEqual(result.returncode,0,f"{result.stdout}\n{result.stderr}")
        self.assertIn('"status": "PASS"',result.stdout)
        self.assertIn('"atomic_skills_validated": 10',result.stdout)

    def test_bid_strategist_registered(self):
        manifest=json.loads((ROOT/'manifest.json').read_text(encoding='utf-8'))
        names={s['name'] for s in manifest['skills']}
        self.assertIn('bid-strategist',names)
        graph=yaml.safe_load((ROOT/'neural-links'/'graph.yaml').read_text(encoding='utf-8'))
        self.assertIn('bid-strategist',graph['nodes'])

    def test_state_router_exists_and_precedes_finalization(self):
        state=yaml.safe_load((ROOT/'routers'/'state-router.yaml').read_text(encoding='utf-8'))
        self.assertIn('missing_strategy_for_scored_bid',state['states'])
        self.assertEqual(state['states']['quality_blocker']['route'],'proposal-qc')

    def test_rejects_manifest_graph_membership_drift(self):
        def mutate(root):
            p=root/'manifest.json'
            m=json.loads(p.read_text(encoding='utf-8'))
            m['skills'].append({'name':'manifest-only','path':'skills/manifest-only/SKILL.md','role':'Unmapped'})
            p.write_text(json.dumps(m),encoding='utf-8')
        result=self.run_mutated_pack(mutate)
        self.assertNotEqual(result.returncode,0)
        self.assertIn("manifest skill 'manifest-only' missing from graph.yaml nodes",result.stdout)

    def test_rejects_unknown_graph_target(self):
        def mutate(root):
            p=root/'neural-links'/'graph.yaml'
            g=yaml.safe_load(p.read_text(encoding='utf-8'))
            g['nodes']['source-intake']['continuations']=['missing-node']
            p.write_text(yaml.safe_dump(g,sort_keys=False),encoding='utf-8')
        result=self.run_mutated_pack(mutate)
        self.assertNotEqual(result.returncode,0)
        self.assertIn('references unknown target',result.stdout)

    def test_static_evals_script(self):
        result=subprocess.run([sys.executable,str(ROOT/'scripts'/'run_static_evals.py')],capture_output=True,text=True)
        self.assertEqual(result.returncode,0,f"{result.stdout}\n{result.stderr}")
        self.assertIn('"status": "PASS"',result.stdout)

if __name__ == '__main__':
    unittest.main()

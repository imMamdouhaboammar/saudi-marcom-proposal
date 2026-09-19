import json
from pathlib import Path
import subprocess
import sys
import unittest

import yaml

ROOT = Path(__file__).resolve().parents[1]


class PackValidationTests(unittest.TestCase):
    def run_json_script(self, relative_path):
        proc = subprocess.run(
            [sys.executable, str(ROOT / relative_path)],
            cwd=ROOT,
            text=True,
            capture_output=True,
        )
        self.assertEqual(proc.returncode, 0, msg=proc.stdout + "\n" + proc.stderr)
        return json.loads(proc.stdout)

    def test_pack_validator_passes(self):
        result = self.run_json_script("scripts/validate_pack.py")
        self.assertEqual(result["status"], "PASS")
        self.assertGreaterEqual(result["atomic_skills"], 10)
        self.assertGreaterEqual(result["scenarios"], 16)

    def test_static_eval_validator_passes(self):
        result = self.run_json_script("scripts/run_static_evals.py")
        self.assertEqual(result["status"], "PASS")
        self.assertGreaterEqual(result["semantic_families"], 12)

    def test_manifest_graph_and_state_contract_align(self):
        manifest = json.loads((ROOT / "manifest.json").read_text(encoding="utf-8"))
        graph = yaml.safe_load((ROOT / "neural-links/graph.yaml").read_text(encoding="utf-8"))
        self.assertEqual(manifest["state_contract"], graph["state_contract"])
        manifest_names = {item["name"] for item in manifest["skills"]}
        self.assertEqual(manifest_names, set(graph["nodes"]))
        self.assertIn("bid-strategist", manifest_names)

    def test_every_graph_node_has_guard(self):
        graph = yaml.safe_load((ROOT / "neural-links/graph.yaml").read_text(encoding="utf-8"))
        for node_id, node in graph["nodes"].items():
            self.assertTrue(node.get("exit_guard"), node_id)

    def test_source_precedence_keeps_prior_proposals_low(self):
        router = yaml.safe_load((ROOT / "routers/source-precedence.yaml").read_text(encoding="utf-8"))
        order = router["precedence"]
        self.assertGreater(
            order.index("private_prior_proposal_pattern"),
            order.index("verified_bidder_owned_fact"),
        )

    def test_eval_contains_transition_and_capacity_cases(self):
        data = json.loads((ROOT / "evals/scenarios.json").read_text(encoding="utf-8"))
        families = {s["family"] for s in data["scenarios"]}
        self.assertIn("procurement-law-transition", families)
        self.assertIn("capacity-stress", families)
        self.assertIn("proof-laundering", families)


if __name__ == "__main__":
    unittest.main()

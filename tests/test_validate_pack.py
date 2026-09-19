import unittest
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

class TestSkillPackValidation(unittest.TestCase):
    def test_validate_pack_script(self):
        result = subprocess.run(
            [sys.executable, str(ROOT / 'scripts' / 'validate_pack.py')],
            capture_output=True,
            text=True
        )
        self.assertEqual(
            result.returncode, 0,
            f"validate_pack.py failed with exit {result.returncode}:\n{result.stdout}\n{result.stderr}"
        )
        self.assertIn('"status": "PASS"', result.stdout)
        self.assertIn('"atomic_skills_validated": 9', result.stdout)

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

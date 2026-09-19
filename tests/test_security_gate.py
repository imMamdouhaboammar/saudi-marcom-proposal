import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

class TestSecurityGate(unittest.TestCase):
    def test_security_gate_passes(self):
        result = subprocess.run(
            [sys.executable, str(ROOT / "scripts" / "security_gate.py")],
            capture_output=True,
            text=True,
        )
        self.assertEqual(result.returncode, 0, f"{result.stdout}\n{result.stderr}")
        self.assertIn('"status": "PASS"', result.stdout)

if __name__ == "__main__":
    unittest.main()

import json
from pathlib import Path
import subprocess
import sys
import tempfile
import textwrap
import unittest

ROOT = Path(__file__).resolve().parents[1]
SCANNER = ROOT / "scripts" / "security_scan.py"


class SecurityScanTests(unittest.TestCase):
    def run_scan(self, root):
        proc = subprocess.run(
            [sys.executable, str(SCANNER), "--root", str(root)],
            text=True,
            capture_output=True,
        )
        return proc, json.loads(proc.stdout)

    def write_workflow(self, root, body):
        path = root / ".github" / "workflows" / "test.yml"
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(textwrap.dedent(body), encoding="utf-8")

    def test_current_repository_passes(self):
        proc, result = self.run_scan(ROOT)
        self.assertEqual(proc.returncode, 0, proc.stdout + proc.stderr)
        self.assertEqual(result["status"], "PASS")

    def test_scans_dotfile_without_suffix(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            token = "ghp_" + ("A" * 32)
            (root / ".env").write_text("TOKEN=" + token, encoding="utf-8")
            proc, result = self.run_scan(root)
            self.assertNotEqual(proc.returncode, 0)
            self.assertTrue(any(".env" in item for item in result["errors"]))

    def test_scans_extensionless_private_key_file(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            key = "-----" + "BEGIN " + "RSA " + "PRIVATE " + "KEY" + "-----\nnot-a-real-key\n"
            (root / "id_rsa").write_text(key, encoding="utf-8")
            proc, result = self.run_scan(root)
            self.assertNotEqual(proc.returncode, 0)
            self.assertTrue(any("id_rsa" in item for item in result["errors"]))

    def test_rejects_job_level_write_permission(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            self.write_workflow(
                root,
                """
                name: bad
                on: push
                permissions:
                  contents: read
                jobs:
                  build:
                    permissions:
                      contents: write
                    runs-on: ubuntu-latest
                    steps: []
                """,
            )
            proc, result = self.run_scan(root)
            self.assertNotEqual(proc.returncode, 0)
            self.assertTrue(
                any("job:build" in item and "contents:write" in item for item in result["errors"])
            )

    def test_allows_read_only_job_permission(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            self.write_workflow(
                root,
                """
                name: safe
                on: push
                permissions:
                  contents: read
                jobs:
                  build:
                    permissions:
                      contents: read
                    runs-on: ubuntu-latest
                    steps: []
                """,
            )
            proc, result = self.run_scan(root)
            self.assertEqual(proc.returncode, 0, proc.stdout + proc.stderr)
            self.assertEqual(result["status"], "PASS")


if __name__ == "__main__":
    unittest.main()

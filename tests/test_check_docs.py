"""Deterministic fixtures for the documentation checker."""
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "tools"))
from check_docs import check  # noqa: E402


class DocChecks(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)

    def put(self, path, content):
        dest = self.root / path
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(content, encoding="utf-8")

    def test_valid_and_external_links(self):
        self.put("README.md", "[Doc](docs/ok.md) [Outside](https://example.org/abc)\n")
        self.put("docs/ok.md", "# Example\n")
        self.assertEqual(check(self.root), [])

    def test_missing_target_detected(self):
        self.put("README.md", "[Missing](docs/not-there.md)\n")
        self.assertTrue(any("missing local link" in problem for problem in check(self.root)))

    def test_fenced_sample_is_ignored(self):
        self.put("README.md", "```md\n[Example](missing.md)\n```\n")
        self.assertEqual(check(self.root), [])

    def test_frontmatter_required(self):
        self.put("skills/sample/SKILL.md", "# No frontmatter\n")
        self.assertTrue(any("frontmatter" in problem for problem in check(self.root)))
        self.put("skills/sample/SKILL.md", "---\nname: sample\ndescription: Does useful things\n---\n# Sample\n")
        self.assertEqual(check(self.root), [])

    def test_escape_rejected(self):
        self.put("README.md", "[Outside](../outside.md)\n")
        self.assertTrue(any("escapes repository" in problem for problem in check(self.root)))


if __name__ == "__main__":
    unittest.main()

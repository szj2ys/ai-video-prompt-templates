import copy
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from promptkit import load_shots, render, validate_shot

ROOT = Path(__file__).resolve().parents[1]


class PromptKitTests(unittest.TestCase):
    def setUp(self):
        self.shots = load_shots(ROOT / 'examples.json')

    def test_examples_have_actionable_review_notes(self):
        self.assertEqual(len(self.shots), 10)
        for shot in self.shots:
            self.assertIn(shot['action'], render(shot))
            self.assertTrue(shot['review'])

    def test_image_reference_without_preservation_is_rejected(self):
        shot = copy.deepcopy(self.shots[0])
        shot['preserve'] = []
        with self.assertRaisesRegex(ValueError, 'preservation note'):
            validate_shot(shot)

    def test_duplicate_ids_and_nonfinite_duration_are_rejected(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / 'shots.json'
            path.write_text(json.dumps([self.shots[0], self.shots[0]]), encoding='utf-8')
            with self.assertRaisesRegex(ValueError, 'Duplicate'):
                load_shots(path)
        shot = copy.deepcopy(self.shots[0])
        shot['duration_seconds'] = float('inf')
        with self.assertRaisesRegex(ValueError, 'finite'):
            validate_shot(shot)

    def test_cli_renders_without_network_or_provider_credentials(self):
        result = subprocess.run([sys.executable, str(ROOT / 'promptkit.py'), str(ROOT / 'examples.json'), '--id', 'ceramic-cup-steam'], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn('The camera remains fixed.', result.stdout)
        self.assertIn('Review after generation:', result.stdout)

    def test_unknown_id_and_bad_json_fail_cleanly(self):
        missing = subprocess.run([sys.executable, str(ROOT / 'promptkit.py'), str(ROOT / 'examples.json'), '--id', 'missing'], capture_output=True, text=True)
        self.assertEqual(missing.returncode, 2)
        self.assertNotIn('Traceback', missing.stderr)
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / 'broken.json'
            path.write_text('{', encoding='utf-8')
            bad = subprocess.run([sys.executable, str(ROOT / 'promptkit.py'), str(path), '--validate'], capture_output=True, text=True)
            self.assertEqual(bad.returncode, 2)
            self.assertNotIn('Traceback', bad.stderr)


if __name__ == '__main__':
    unittest.main()

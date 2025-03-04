import unittest
import sys
import os

# Add the src directory to the system path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from main import get_recommendations

class TestMain(unittest.TestCase):

    def test_get_recommendations_valid_input(self):
        result = get_recommendations("movie")
        self.assertIn("Inception", result)
        self.assertIn("The Matrix", result)

    def test_get_recommendations_invalid_input(self):
        result = get_recommendations("unknown")
        self.assertEqual(result, [])

    def test_get_recommendations_partial_input(self):
        result = get_recommendations("pod")
        self.assertIn("Podcast", result)
        self.assertIn("The Daily", result)

if __name__ == '__main__':
    unittest.main()
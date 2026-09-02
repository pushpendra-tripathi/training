"""
module for test cases
"""

import sys

sys.path.insert(0, "/home/sourabh/work/training/intern_training/week01/day02/utils")

import unittest

from utils.collection import dedupe, frequencies, groupby
from utils.text import clean_text, count_chars, tokenize


class TestTextUtils(unittest.TestCase):
    """
    class to test the module text.py
    """

    def test_clean_text(self):
        self.assertEqual(clean_text("  HELLO  "), "hello")

    def test_count_chars(self):
        self.assertEqual(
            count_chars("hello world"),
            {"h": 1, "e": 1, "l": 3, "o": 2, "w": 1, "r": 1, "d": 1},
        )

    def test_tokenize(self):
        self.assertEqual(tokenize("hello world"), ["hello", "world"])


class TestCollections(unittest.TestCase):
    """
    class to test the module collection.py
    """

    def test_frequencies(self):
        self.assertEqual(frequencies(["a", "b", "a"]), {"a": 2, "b": 1})

    def test_dedupe(self):
        self.assertEqual(dedupe(["a", "b", "b"]).sort(), ["a", "b"].sort())

    def test_group_by(self):
        self.assertEqual(
            groupby(
                [{"status": "todo", "id": 1}, {"status": "done", "id": 2}], key="status"
            ),
            {
                "todo": [{"status": "todo", "id": 1}],
                "done": [{"status": "done", "id": 2}],
            },
        )


if __name__ == "__main__":
    unittest.main()

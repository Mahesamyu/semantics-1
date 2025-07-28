# tests/test_quicksort.py

import unittest

class TestQuickSort(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(quicksort([3, 1, 2]), [1, 2, 3])

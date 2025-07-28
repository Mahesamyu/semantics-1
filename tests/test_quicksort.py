import unittest
from assignmen.quicksort import quicksort  # ← Adjust this path based on your folder structure

class TestQuickSort(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(quicksort([3, 1, 2]), [1, 2, 3])


import unittest
import sys
sys.path.insert(0, './assignmen')  # Change to 'assignment' if renamed
from quicksort import quicksort

class TestQuickSort(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(quicksort([3, 1, 2]), [1, 2, 3])


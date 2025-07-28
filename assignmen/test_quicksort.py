import unittest
from assignment.quicksort import quicksort

class TestQuickSort(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(quicksort([3, 1, 2]), [1, 2, 3])

if __name__ == '__main__':
    unittest.main()

import unittest
from lab1 import *

 # A few test cases.  Add more!!!
class TestLab1(unittest.TestCase):

    def test_max_list_iter(self):
        """add description here"""
        tlist = None
        with self.assertRaises(ValueError):  # used to check for exception
            max_list_iter(tlist)
        self.assertEqual(max_list_iter([5, 4, 3, 2, 0, -10]), 5) # testing max = beginning
        self.assertEqual(max_list_iter([-15, -14, -13, -12, -11, -10]), -10) # testing max = end
        self.assertEqual(max_list_iter([6]), 6) # testing 1 value in list
        self.assertEqual(max_list_iter([]), None) # testing list = []
        self.assertEqual(max_list_iter([5, 4, 3, 20, 20, 20]), 20) # testing for multiple max values

    def test_reverse_rec(self):
        self.assertEqual(reverse_rec([1, 2, 3]), [3, 2, 1]) # testing reversal functionality
        self.assertEqual(reverse_rec([-2, -1, 0, 1, 2]), [2, 1, 0, -1, -2]) # testing larger list
        self.assertEqual(reverse_rec([3, 2, 1]), [1, 2, 3]) # testing different list
        self.assertEqual(reverse_rec([3]), [3]) # testing one value in list

    def test_bin_search(self):
        list_val =[0, 1, 2, 3, 4, 7, 8, 9, 10]
        self.assertEqual(bin_search(0, 0, len(list_val)-1, list_val), 0) # testing for values throughout the list...

        list_val = [0, 1, 2, 3, 4, 7, 8, 9, 10]
        self.assertEqual(bin_search(1, 0, len(list_val) - 1, list_val), 1)  # testing for values...

        list_val = [0, 1, 2, 3, 4, 7, 8, 9, 10]
        self.assertEqual(bin_search(2, 0, len(list_val) - 1, list_val), 2)  # testing for values...

        list_val = [0, 1, 2, 3, 4, 7, 8, 9, 10]
        self.assertEqual(bin_search(3, 0, len(list_val) - 1, list_val), 3)  # testing for values...

        list_val = [0, 1, 2, 3, 4, 7, 8, 9, 10]
        self.assertEqual(bin_search(4, 0, len(list_val) - 1, list_val), 4)  # testing for values...

        list_val = [0, 1, 2, 3, 4, 7, 8, 9, 10]
        self.assertEqual(bin_search(7, 0, len(list_val) - 1, list_val),  5)  # testing for values...

        list_val = [0, 1, 2, 3, 4, 7, 8, 9, 10]
        self.assertEqual(bin_search(8, 0, len(list_val) - 1, list_val), 6)  # testing for values...

        list_val = [0, 1, 2, 3, 4, 7, 8, 9, 10]
        self.assertEqual(bin_search(9, 0, len(list_val) - 1, list_val), 7)  # testing for values...

        list_val = [0, 1, 2, 3, 4, 7, 8, 9, 10]
        self.assertEqual(bin_search(10, 0, len(list_val) - 1, list_val), 8)  # testing for values...

        list_val = [0, 1, 2, 3, 4, 7, 8, 9, 10]
        self.assertEqual(bin_search(21, 0, len(list_val) - 1, list_val), None)  # testing for value not in list

        list_val = [0, 1, 2, 3, 4, 7, 8, 9, 10, 15]
        self.assertEqual(bin_search(15, 0, len(list_val) - 1, list_val), 9)  # testing for value with different length list (even length)

        list_val = [-1, 1, 2, 3, 4, 7, 8, 9, 10, 15]
        self.assertEqual(bin_search(1, 0, len(list_val) - 1, list_val), 1)  # testing for value...

if __name__ == "__main__":
        unittest.main()



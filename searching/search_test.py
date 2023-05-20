from binary_search import binary_search
from linear_search import linear_search
import unittest


class Test(unittest.TestCase):
    def test_binary_search(self):
        arr = [-1, 3, 5, 7, 7, 7.5, 8, 9, 1000]
        expected = 6
        actual = binary_search(arr, 8)
        self.assertEqual(expected, actual)

    def test_linear_search(self):
        arr = [1, 7, 3, 9, -1, -1, 5]
        expected = 6
        actual = linear_search(arr, 5)
        self.assertEqual(expected, actual)

    def test_value_not_found(self):
        search_methods = [binary_search, linear_search]
        expected = -1
        arr = [1, 2, 3, 5, 6]
        for search_method in search_methods:
            actual = search_method(arr, 4)
            self.assertEqual(expected, actual)

if __name__ == "__main__":
    unittest.main()
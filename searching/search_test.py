from binary_search import binary_search
import unittest


class Test(unittest.TestCase):
    def test_binary_search(self):
        arr = [-1, 3, 5, 7, 7, 7.5, 8, 9, 1000]
        expected = 6
        actual = binary_search(arr, 8)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
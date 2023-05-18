from merge_sort import merge_sort
from insertion_sort import insertion_sort
from selection_sort import selection_sort
from bubble_sort import bubble_sort
import unittest


class Test(unittest.TestCase):
    def test_sort_1(self):
        sort_methods = [merge_sort, insertion_sort, selection_sort,
                        bubble_sort]
        expected = [1, 2, 3, 4, 5, 6]

        for sort_method in sort_methods:
            arr = [1, 5, 3, 6, 4, 2]
            sort_method(arr)
            self.assertEqual(expected, arr)


if __name__ == "__main__":
    unittest.main()


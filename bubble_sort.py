import unittest


def bubble_sort(arr):
    i_end = len(arr) - 1

    for i in range(0, len(arr)):
        for j in range(0, i_end - i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]


class Test(unittest.TestCase):
    def test_merge_1(self):
        arr1 = [1, 5, 3, 6, 4, 2]
        expected = [1, 2, 3, 4, 5, 6]
        bubble_sort(arr1)
        self.assertEqual(expected, arr1)


if __name__ == "__main__":
    unittest.main()

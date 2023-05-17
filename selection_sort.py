import unittest


def selection_sort(arr):
    i = 0

    while i < len(arr)-1:
        for j in range(i+1, len(arr)):
            if arr[j] < arr[i]:
                arr[j], arr[i] = arr[i], arr[j]
        i += 1


class Test(unittest.TestCase):
    def test_merge_1(self):
        arr1 = [1, 5, 3, 6, 4, 2]
        expected = [1, 2, 3, 4, 5, 6]
        selection_sort(arr1)
        self.assertEqual(expected, arr1)


if __name__ == "__main__":
    unittest.main()

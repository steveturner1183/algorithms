import unittest


def insertion_sort(arr):
    i = 0
    j = i + 1

    while i < len(arr)-1:
        while arr[j] < arr[j-1]:
            temp = arr[j-1]
            arr[j-1] = arr[j]
            arr[j] = temp
            j -= 1
        i += 1
        j = i + 1


class Test(unittest.TestCase):
    def test_merge_1(self):
        arr1 = [1, 5, 3, 6, 4, 2]
        expected = [1, 2, 3, 4, 5, 6]
        insertion_sort(arr1)
        self.assertEqual(expected, arr1)


if __name__ == "__main__":
    unittest.main()

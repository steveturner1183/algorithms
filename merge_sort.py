import unittest


def merge_sort(arr):
    if len(arr) <= 1:
        return

    else:
        mid = len(arr) // 2
        # Left and right sides of array
        l_arr = arr[:mid]
        r_arr = arr[mid:]

        # Recursively sort arrays
        merge_sort(l_arr)
        merge_sort(r_arr)

        l_size = len(l_arr)
        r_size = len(r_arr)

        i = j = k = 0

        while i < l_size and j < r_size:
            if l_arr[i] < r_arr[j]:
                arr[k] = l_arr[i]  # fill original with smaller element
                i += 1
            else:
                arr[k] = r_arr[j]  # fill original with smaller element
                j += 1
            k += 1

        # copying remaining elements if any
        while i < l_size:
            arr[k] = l_arr[i]
            k += 1
            i += 1

        while j < r_size:
            arr[k] = r_arr[j]
            k += 1
            j += 1


class Test(unittest.TestCase):
    def test_merge_1(self):
        arr1 = [1, 3, 5, 2, 4, 6]
        expected = [1, 2, 3, 4, 5, 6]
        merge_sort(arr1)
        self.assertEqual(expected, arr1)


if __name__ == "__main__":
    unittest.main()

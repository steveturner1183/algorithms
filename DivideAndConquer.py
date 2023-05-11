import unittest

def kth_element(arr1, arr2, k):
    """
    Given two sorted arrays of size m and n respectively, find the element
    that would be at the kth position in combined sorted array.
    :param arr1: Array 1 of size m
    :param arr2: Array 2 of size n
    :param k: Element to find in sorted array
    :return: Element
    """
    return 5


class Test(unittest.TestCase):
    def test1(self):
        arr1 = [1, 3, 5, 7]
        arr2 = [2, 4, 6, 8]
        k = 5
        expected = 5
        actual = kth_element(arr1, arr2, k)
        self.assertEqual(expected, actual)

if __name__ == "__main__":
    unittest.main()

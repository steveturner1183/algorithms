def partition(arr, low, high):
    pivot = arr[high]

    i = low-1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]

    return i + 1


def quick_sort(arr, low=None, high=None):
    if low is None and high is None:
        low = 0
        high = len(arr) - 1

    if low < high:
        part_i = partition(arr, low, high)

        quick_sort(arr, low, part_i - 1)
        quick_sort(arr, part_i + 1, high)
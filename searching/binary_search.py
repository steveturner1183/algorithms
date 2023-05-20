def binary_search(arr, value):
    low = 0
    high = len(arr) - 1

    while low < high:
        mid = (low + high) // 2

        if arr[mid] == value:
            return mid

        elif value > arr[mid]:
            low = mid

        elif value > arr[mid]:
            high = mid

    return -1

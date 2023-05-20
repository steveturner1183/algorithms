def binary_search(arr, value):
    low = 0
    high = len(arr) - 1

    while low < high:
        mid = (low + high) // 2
        print(low, high, mid)

        if arr[mid] == value:
            return mid

        elif value > arr[mid]:
            low = mid + 1

        elif value < arr[mid]:
            high = mid - 1

    return -1

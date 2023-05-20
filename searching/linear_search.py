def linear_search(arr, value):
    i = 0

    while i < len(arr):
        if arr[i] == value:
            return i
        else:
            i += 1
    return -1
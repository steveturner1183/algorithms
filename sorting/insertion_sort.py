def insertion_sort(arr):
    i = 0
    j = i + 1

    while i < len(arr)-1:
        while arr[j] < arr[j-1]:
            arr[j-1], arr[j] = arr[j], arr[j-1]
            j -= 1
        i += 1
        j = i + 1

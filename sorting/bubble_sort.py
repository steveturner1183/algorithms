def bubble_sort(arr):
    i_end = len(arr) - 1

    for i in range(0, len(arr)):
        for j in range(0, i_end - i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
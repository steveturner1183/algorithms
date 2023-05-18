def selection_sort(arr):
    i = 0

    while i < len(arr)-1:
        for j in range(i+1, len(arr)):
            if arr[j] < arr[i]:
                arr[j], arr[i] = arr[i], arr[j]
        i += 1


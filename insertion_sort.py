def insertionSort2(n, arr):
    # This is selection sort
    # for idx in range(n - 1):
    #     min_idx = idx
    #     for swap_idx in range(idx + 1, n):
    #         min_idx = min(min_idx, swap_idx, key=lambda i: arr[i])

    #     arr[min_idx], arr[idx] = arr[idx], arr[min_idx]
    #     for num in arr:
    #         print(num, end=" ")
    #     else:
    #         print("")
    # return arr

    for start in range(1, n):
        idx = start
        while idx > 0 and arr[idx - 1] > arr[idx]:
            arr[idx - 1], arr[idx] = arr[idx], arr[idx - 1]
            idx -= 1
        for num in arr:
            print(num, end=" ")
        else:
            print("")

    return arr

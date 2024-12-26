def bubble_sort(arr):
    n = len(arr)
    

    for passes in range(0,n):
        for i in range(0, n-1-passes):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]

    return arr    

unsorted_list  = [64, 34, 25, 12, 22, 11, 90]
print(bubble_sort(unsorted_list))

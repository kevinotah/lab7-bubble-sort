def bubblesort(arr: list[int]) -> list[int]:
    if len(arr) <= 1:
        return arr
    
    i = 0
    while i < len(arr):

        for j in range(len(arr) - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
        i += 1
        
    return arr

bubblesort([3, 4, 0, 2, 1, 5])
#bubble sort

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(i+1, n):
            if arr[j]<arr[i]:
                arr[j], arr[i] = arr[i], arr[j]
                swapped = True
        if not swapped:
            break

    return arr
    
arr = [62, 38, 79, 92, 96, 25, 49, 35, 75, 91]

result = bubble_sort(arr)
print(result)


arr = [23,45,67,43,25,3,4,5,68,90]

def max(arr):
    max = arr[0]
    for ele in range(len(arr)):
        if max < arr[ele]:
            max = arr[ele]
    return max

def min(arr):
    min = arr[0]
    for ele in range(len(arr)):
        if min > arr[ele]:
            min = arr[ele]
    return min


max_ele = max(arr)
min_ele = min(arr)
print(f'max is {max_ele} min is {min_ele}')
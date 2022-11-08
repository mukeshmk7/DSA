arr = [23,45,67,43,25,3,4,5,68,90]
search = 67

def bin_search(arr, search):
    arr.sort()
    start, end = 0, len(arr)-1
    while start <= end:
        mid = (start + end)//2
        if arr[mid] < search:
            start = mid + 1
        elif arr[mid] > search:
            end = mid - 1
        elif arr[mid] == search:
            return f'{search} is found in arr'
    else:
        return -1

find_ele = bin_search(arr, search)
print(find_ele)
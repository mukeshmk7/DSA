arr = [90, 80, 70, 60, 50, 40]
search = 60

def bin_search(arr, search):
    start, end = 0, len(arr)-1
    while start <= end:
        mid = (start + end)//2
        if arr[mid] < search:
            end = mid - 1
        elif arr[mid] > search:
            start = mid + 1
        elif arr[mid] == search:
            return f'{search} is found in arr'
    else:
        return -1

find_ele = bin_search(arr, search)
print(find_ele)
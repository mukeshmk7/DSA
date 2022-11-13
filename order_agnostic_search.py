arr = [5, 7, 17, 22, 56, 79]
search = 56

def is_asc(arr):
    start, end = 0, len(arr)-1
    if arr[start] < arr[end]:
        return True
    return False

def binary_search(arr, search):
    start, end = 0, len(arr)-1
    is_ascending = is_asc(arr)
    while start <= end:
        mid = (start + end)//2
        if arr[mid] < search:
            if is_ascending:
                start = mid + 1
            else:
                end = mid - 1
        elif arr[mid] > search:
            if is_ascending:
                end = mid - 1
            else:
                start = mid + 1
        elif arr[mid] == search:
            return search
    else:
        return -1

print(binary_search(arr, search))


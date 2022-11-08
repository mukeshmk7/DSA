arr = [
    [10,20,32],
    [101,120,132,165],
    [110,210,312],
]

search = 210

def search_2d(arr, search):
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] == search:
                return f'element {search} is found in {i+1} row and {j+1} column'
    else:
        return -1


find_pos = search_2d(arr, search)
print(find_pos)


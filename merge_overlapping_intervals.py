a = [(1, 3), (5, 8), (4, 10), (20, 25)]

def merge_intervals(arr):
    arr.sort(key= lambda x: x[0])
    stop = len(arr)-1
    i = 0
    while i < stop:
        if arr[i][1] >= arr[i+1][0]:
            stop -= 1
            arr[i] = (arr[i][0],max(arr[i+1][1],arr[i][1]))
            del arr[i+1]
        i += 1
    return arr


print(merge_intervals(a))#[(1, 3), (4, 10), (20, 25)]
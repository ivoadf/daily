a = [5,7,11,43,76,412,888,951,1001,1020,1320]

def linear_search(arr,x):
    for i,y in enumerate(arr):
        if x == y:
            return i
    return -1

print(linear_search(a,951))

def binary_search(arr,l,r,x):
    mid = l + (r-l)//2
    if x < arr[mid]:
        return binary_search(arr,l,mid,x)
    elif x > arr[mid]:
        return binary_search(arr,mid,r,x)
    else:
        return mid

print(binary_search(a,0,len(a),951))

def jump_search(arr,x):
    step_size = 3
    index = 0
    while index < len(arr)-step_size:
        if x >= arr[index] and x <= arr[index+step_size]:
            for i in range(index,index+step_size+1):
                if arr[i] == x:
                    return i
        else:
            index += step_size

def exponential_search(arr,size,x):
    id = size-1
    if arr[id] < x:
        if size*2 < len(arr):
            return exponential_search(arr,size*2,x)
        else:
            return -1
    elif arr[id] > x:
        return binary_search(arr,size/2,id,x)
    else:
        return id
print(exponential_search(a,1,951))


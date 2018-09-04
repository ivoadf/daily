arr = [5,2,6,53,134,55,332,762,22]

def selection_sort(arr):
    for i in range(len(arr)):
        min_id = i
        for j in range(i+1,len(arr)):
            if arr[min_id] > arr[j]:
                min_id = j
        arr[min_id],arr[i] = arr[i], arr[min_id]
    return arr

print(selection_sort(arr))

arr = [5,2,6,53,134,55,332,762,22]
def bubble_sort(arr):
    for i in range(len(arr)):
        swaps = 0
        for j in range(1,len(arr)-i):
            if arr[j-1] > arr[j]:
                arr[j-1], arr[j] = arr[j], arr[j-1]
                swaps += 1
        if swaps == 0:
            break
    return arr

print(bubble_sort(arr))

arr = [5,2,6,53,134,55,332,762,22]
def insertion_sort(arr):
    for i in range(1,len(arr)):
        elem = arr[i]
        j = i-1 #index of last sorted elem
        while j >= 0 and elem < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = elem
    return arr

print(insertion_sort(arr))

arr = [5,2,6,53,134,55,332,762,22]
def heap_sort(arr): 
    # n - heap size
    # i - root id
    def heapify(arr,n,i):
        largest = i
        left = 2*i+1
        right = 2*i+2

        if left < n and arr[left] > arr[largest]:
            largest = left
        if right < n and arr[right] > arr[largest]:
            largest = right
        if largest != i:
            arr[i],arr[largest] = arr[largest],arr[i]
            heapify(arr,n,largest)
    # build max heap
    for i in range(len(arr),-1,-1):
        heapify(arr,len(arr),i)
    # extract max elements
    for i in range(len(arr)-1,0,-1):
        arr[i],arr[0] = arr[0],arr[i] # swap max with last elem
        heapify(arr,i,0) # move new elem to right spot, ignoring last elems that are already sorted
    return arr

print(heap_sort(arr))

arr = [5,2,6,53,134,55,332,762,22]
def quick_sort(arr,low,high):
    # assume pivot is last elem arr[high]
    def partition(arr,low,high):
        i = low -1 # id-1 to place values smaller than pivot
        for j in range(low,high):
            if arr[j]<arr[high]:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i+1], arr[high] = arr[high], arr[i+1]
        return i+1

    if low < high:
        split_id = partition(arr,low,high)
        quick_sort(arr,low,split_id-1)
        quick_sort(arr,split_id+1,high)

quick_sort(arr,0,len(arr)-1)
print(arr)

arr = [5,2,6,53,134,55,332,762,22]
def merge_sort(arr,l,r):
    def merge(arr,l, m, r):
        n1 = m - l + 1
        n2 = r- m
 
        # create temp arrays
        L = [0] * (n1)
        R = [0] * (n2)
 
        # Copy data to temp arrays L[] and R[]
        for i in range(0 , n1):
            L[i] = arr[l + i]
 
        for j in range(0 , n2):
            R[j] = arr[m + 1 + j]
        
        # Merge the temp arrays back into arr[l..r]
        i = 0     # Initial index of first subarray
        j = 0     # Initial index of second subarray
        k = l     # Initial index of merged subarray
 
        while i < n1 and j < n2 :
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        
            # Copy the remaining elements of L[], if there are any
        while i < n1:
            arr[k] = L[i]
            i += 1
            k += 1
 
        # Copy the remaining elements of R[], if there are any
        while j < n2:
            arr[k] = R[j]
            j += 1
            k += 1
    if l < r:
        middle = (r+l)//2
        merge_sort(arr,l,middle)
        merge_sort(arr,middle+1,r)
        merge(arr,l,middle,r)
merge_sort(arr,0,len(arr)-1)
print(arr)

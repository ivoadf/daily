def heapify(arr, root_id):
    tmp = root_id
    heap_size = len(arr)
    left = 2*root_id + 1
    right = 2*root_id + 2

    if left < heap_size and arr[left][1] > arr[root_id][1]:
        tmp = left
    elif right < heap_size and arr[right][1] > arr[root_id][1]:
        tmp = right
    if tmp != root_id:
        arr[tmp], arr[root_id] = arr[root_id], arr[tmp]
        heapify(arr,tmp)

def build_heap(arr):
    for i in range(len(arr)-1, -1, -1):
        heapify(arr, i)

def no_adjecent_chars(s):
    frequency_map = {}
    for c in s:
        if c in frequency_map:
            frequency_map[c] += 1
        else:
            frequency_map[c] = 1
    arr = [(k,v) for k,v in frequency_map.items()]
    build_heap(arr)
    result_string = arr[0][0] #start with most frequent character
    arr[0] = (arr[0][0], arr[0][1]-1) # reduce frequency
    element_waiting = True
    w_id = 0 # element waiting id
    while len(result_string) < len(s) and w_id < len(arr)-1:
        heapify(arr, w_id+1)
        result_string += arr[w_id+1][0]
        arr[w_id+1] = (arr[w_id+1][0], arr[w_id+1][1]-1)
        #swap element waiting
        if element_waiting:
            arr[w_id], arr[w_id+1] = arr[w_id+1], arr[w_id]
            if arr[w_id][1] == 0:
                element_waiting = False
        else:
            w_id += 1
            element_waiting = True
    if element_waiting:
        return None
    return result_string

print(no_adjecent_chars("aaabbc"))
print(no_adjecent_chars("aa"))

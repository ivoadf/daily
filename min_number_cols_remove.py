a = [
    'cba',
    'daf',
    'ghi'
]

b = [
    'ca',
    'df',
    'gi'
]

c = [
    'abcdef'
]

d = [
    'zyx',
    'wvu',
    'tsr'
]

def number_cols(arr,N,M):
    count = 0
    for i in range(M):
        for j in range(N-1):
            if arr[j][i] > arr[j+1][i]:
                count += 1
                break
    return count

print(number_cols(a,3,3))#1
print(number_cols(b,3,2))#0
print(number_cols(c,1,6))#0
print(number_cols(d,3,3))#3
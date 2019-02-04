def edit_distance(s1, s2):
    # extra row in each dimension to represent length 0 strings
    store = [None]*(len(s1)+1)
    for i in range(len(store)):
        store[i] = [-1]*(len(s2)+1)
    for i in range(len(s1)+1):
        for j in range(len(s2)+1):
            if i == 0: # empty s1
                store[i][j] = j
            elif j == 0: #empty s2
                store[i][j] = i

            elif s1[i-1] == s2[j-1]: # CAREFUL! errors by one here. necessary because store matrix represents length 0 strings as well
                store[i][j] = store[i-1][j-1] # same edit distance as previous substrings
            else:
                store[i][j] = min(store[i][j-1], store[i-1][j], store[i-1][j-1]) + 1

    return store[len(s1)][len(s2)]
str1 = "sunday"
str2 = "saturday"

print(edit_distance(str1, str2))

s1 = "banana" #anana
s2 = "aabcdcb" #bcdcb

def find_longest_pal(s):
    max_len = 0
    start = 0
    # [i,j] = sub_string[i,j] is palindrome = 1 else = 0
    dynam_tab = [[False for _ in range(len(s))] for _ in range(len(s))]

    #all strings size 1 are palidromes
    for i in range(len(s)):
        dynam_tab[i][i] = True
    #check strings of size 2
    for i in range(len(s)-1):
        if s[i] == s[+1]:
            dynam_tab[i][i+1] = True
    #fill table for rest of substrings
    for l in range(3,len(s)+1):
        for start_id in range(0,len(s)-l+1):
            end_id = start_id + l - 1
            if dynam_tab[start_id+1][end_id-1] and s[start_id] == s[end_id]:
                dynam_tab[start_id][end_id] = True
                if l > max_len:
                    max_len = l
                    start = start_id
    return s[start:start+max_len]

print(find_longest_pal(s1))
print(find_longest_pal(s2))

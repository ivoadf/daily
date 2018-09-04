m = [[1,  2,  3,  4,  5],
    [6,  7,  8,  9,  10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20]]

def print_spiral(m):
    h_max = len(m[0])-1
    v_max = len(m)-1
    h_start = 0
    v_start = 0
    h = h_start
    v = v_start
    num_prints = 0
    while num_prints < len(m)*len(m[0]):
        print(m[v][h])
        num_prints += 1
        if h == h_start and v == v_start+1:#end of loop
            h_start += 1
            v_start += 1
            h_max -= 1
            v_max -= 1
            h = h_start
            v = v_start
            continue
        #top
        if v == v_start and h < h_max:
            h += 1
        #right
        elif v < v_max and h == h_max:
            v += 1
        #bottom
        elif v == v_max and h > h_start:
            h -= 1
        #left
        elif h == h_start and v > v_start:
            v -= 1

print_spiral(m)
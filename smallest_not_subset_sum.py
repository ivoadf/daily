def smallest(a):
    candidate = 1
    for i in range(len(a)):
        if a[i] <= candidate:
            """
            At each iteration you know that it's possible to make all values
            from 1 to candidate-1. if that is true and a[i]<=candidate you can make all values from
            1 to candidate-1+a[i].
            Ex: candidate=7 a[i]=7
            you know that all values between 1 and 6 can be achieved with sums if not candidate is incorrect
            1,2,3,4,5,6
            if you sum a[i]=7 to those you can make all the values until candidate-1 + a[i]
            7 = 1+6
            8 = 2+6
            9 = 3+6
            .
            .
            .
            13 = 7+6
            So next candidate will be 14 = candidate+a[i]
            """
            candidate += a[i]
        else:
            break
    return candidate

print(smallest([1,2,3,10])) #7
print(smallest([2,5,10])) #1
print(smallest([1,2,3,7])) #14
print(smallest([1,1,1,1])) #5

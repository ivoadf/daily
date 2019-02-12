def kill(N, step):
    if N == 1:
        return 1
    return (kill(N - 1, step) + step-1) % N + 1



print(kill(5,2)) #[2, 4, 1, 5, 3]
print(kill(4,3)) #[3, 2, 4, 1]
print(kill(4,2)) #[2, 4, 3, 1]

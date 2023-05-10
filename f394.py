def print_pattern(n):
    for i in range(n, 0, -1):
        print(" " * (i-1))
        for j in range(n, i-1, -1):
            print(j, end=" ")
        for k in range(i+1, n+1):
            print(k, end=" ")
        print()

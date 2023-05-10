def print_pattern(n):
    for i in range(0,n):
        for j in range(0, i):
            print(" ", end="")
        for k in range(n, i, -1):
            print(k, end="")
        for l in range(i+2, n+1, 1):
            print(l, end="")
        print()

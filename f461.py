def print_pattern(n):
    p = n-1
    for i in range(n):
        for j in range(p):
            print(" ", end="")
            m = 0
        for k in range(n, n-i, -1):
            print(k, end="")
            m = k
        for l in range(m+1, n+1):
            print(l, end="")
        p = p -1
        print()

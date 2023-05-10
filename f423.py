def print_pattern(n):
    sp = n - 1
    for i in range(n):
        for j in range(sp):
            print(" ", end="")
        m=0
        for k in range(n, n-i, -1):
            print(k, end="")
            m = k
        for l in range(m+1, n+1):
            print(l, end="")
        sp = sp - 1
        print()

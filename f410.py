def print_pattern(n):
    for p in range(0, n):
        if p == 0:
            print(n)
        if p == 1:
            print(str(n) + str(n-1) + str(n))
        else:
            for p in range(n, 3-p):
                print(str(p), end="")
            for k in range(n+1-p, n):
                print(str(k), end="")
                print(str(n))

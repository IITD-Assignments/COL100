def print_pattern(n):
    s = n-1
    for i in range(n):
        for k in range(s):
            print(" ", end="")
        for l in range(n, n-i-1, -1):
            print(l, end="")
        for t in range(n-i, n):
            print(t, end="")
        print()
        s -= 1

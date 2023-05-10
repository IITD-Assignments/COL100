def print_pattern(n):
    for i in range(1, n+1):
        for j in range(0, i):
            print(" ", end="")
            j = j + 1
        for k in range(n, i-1):
            print(k, end="")
            k = k -1
        for l in range(i+1, n+1):
            print(l, end="")
            l = l + 1
        print()
        i = i + 1

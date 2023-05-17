def print_pattern(n):
    k = n
    s = str(n)
    L = range(1, n+1)
    for a in range(n):
        print(" " * (k-1), s)
        s = ""
        for b in range(-1, -a-2, -1):
            s += str(L[b])
        s = s[:] + s[-2::-1]
        k-=1

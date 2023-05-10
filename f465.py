def print_pattern(n):
    l = []
    for a in range(n, 0, -1):
        l.append(a)
    for i in range(0, n):
        print(" " * (n-i-1), end="")
        for j in range(0, i+1):
            print(l[j], end="")
        for k in range(i-1, -1, -1):
            print(l[j], end="")

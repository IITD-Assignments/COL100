def print_pattern(n):
    for i in range(n):
        a1 = []
        a2 = []
        for t in range(i+1, n+1):
            a2 = a2 + str(t)
        for s in range(n, i+1, -1):
            a1 = a1 + str(s)

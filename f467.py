def print_pattern(n):
    for i in range(n):
        L = []
        for j in range(2 * i + 1):
            L.append(0)
        for j in range(i + 1):
            L[j] = n - j
        if i != 0:
            for j in range(i):
                L[-j-1] = n-j
        s = " "
        for k in L:
                s = s + str(k)
            
        return s

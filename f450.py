def print_pattern(n):
    for j in range(1, n+1):
        l = []
        k = 0
        while k < j-1:
            l.append(" ")
            k += 1
        for i in range(n, j-1, -1):
            l.append(str(i))
        ls = l[-2:-n:-1]
        l = l + ls
        print("".join(l))

def print_pattern(n):
    l1 = []
    for i in range(n):
        l2 = [" " for j in range(2 * n - 1)]
        for k in range(i, n-1):
            l2[k] = n-k+i
            l2[-1-k] = n-k+i
        l2[n-1] = i + 1
        l1.append(l2)
    for i in l1:
        for k in l2:
            print(k, sep="")
        print()

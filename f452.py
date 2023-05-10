def print_pattern(n):
    for i in range(1, n+1):
        l = []
        l2 = []
        for j in range(i, 0, -1):
            l.append(j)
        l1 = l[1::-1]
        del l[0]
        l2 = l + l1
        print(" " * (i-1), end=" ")
        for ch in l2:
            print(ch, end="")
        print()

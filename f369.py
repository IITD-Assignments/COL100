def print_pattern(n):
    elt = 1
    for i in range(n, 0, -1):
        print(" " * (i-1), end="")
        a = n
        for j in range(elt // 2 + 1):
            print(a, end="")
            a = a - 1
        a = a + 1
        for k in range(elt // 2):
            print(a, end="")
            a = a + 1
        print()
        elt = elt + 2
    
def print_pattern(n):
    for i in range(1, n+1):
        k = i -1
        print(" " * k, end="")
        for j in range(n, i, -1):
            print(j, end="")
        for m in range(i, n+1):
            print(m, end="")
        print()

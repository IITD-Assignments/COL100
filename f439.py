def print_pattern(n):
    for i in range(1, n+1):
        for l in range(0, i-1):
            print(" ", end="")
        for j in range(n, i-1):
            print(j, end="")
        for k in range(i+1, n+1):
            print(k, end="")
        print()

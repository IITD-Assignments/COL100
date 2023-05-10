def print_pattern(n):
    for i in range(n):
        print(i * " ", end="")
        for j in range(n, i, -1):
            print(j, end="")
        for k in range(i+2, n+1):
            print(k, end="")
        print()

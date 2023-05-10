def print_pattern(n):
    for i in range(n):
        if (i > 0):
            print(i * " ", end="")
        for j in range(n, i, -1):
            print(j, end="")
        for k in range(i+1, n+1):
            print(k, end="")
        if (i>0):
            print(i * " ", end="")
        print()


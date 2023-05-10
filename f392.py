def print_pattern(n):
    x = n
    for i in range(n, 0, -1):
        x = n
        for j in range(2*n):
            if (j <= n-1):
                print(x, end="")
                x=x-1
            else:
                x=x+1
                print(x, end="")
        print()
        print(" ", end="")

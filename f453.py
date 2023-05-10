def print_pattern(n):
    for i in range(1, n+1):
        for j in range(n-i, 0, -1):
            print(" ", end="")
        for x in range(n, n+1-i, -1):
            print(x, end="")
        for y in range(n+2-i, n+1):
            print(y, end="")
        print(" ")

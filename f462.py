def print_pattern(n):
    for i in range(1, n+1):
        print(" " * (n-i), end="")
        for j in range(n, n-i, -1):
            print(j, end="")
        for k in range(n-i+2, n+1):
            print(k, end="")
        print(" " * (n-i))

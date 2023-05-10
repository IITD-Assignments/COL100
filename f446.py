def print_pattern(n):
    for i in range(n):
        for j in range(0, n-(i-1)):
            print(end=" ")
        for k in range(n, 0, -1):
            print(k, end="")

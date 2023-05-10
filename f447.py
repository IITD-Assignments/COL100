def print_pattern(n):
    for i in range(1,n):
        print(" " * (i-1), end="")
        for j in range(i, 1, -1):
            print(j, end="")
        for j in range(2, i+1):
            print(j, end="")
        print()

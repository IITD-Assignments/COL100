def print_pattern(n):
    for i in range(n, 0, -1):
        for j in range(i, 0, -1):
            print(i, end="")
            if j == 1:
                for k in range(1, i):
                    print(i, end="")
    print(" ")

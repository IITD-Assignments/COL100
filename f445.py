def print_pattern(n):
    for i in range(n, 0, -1):
        if i == 1:
            print(i)
        else:
            for j in range(i, 1, -1):
                print(j, end="")
            for j in range(1, i+1):
                print(j, end="")
            print()

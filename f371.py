def print_pattern(n):
    for i in range(1, n+1):
        for j in range(1, 2 * n):
            if abs(n-j) <= i-1:
                print(abs(n-j) + n + 1 - i, end="")
                print("", end="")

        print("")

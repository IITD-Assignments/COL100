def print_pattern(n):
    for i in range(1, n+1):
        for k in range(i-1):
            print(" ", end="")
        j = n
        while (j >= i):
            print(j, end="")
            j -= 1
        j = i + 1
        while (j <= n):
            print(j, end="")
            j += 1
        print(" ")
def print_pattern(n):
    for i in range(1, n+1):
        for j in range(1, 2*n):
            if (j > n-i) and (j < n + i):
                if j <= n:
                    print(2*n-j-i+1, end="")
                else:
                    print(j+1-i, end="")
            else:
                print(" ", end="")
        print()

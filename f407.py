def print_pattern(n):
    for i in range(1, n+1):
        for j in range(n-i+1):
            print(j+1, end="")
            for j in range(n-i,n):
                print(n-i+1, end="")
            for j in range(n, n+i):
                print(n-i+1, end="")
            for j in range(n+i, 2*n):
                print(j-n+1, end="")
                print()

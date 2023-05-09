def print_pattern(n):
    for i in range(n):
        for z in range(i+1):
            print(" ", end="")
        for j in range(n-i):
            print(n-j, end="")
        for k in range(2*n-1-n-i):
            print(n-i+k+k, end="")
        print()

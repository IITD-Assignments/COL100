def print_pattern(n):
    for i in range(1, n+1):
        for j in range(n, i, -1):
            print(j, end="")
        for k in range(i, n+1):
            print(k, end="")
    
        print()

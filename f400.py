def print_pattern(n):
    for i in range(n):
        for l in range(i+2, n+1):
            for j in range(n, i, -1):
                print(j, end="")
            for k in range(l, n+1):
                print(k, end="")
            
            print()
        if i == (n-1):
            print(n)

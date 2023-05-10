def print_pattern(n):
    for start in range(0,n):
        for k in range(n, start, -1):
            print(k, end="")
        for k in range(start+2,n+1):
            print(k, end="")
        print()

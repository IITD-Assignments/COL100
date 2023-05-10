def print_pattern(n):
    r = 1
    while (r <= n):
        c = 1
        while (c <= n-r):
            print(" ", end="")
            c = c + 1
        while (c <= n):
            print(-c-r+1+2*n, end="")
            c = c+1
        while (c <= n+r-1):
            print(c-r+1, end="")
            c = c + 1
        r = r + 1
        print("")

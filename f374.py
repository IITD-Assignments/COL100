def print_pattern(n):
    print((n+1)*" " + str(n))
    for i in range(n-1, 1, -1):
        s = ""
        for j in range(n, i-1, -1):
            s = s + str(j)
        s = s + str(i-1) + s[::-1]
        print()

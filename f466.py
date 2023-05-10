def print_pattern(n):
    for i in range(1, n+1):
        s = " "
        for j in range(i, 2 *n-i+1):
            x = abs(n-j) + i
            s += str(x)
        print(int(s))

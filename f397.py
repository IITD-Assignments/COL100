def print_pattern(n):
    s = ""
    for i in range(n, 0, -1):
        s = s + str(i)
    for j in range(1, n+1):
        p = str(n) + s[1:j] + s[:] + str(n)
        print(p)

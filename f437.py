def print_pattern(n):
    for i in range(n):
        s1 = ""
        s2 = ""
        for t in range(i+1, n+1):
            s2 = s2 + str(t)
        for p in range(n, i+1, -1):
            s1 = s1 + str(p)
        s3 = " "
        s4 = ""
        for l in range(i):
            s4 = s4 + s3
        print(s4 + s1 + s2 + s4)

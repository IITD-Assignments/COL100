def print_pattern(n):
    p = str(n)
    s = p
    t = n
    for i in range(n):
        if (i == 1):
            print(s)
        else:
            print(s + str(t) + reversed(s))
        t = t - 1
        s = s[0:int(len(s) / 2) + 1] + str(t)

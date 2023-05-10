def print_pattern(n):
    for i in range(n):
        s = " " * i
        k = n
        a = ""
        while (k <= n):
            a = a + str(k)
            k = k - 1
        print(s + a + s)

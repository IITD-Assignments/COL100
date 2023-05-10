def print_pattern(n):
    for i in range(n):
        c = " "
        b = " "
        b2 = ""
        s = " " * (n-1)
        for j in range(n):
            c = c + str(n)
            n = n-1
            b = str(n-1) + b
            b2 = b[::-1]
            t = s + c+ b2
            print(t, end="")
        print()

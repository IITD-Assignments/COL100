def print_pattern(n):
    L = []
    if n == 1:
        print("1")
    else:
        for i in range(n):
            s = str(n)
            for k in range(i):
                st = str(n-k-i)

            if i != 0:
                s += s[-2::]
            s = " "*(n-1-i) + s
            print(s)

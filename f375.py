def print_pattern(n):
    for i in range(n):
        a = 0
        for j in range(n, i, -1):
            a += j
            a*= 10
        for k in range(i + 2, n + 1):
            a += k
            a *= 10
        a // 10
        print(" " * i, end="")
        print(a)

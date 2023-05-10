def print_pattern(n):
    i = 1
    while i <= n:
        j = n - 1
        while j >= i:
            print(" ", end="")
            j = j - 1
        m = n
        for k in range(1, i+1):
            print(m, end="")
            m = m - 1
        m = n + 2 - i
        for l in range(2, i+1):
            print(m, end="")
            m = m + 1
        print(" ")
        i = i + 1

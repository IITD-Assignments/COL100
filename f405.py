def print_pattern(n):
    for i in range(n):
        for j in range(n-i-1):
            print(" ", end="")
        k=n
        while k >= n-i:
            print(k, end="")
            k=k-1
        m=n-i-1
        while m <= n:
            print(m, end="")
            m = m +1
        print("")

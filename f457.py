def print_pattern(n):
    for i in range(1, n, -1):
        def patt(i, n):
            if n == i:
                break
            else:
                return str(n) + patt(i, n-1) + str(n)
        
        print(patt(n))

def print_pattern(n):
    def a(k):
        def num1(k, n):
            a = []
            for i in range(n, k+1, -1):
                a.append(i)  ## fixed
            return a

        def num2(k,n):
            b = []
            for j in range(k+1, n+1):
                b.append(j)  ## fixed
            return b

        l = num1(k,n)  ## fixed
        l.append(num2(k,n))
        return l

    for k in range(1, n+1):
        print(a(k))

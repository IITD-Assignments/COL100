def print_pattern(n):
    n = int(n)
    if n == 1:
        print(1)
    if n == 2:
        print("212")
        print("2")
    else:
        for i in range(0, n):
            L = []
            for j in range(n,i,-1):
                L.append(str(j))
            for k in range(i+2, n+1):
                L.append(str(k))
            print(" " * i)
            for m in L:
                print(m, end=" ")
            print()

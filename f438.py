def print_pattern(n):
    for j in range(0,n):
        k = ""
        for i in range(n, j, -1):
            k = k + str(i)
        k = k + k[len(k)-2:-1:-1]

        print(k)
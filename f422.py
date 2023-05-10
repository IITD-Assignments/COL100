def print_pattern(n):
    for i in range(0, n):
        t = i
        while (t > 0):
            print(" ", end="")
            t -= 1
        for j in range(n, i, -1):
            print(j, end="")
        if (i+2 <= n):
            for j in range(i+2, n+1):
                print(j, end="")
        
        print()

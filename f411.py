def print_pattern(n):
    for i in range(n, 0, -1):
        k = n
        for j in range(n-i):
            print(" ", end="")
        for j in range(i):
            print(k, end="")
            k = k - 1
        for j in range(i-2):
            k = k + 1
            print(k, end="")
        for j in range(3-i):
            print(" ", end="")
        
        print("\n")

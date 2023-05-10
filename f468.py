def print_pattern(n):
    for i in range(n):
        for j in range(n-i+1):
            print(" ", end="")
        for k in range(i +1):
            print(n-k, end="")
        for l in range(i):
            print(n-i+1+l, end="")
        for m in range(n-i+1):
            print(" ", end="")
        print()

def print_pattern(n):
    for i in range(n):
        for j in range(i):
            print(" ", end="")
        for j in range(n-i-1):
            print(n-j, end="")
        print(i+1, end="")
        for j in range(n-i-1):
            print(i+j+2, end="")
        for j in range(i):
            print(" ", end="")
        print("")

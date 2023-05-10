def print_pattern(n):
    for i in range(1, n+1):
        print(" " * (4-i), end="")
        for j in range(i):
            print(str(n+1-i), end="")
        k=i-1
        m=1
        while k>= 1:
            print(str(n+1-i+m), end="")
            m+=1
            k-=1
        print(" " * (4-i), end="")
        print()

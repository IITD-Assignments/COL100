def print_pattern(n):
    i = 1
    j = n
    while (i <= n):
        print(" " * (i-1), end="")
        j = n
        while (j >= i):
            print(j, end="")
            j -=1
        
        j = i + 1
        while (j <= n):
            print(j, end="")
            j += 1
        
        i+= 1
        print("")

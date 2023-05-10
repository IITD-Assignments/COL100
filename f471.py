def print_pattern(n):
    for i in range(n):
        # j = n  ## fixed
        while j >= i:
            print(j)
            j = j-1
        while j+1 <= n:
            print(j+1)
            j = j + 1
        k = 0
        while (k < i):
            print(" ")
            k = k + 1
        print(' ')

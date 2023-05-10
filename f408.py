def print_pattern(n):
    i = n
    while i >= 1:
        k = n
        j = i
        while j >= 1:
            print(k, end="")
            k -= 1
            j -= 1
        j = 2
        k += 1
        while j <= i:
            print(k, end="")
            k += 1
            j += 1
        print("")
        i-=1

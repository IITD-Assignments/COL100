def print_pattern(n):
    i = 1
    for i in range(i, n):
        if i < n:
            patt = i + 1, i, i + 1
            print(end="")
            print(i)
            i+=1
            return patt
        elif i == 1:  ## fixed
            print(i)

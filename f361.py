def print_pattern(n):
    s = [1, 2, 3, 4, 5, 6, 7]
    if n == 1:
        return 1

    if n > 1:
        i = 0
        j = 1
        res = " "
        for k in range(j):
            res = s[i] + print_pattern(i-1) + s[i]
            j = j - 1
        
        return res
def print_pattern(n):
    while True:
        if n < 5:
            for i in range(1, n):
                for j in range(1, i+1):
                    if i == j:
                        return i
                        break
                    elif i < j:
                        return i, i-1
                        break

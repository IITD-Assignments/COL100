def print_pattern(n):
    for i in range(1, n+1):
        temp = n
        for j in range(i, 2 * n - i + 1):
            print(temp, end="")
            if (j <= n):
                temp -= 1
            else:
                temp += 1
        
        print()

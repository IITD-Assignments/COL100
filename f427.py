def print_pattern(n):
    for i in range(n):
        length = 2 * i + 1
        string = " "
        k = n
        for i in range(length // 2 + 1):
            string += str(k)
            k -= 1
        if len(string) == 1:
            print(string)
        else:
            print(string + (string[::-1])[1::])

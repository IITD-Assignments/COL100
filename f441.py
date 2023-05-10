def print_pattern(n):
    list_1 = []
    list_2 = []
    for i in range(0, n):
        if i == 0:
            list_2.append(n)
            list_1.append(list_2)
        else:
            for j in range(0, 2*i+1):
                if j == 0 or j == 2 * i:
                    list_2.append(n)
                else:
                    if i - j >= 0:
                        list_2.append(n-j)
                    else:
                        list_2.append(n+i-j)
            list_1.append(list_2)

    print(list_1, list_2)

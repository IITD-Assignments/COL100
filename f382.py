def print_pattern(n):
    if n > 1:
        arr1 = []
        arr2 = []
        for i in range(1, n+1):
            arr1.append(i)
        for i in range(n, 0, -1):
            arr2.append(i)
        while len(arr1) != 0:
            # arr = arr2.extend(arr1)
            arr = arr2.copy()
            arr.extend(arr1)
            for j in arr:
                print(j, end="")
            print()
            arr2 = arr2[0:-2]
            arr1 = arr1[1:-1]
        print(arr2[0])
    elif n == 1:
        print(1)

def print_pattern(n):
    for i in range(n, 0, -1):
        for j in range(n, 0, -1):
            while j >= 1:  ## fixed
                print(j, end=" ")
            while j < n:
                print(j+1, end="")
                j = j+ 1
        print("\n")

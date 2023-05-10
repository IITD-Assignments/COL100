def print_pattern(n):
    for i in range(n):
        print((n-i-1) * " ")
        for j in range(2*i+1):
            if j<= i:
                print(n-j, end="")
            else:
                print(j+n-2*i, end="")
        print("\n")

def print_pattern(n):
    for i in range(1, n+1):
        line = ""
        for j in range(i, n+1):
            if j == i:
                line += str(j)
            else:
                line = str(j) + line + str(j)
        
        line = " " * int((2*n-1-len(line))/2) + line  ## fixed
        print(line)

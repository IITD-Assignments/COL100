def print_pattern(n):
    a = "1"
    for i in range(2, n+1):
        a  = str(i) + a + str(i)
    for k in range(0, n):
        print(int(a[n-1-k:n+k]))

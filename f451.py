def print_pattern(n):
    for k in range(n):
        p = k + 1
        pr_out = str(p)
        while p < n:
            pr_out = str(p+1) + pr_out + str(p+1)
            p += 1
        print(pr_out)

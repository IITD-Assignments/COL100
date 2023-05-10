def print_pattern(n):
    if n == 1:
        return 1
    else:
        Li1 = []
        for i in range(n):
            Li1.append(i)
            # Li2 = Li1.reverse()
            Li2 = Li1.copy()
            Li2.reverse()
            b = Li1 + Li2

    if len(b) % 2 == len(b):
        for j in range(i):
            b.remove(len(b) // 2)
    
    if len(b) % 2 == 0:
        for k in range(len(b)):
            b.remove(len(b)//2 + len(b)//2 + 1)
    
    print(c for c in range(len(b)))

def print_pattern(n):
    if n == 1:
        return 1
    if n > 1:
        row = [n]
        for i in range(1, n+1):
            new_row = [n]
            for j in range(1, i):
                new_row.append(row[j-1]-1)
            new_row.append(n)
        row = new_row
    
    return row

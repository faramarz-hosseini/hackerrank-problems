def pageCount(n, p):
    flips = []
    current_start = [0, 1]
    if n % 2 == 0:
        current_end = [n, n + 1]
    else:
        current_end = [n-1, n]

    flip_num_from_start = 0
    flip_num_from_end = 0

    for i in range(1, n+1, 2):
        if p in current_start:
            flips.append(flip_num_from_start)
            break
        flip_num_from_start += 1
        current_start = [i+1, i+2]

    for i in range(n, 1, -2):
        if p in current_end:
            flips.append(flip_num_from_end)
            break
        flip_num_from_end += 1
        if n % 2 == 0:
            current_end = [i-2, i-1]
        else:
            current_end = [i-3, i-2]
    return min(flips)

print(pageCount(6, 5))
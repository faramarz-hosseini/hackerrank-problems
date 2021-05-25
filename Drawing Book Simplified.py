def pageCount(n, p):
    pages_from_start = []
    flips_needed = []
    x = 0
    for i in range(n//2 + 1):
        pages_from_start.append((x, x+1))
        x += 2

    pages_from_end = [i for i in pages_from_start[::-1]]
    for page in pages_from_start:
        if p in page:
            flips_needed.append(pages_from_start.index(page))
    for page in pages_from_end:
        if p in page:
            flips_needed.append(pages_from_end.index(page))
    return min(flips_needed)

print(pageCount(5, 4))
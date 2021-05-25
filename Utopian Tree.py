def utopian_tree(n):
    growth = 1
    for cycle in range(1, n+1):
        if cycle % 2 != 0:
            growth *= 2
        else:
            growth += 1
    return growth


print(utopian_tree(4))

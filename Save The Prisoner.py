def save_the_prisoner(n, m, s):
    return ((s-1+m-1) % n) + 1


print(save_the_prisoner(7, 19, 2))

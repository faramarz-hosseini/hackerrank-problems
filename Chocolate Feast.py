def chocolate_feast(n, c, m):
    initial_candies = n // c
    initial_wrappers = initial_candies
    while initial_wrappers >= m:
        initial_candies += 1
        initial_wrappers -= m - 1

    return initial_candies


chocolate_feast(12, 4, 4)

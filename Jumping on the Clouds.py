def jumping_on_the_clouds(c):
    max_index = len(c) - 1
    index = 0
    jumps = 0
    while index < max_index:
        if index + 2 <= max_index and c[index+2] == 0:
            index += 2
            jumps += 1
        else:
            index += 1
            jumps += 1
    return jumps


print(jumping_on_the_clouds([0, 0, 1, 0, 0, 1, 0]))

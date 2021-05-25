import math


def squares(a, b):
    square_ints = []
    for i in range(a, b+1):
        sqrt = math.sqrt(i)
        if int(sqrt) == sqrt:
            if (sqrt)**2 == i:
                square_ints.append(i)
    return len(square_ints)

squares(3, 9)

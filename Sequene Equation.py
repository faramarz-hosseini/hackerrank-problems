def permutation_equation(p):
    result = []
    for x in range(1, len(p)+1):
        index = p.index(x) + 1
        answer = p.index(index) + 1
        result.append(answer)
    return result

permutation_equation([4, 3, 5, 1, 2])
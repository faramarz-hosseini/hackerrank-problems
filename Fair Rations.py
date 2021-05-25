def fairRations(B):
    res = 0

    for ind in range(len(B) - 1):
        if B[ind] % 2 == 1:
            B[ind] += 1
            B[ind + 1] += 1
            res += 2
    return str(res) if all(x % 2 == 0 for x in B) else 'NO'

print(fairRations([2,4,5,6]))

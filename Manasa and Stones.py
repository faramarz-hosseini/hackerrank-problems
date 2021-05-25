from itertools import combinations_with_replacement


def stones(n, a, b):
    scenarios = list(combinations_with_replacement([a, b], n))
    results = list()
    last_stone = 0
    for scenario in scenarios:
        for step in range(1, len(scenario)):
            last_stone += scenario[step]
        results.append(last_stone)
        last_stone = 0
    result = []
    boo = [result.append(num) for num in results if num not in result]
    return sorted(result)


print(stones(4, 10, 100))

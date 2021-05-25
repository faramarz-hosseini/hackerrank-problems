def circular_array_rotation(a, k, queries):
    result = []
    rotates = k % len(a)
    for _ in range(rotates):
        last_element = a[-1]
        a.pop()
        a.insert(0, last_element)
    for query in queries:
        result.append(a[query])
    return result

circular_array_rotation([1, 2, 3], 2, [0, 1, 2])

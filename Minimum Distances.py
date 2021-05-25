def minimum_distances(a):
    distances = []
    for element in a:
        if a.count(element) > 1:
            element_indices = [i for i, x in enumerate(a) if x == element]
            if len(element_indices) > 1:
                distance = element_indices[1] - element_indices[0]
                distances.append(distance)
    if distances:
        return min(distances)
    else:
        return -1

print(minimum_distances([7,1,3,4,1,7]))

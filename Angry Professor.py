def angry_professor(k, a):
    counter = 0
    for arrival in a:
        if arrival <= 0:
            counter += 1
    if counter >= k:
        return 'NO'
    return 'YES'

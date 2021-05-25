def cut_the_sticks(arr):
    result = [len(arr)]
    while True:
        arr = [x for x in arr if x != min(arr)]
        if len(arr) == 0:
            break
        result.append(len(arr))
    return result


print(cut_the_sticks([1, 13, 3, 8, 14, 9, 4, 4]))

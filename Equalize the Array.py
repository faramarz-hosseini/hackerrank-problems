def array_equalizer(arr):
    dic = dict()
    big_chad = 0
    deletions = 0
    for i in arr:
        if dic.get(i):
            dic[i] += 1
        else:
            dic[i] = 1
    for key, value in dic.items():
        if value > big_chad:
            big_chad = key
    for key, value in dic.items():
        if key != big_chad:
            deletions += value
    return deletions


print(array_equalizer([1,1,2,2]))

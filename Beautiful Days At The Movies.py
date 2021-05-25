def beautiful_days(i, j, k):
    happy_days = 0
    for i in range(i, j+1):
        lst = []
        for x in str(i):
            lst.append(x)
        lst.reverse()
        rev = int(''.join(lst))
        if abs(i - rev) % k == 0:
            happy_days += 1
    return happy_days

beautiful_days(20,23,6)
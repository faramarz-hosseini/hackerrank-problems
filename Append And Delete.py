def append_and_delete(s, t, k):
    if s[0] == t[0]:
        i = 0
        x = 1
        while s[i] == t[i] and i < (len(s) - 1) and i < (len(t) - 1):
            i += 1
            x += 1
        k -= (len(s) - x)
        k -= (len(t) - x)
        if k >= 0:
            return "Yes"
        else:
            return "No"
    else:
        k -= len(s)
        k -= len(t)
        if k >= 0:
            return "Yes"
        else:
            return "No"


print(append_and_delete('y', 'yu', 2))

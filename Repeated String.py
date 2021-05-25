def repeated_string(s, n):
    string_length = len(s)
    a_count = s.count('a')
    result = (n // string_length) * a_count
    if n % string_length == 0:
        return result
    else:
        for _ in range(n%string_length):
            if s[_] =='a':
                result += 1
        return result


print(repeated_string('a', 10))


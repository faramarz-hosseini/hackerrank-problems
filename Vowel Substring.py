def vowel_string(s, k):
    vowels = {'a', 'e', 'i', 'u', 'o'}
    ans = {}
    a = s[0:k]
    c = 0
    for char in a:
        if char in vowels:
            c += 1
    for i in range(len(s)):
        if s[i] in vowels:
            a = s[i:k+i]
            if a[-1] in vowels:
                pass
    max_ans = max(ans.values())
    for key in ans.keys():
        if ans[key] == max_ans:
            return key


print(vowel_string('azerdii', 5))

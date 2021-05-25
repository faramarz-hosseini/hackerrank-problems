
def happy_lady_bugs(b):
    # Write your code here
    if b.count('_') < 1:
        count = 0
        char = b[0]
        for chr in b:
            if count < 2 and char != chr:
                return "NO"
            if chr != char:
                count = 0
            count += 1

            char = chr
    for chr in b:
        if chr != "_" and b.count(chr) < 2:
            return "NO"
    return "YES"


happy_lady_bugs('RRGGBBXX')
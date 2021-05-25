def find_digits(n):
    divisors = 0
    for num in str(n):
        num = int(num)
        if num != 0 and n % num == 0:
            divisors += 1
    return divisors


print(find_digits(1012))

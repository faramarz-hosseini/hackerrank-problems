
def kaprekar_numbers(p, q):
    nums = []
    for i in range(p, q+1):
        length = 0
        for letter in str(i):
            length += 1
        sqr = str(i * i)
        if len(sqr) > 1:
            chars_num = len(sqr)
            right = ""
            left = ""
            for char in sqr:
                if chars_num > length:
                    left += char
                    chars_num -= 1
                else:
                    right += char
            if int(right) + int(left) == i:
                nums.append(i)
        elif int(sqr) == i:
            nums.append(i)
        else:
            continue
    if len(nums) >= 1:
        for num in nums:
            print(num, end=" ")
    else:
        print("INVALID RANGE")


kaprekar_numbers(297, 300)

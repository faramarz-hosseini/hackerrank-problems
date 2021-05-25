def picking_numbers(a):
    a.sort()
    current_num = a[0]
    next_num = current_num + 1
    result = []
    for i in a:
        if i == current_num or i == next_num:
            result.append(str(i))
        else:
            result.append('CHANGE')
            result.append(str(i))
            current_num = i
            next_num = current_num + 1
    index = 0
    counter = 0
    max_len = -1
    if "CHANGE" in result:
        while index < len(result):
            if result[index] == "CHANGE":
                max_len = max(max_len, counter)
                counter = 0
            else:
                counter += 1
            index += 1
    else:
        return len(result)
    return max_len


picking_numbers([2,2,2,2,2])

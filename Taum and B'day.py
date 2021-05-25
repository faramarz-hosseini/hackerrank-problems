def taum_bday(b, w, bc, wc, z):
    cheaper_color = min(bc, wc)
    other_color = max(bc, wc)
    cheaper_color_num = 0
    other_color_num = 0
    if cheaper_color == bc:
        cheaper_color_num = b
        other_color_num = w
    elif cheaper_color == wc:
        cheaper_color_num = w
        other_color_num = b

    if cheaper_color == other_color:
        return (cheaper_color_num + other_color_num) * other_color
    elif cheaper_color + z >= other_color:
        return cheaper_color_num * cheaper_color + other_color_num * other_color
    elif cheaper_color + z < other_color:
        convert_cost = (cheaper_color + z) * other_color_num
        return (cheaper_color_num * cheaper_color) + convert_cost


print(taum_bday(3, 6, 9, 1, 1))

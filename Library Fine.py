def library_fine(d1, m1, y1, d2, m2, y2):
    if y2 > y1:
        return 0
    if y2 >= y1 and m2 > m1:
        return 0
    if y2 >= y1 and m2 >= m1 and d2 > d1:
        return 0
    days = abs(d1-d2)
    months = abs(m1-m2)
    years = y1 - y2
    if years > 0:
        return 10000
    if months != 0:
        return months * 500
    return days * 15


print(library_fine(9,6,2015,6,6,2015))

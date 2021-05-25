def viral_advertising(n):
    current_audience = 5
    current_fans = current_audience // 2
    if n == 1:
        return current_fans
    for i in range(1, n):
        current_audience = current_audience // 2 * 3
        current_fans += current_audience // 2
    return current_fans

viral_advertising(5)
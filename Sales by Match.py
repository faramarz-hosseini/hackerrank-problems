def sockMerchant(n, ar):
    pairs = 0
    socks = {}
    for item in ar:
        if socks.get(item) is None:
            socks[item] = 1
        else:
            socks[item] += 1
    for socks_num in socks.values():
        pairs += socks_num // 2
    return pairs

def service_lane(n, cases):
    results = []
    for case in cases:
        widths = width[case[0]:case[1]+1]
        results.append(min(widths))
    return results

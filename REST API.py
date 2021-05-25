import requests


def rest_api(team, year):
    goals = 0
    url1 = f'https://jsonmock.hackerrank.com/api/football_matches'
    url2 = f'https://jsonmock.hackerrank.com/api/football_matches'
    params1 = {
        'team1': team,
        'year': year,
    }
    params2 = {
        'team2': team,
        'year': year,
    }
    r1 = requests.get(url=url1, params=params1)
    r2 = requests.get(url=url2, params=params2)
    data1 = r1.json()
    data2 = r2.json()
    for data_entry in data1['data']:
        goals += int(data_entry['team1goals'])
    for data_entry in data2['data']:
        goals += int(data_entry['team2goals'])
    return goals


print(rest_api('Barcelona', 2011))


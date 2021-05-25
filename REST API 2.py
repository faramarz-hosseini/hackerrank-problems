import requests


def rest_api(competition, year):
    goals = 0
    url1 = 'https://jsonmock.hackerrank.com/api/football_competitions'
    params1 = {
        'name': competition,
        'year': year
    }
    r1 = requests.get(url=url1, params=params1)
    data = r1.json()
    winner = data['data'][0]['winner']
    winner_url1 = 'https://jsonmock.hackerrank.com/api/football_matches'
    winner_url2 = 'https://jsonmock.hackerrank.com/api/football_matches'
    params2 = {
        'competition': competition,
        'year': year,
        'team1': winner,
    }
    params3 = {
        'competition': competition,
        'year': year,
        'team2': winner,
    }
    r2 = requests.get(url=winner_url1, params=params2)
    data2 = r2.json()['data']
    r3 = requests.get(url=winner_url2, params=params3)
    data3 = r3.json()['data']
    for data_entry in data2:
        goals += int(data_entry['team1goals'])
    for data_entry in data3:
        goals += int(data_entry['team2goals'])
    return goals


print(rest_api('English Premier League', 2014))

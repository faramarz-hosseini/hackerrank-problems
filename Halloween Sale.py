def how_many_games(p, d, m, s):
    games = 0
    game_price = p
    current_budget = s
    while current_budget > 0:
        current_budget -= game_price
        if game_price - d > m:
            game_price -= d
        else:
            game_price = m

        games += 1

    if current_budget < 0:
        games -= 1

    return games


print(how_many_games(89, 60, 27, 7777))

f = open('data.txt')

games = f.read().split('\n')


def return_score(game):
    num = int(game.split(':')[0].split('Game ')[1])
    draws = game.split(': ')[1].split('; ')
    print(draws)
    for draw in draws:
        individual_draw = draw.split(', ')
        scores = list(map(not_exceeding, individual_draw))
        if 0 in scores:
            return 0

    print('\n')
    return num


def not_exceeding(ind_draw, red_limit=12, green_limit=13, blue_limit=14):
    number = int(ind_draw.split(' ')[0])
    color = ind_draw.split(' ')[1]

    if color == "red" and number > red_limit:
        return 0
    if color == "green" and number > green_limit:
        return 0
    if color == "blue" and number > blue_limit:
        return 0
    return 1


print(sum(map(return_score, games)))

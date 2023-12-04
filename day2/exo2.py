f = open('data.txt')

games = f.read().split('\n')


def return_score(game):
    draws = game.split(': ')[1].split('; ')

    minimum_red, minimum_green, minimum_blue = 1, 1, 1
    for draw in draws:
        individual_draw = draw.split(', ')
        for color_draw in individual_draw:
            tuple_score = color_score(color_draw)
            color = tuple_score[0]
            score = tuple_score[1]

            if color == 'red':
                minimum_red = max(minimum_red, score)
            if color == 'green':
                minimum_green = max(minimum_green, score)
            if color == 'blue':
                minimum_blue = max(minimum_blue, score)

    return minimum_red * minimum_green * minimum_blue


def color_score(ind_draw):
    number = int(ind_draw.split(' ')[0])
    color = ind_draw.split(' ')[1]

    return (color, number)


print(sum(map(return_score, games)))

import numpy as np
import re

f = open('data.txt')

cards = []

for game in f.read().split('\n'):
    game_number = int(re.findall(r'\d+', game.split(': ')[0])[0])
    print(game_number)
    # print(cards.count(game_number))
    game = game.split(': ')[1]
    winning_numbers = game.split(' |')[0].split(' ')
    my_numbers = game.split('| ')[1].split(' ')

    # clean
    winning_numbers = [winning_number for winning_number in winning_numbers if winning_number != ""]
    my_numbers = [my_number for my_number in my_numbers if my_number != ""]

    common_numbers = np.intersect1d(winning_numbers, my_numbers)

    # print(common_numbers)

    cards_gained = []

    cards_gained += [game_number]

    cards_gained += [game_number+i for i in range(1, len(common_numbers)+1)] * (cards.count(game_number)+1)

    # print(cards_gained)
    # print()

    cards += cards_gained
    '''
    print(winning_numbers)
    print(my_numbers)
    print(common_numbers)
    print(point)
    print()
    '''

print(cards)
print(len(cards))

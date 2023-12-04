import numpy as np

f = open('data1.txt')

points = 0

for game in f.read().split('\n'):
    game = game.split(': ')[1]
    winning_numbers = game.split(' |')[0].split(' ')
    my_numbers = game.split('| ')[1].split(' ')

    # clean
    winning_numbers = [winning_number for winning_number in winning_numbers if winning_number != ""]
    my_numbers = [my_number for my_number in my_numbers if my_number != ""]

    common_numbers = np.intersect1d(winning_numbers, my_numbers)

    if len(common_numbers) == 0:
        point = 0
    else:
        point = 2**(len(common_numbers)-1)
    points += point
    '''
    print(winning_numbers)
    print(my_numbers)
    print(common_numbers)
    print(point)
    print()
    '''

print(points)
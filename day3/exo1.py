import re


class Grid:
    def __init__(self, file='data_test_exo1.txt'):
        self.file = file
        self.grid = None
        self.grid_size = None

        # setup
        self.get_grid()

    def get_grid(self):
        f = open(self.file)

        _ = f.read().split('\n')
        self.grid_size = len(_)
        self.grid = ''.join(_)

    def get_numbers(self):
        return re.findall(r'-?\d+', self.grid)

    def get_number_position(self, number):
        """" get index of each digit of the number """
        idx = self.grid.index(number)
        return [idx + i for i in range(len(number))]

    def get_adjacent_number_position(self, idx):
        """ get the idx of every possible adjacent idx """
        size = self.grid_size
        numbers = [idx-1, idx+1, idx-size-1, idx-size+1, idx+size-1, idx+size+1]

        # remove idx that are out of the grid; grid is a square
        return [number for number in numbers if 0 <= number < self.grid_size**2]

    def is_symbol(self, list_idx):
        """ return 1 if one of the idx in list_idx is a symbol """
        not_a_symbol = [str(i) for i in range(10)] + ['.']
        return max([1 if self.grid[idx] not in not_a_symbol else 0 for idx in list_idx])

    def is_a_part_number(self, number):
        """ determine if a number is a part number """
        idx = self.get_number_position(number)
        idx = map(self.get_adjacent_number_position, idx)
        # 2D list to 1D list
        idx = sum(idx, [])
        # remove duplicates and remove positions that are those of the nums
        idx = set(idx) - set(self.get_number_position(number))
        return self.is_symbol(idx)

    def resolve_problem(self):
        numbers = self.get_numbers()
        print(numbers)
        part_numbers = [int(number) for number in numbers if self.is_a_part_number(number)]
        print(part_numbers)
        return sum(part_numbers)


grid = Grid(file='data_test_custom.txt')
solution = grid.resolve_problem()

print(solution)

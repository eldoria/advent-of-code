f = open('data.txt')

words = f.read().split('\n')


def return_calibration(word):
    digits = [c for c in word if c.isdigit()]

    return int(digits[0] + digits[-1])


answer = sum(map(return_calibration, words))
print(answer)

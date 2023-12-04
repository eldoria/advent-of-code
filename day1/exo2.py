f = open('data.txt')

words = f.read().split('\n')

letters_to_digit = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}


def return_calibration(word, d=letters_to_digit):
    digits = []
    j = 0
    for i in range(len(word)):
        w1 = word[j:i+1]
        w2 = word[i]

        for number in d.keys():
            if number in w1:
                digits.append(d[number])
                j = i-1
        if w2.isdigit():
            digits.append(w2)

    return int(digits[0] + digits[-1])


answer = sum(map(return_calibration, words))
print(answer)

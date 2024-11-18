import yaml

# Part01

# 12 38 15 77 = 142
word = "1abc2 pqr3stu8vwx a1b2c3d4e5f treb7uchet"


def word_split(word):
    return word.split()


def find_first_and_last_digit(word_split):
    number = []
    for w in word_split:
        digit = [char for char in w if char.isdigit()]
        if digit:
            concat_digit = digit[0] + digit[-1]
            number.append(int(concat_digit))
    return number


def sum_first_and_last_digit(number):
    return sum(number)


def test_part_one(word):
    word = word_split(word)
    digit = find_first_and_last_digit(word)
    return sum_first_and_last_digit(digit)


def import_yml(file):
    with open(file, 'r') as file:
        input = yaml.safe_load(file)
    return input


def part_one(word):
    word = import_yml('input.yml')
    word = word_split(word)
    digit = find_first_and_last_digit(word)
    return sum_first_and_last_digit(digit)


print('test part01:', test_part_one(word))
print('part one:', part_one(word))

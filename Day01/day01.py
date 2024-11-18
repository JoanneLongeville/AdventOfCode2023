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


# Part02

# 29 83 13 24 42 14 76 = 281
word = (
    "two1nine eightwothree abcone2threexyz xtwone3four "
    "4nineeightseven2 zoneight234 7pqrstsixteen"
)
word_to_digit = {
    "one": "1", "two": "2", "three": "3", "four": "4", "five": "5",
    "six": "6", "seven": "7", "eight": "8", "nine": "9"
}


def transform_char_to_digit(word_split):
    def transform_word(word):
        result = ""
        i = 0
        while i < len(word):
            match_found = False
            for key in word_to_digit:
                if i + len(key) <= len(word) and word[i:i+len(key)] == key:
                    result += word_to_digit[key]
                    i += len(key)
                    match_found = True
                    break
            if not match_found:
                result += word[i]
                i += 1
        return result
    return [transform_word(word) for word in word_split]


def test_part_two(word):
    word = word_split(word)
    print(word)
    word_to_digit = transform_char_to_digit(word)
    print(word_to_digit)
    digit = find_first_and_last_digit(word_to_digit)
    return sum_first_and_last_digit(digit)


def part_two(word):
    word = import_yml('input.yml')
    word = word_split(word)
    word_to_digit = transform_char_to_digit(word)
    digit = find_first_and_last_digit(word_to_digit)
    return sum_first_and_last_digit(digit)


print('test part02:', test_part_two(word))
print('part two:', part_two(word))  # still not working (need 54591 but have 54623)

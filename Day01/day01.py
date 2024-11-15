#find numbers, add them and print the sum
import yaml

word = "1abc2 pqr3stu8vwx a1b2c3d4e5f treb7uchet"
word_split = word.split()
number = []
for w in word_split:
    digit = [char for char in w if char.isdigit()]
    if digit:
        concat_digit = digit[0] + digit[-1]
        number.append(int(concat_digit))
print('word', word)
print('word_split', word_split)
print('number', number)
print(sum(number))


with open('input.yml', 'r') as file:
    input = yaml.safe_load(file)
words = input
words_split = words.split()
numbers = []
current_numbers = ""
for w in words_split:
    digits = [char for char in w if char.isdigit()]
    if digits:
        concat_digits = digits[0] + digits[-1]
        numbers.append(int(concat_digits))
#print('words', words)
#print('words_split', words_split)
#print('numbers', numbers)
print(sum(numbers))
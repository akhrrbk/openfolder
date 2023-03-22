# this is a number extractor from a string
# built by github.com/akhrrbk with the help of chat gpt3

import re

def extract_numbers(s):
    pattern = r'\d+'
    numbers = re.findall(pattern, s)
    return ','.join(numbers)

s = "14100000 UZS"
numbers_str = extract_numbers(s)
print(numbers_str)
# print(type(numbers_str))
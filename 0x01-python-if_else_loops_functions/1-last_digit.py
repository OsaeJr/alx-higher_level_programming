#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

base = 'Last digit of'
last_number = abs(number) % 10 if number < 0 else number % 10

comparison_result = (
    f'{base} {number} is {last_number} and is greater than 5' if last_number > 5
    else f'{base} {number} is {last_number} and is 0' if last_number == 0
    else f'{base} {number} is {last_number} and is less than 6 and not 0'
)

print(comparison_result)

#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
ld = number % 10
strr = 'Last digit of {:d} is {:d}'
if ld > 5:
    print(strr.format(number, ld), "and is greater than 5")
elif ld == 0:
    print(strr.format(number, ld), "and is 0")
elif number < 0:
    ld = (-number) % 10
    ld = ld * -1
    print(strr.format(number, ld), "and is less than 6 and not 0")

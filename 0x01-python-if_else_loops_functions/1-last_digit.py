#!/usr/bin/python3
import random
number = random.randint(-10, 10)
Lastdigit = number % 10
if Lastdigit > 5:
    print(f"Last digit of {number:d} is {Lastdigit:d} and is greater 5")
elif Lastdigit == 0:
    print(f"Last digit of {number:d} is {Lastdigit:d} and is zero")
elif Lastdigit < 6 and != 0:
    print(f"Last digit of {number:d} is {Lastdigit:d} and is less than 6 and not 0")

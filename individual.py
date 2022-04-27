import random

a = int(input('a = '))
b = int(input('b = '))

print((a % b and not (b % a) and 1) or (b % a and not (a % b) and 1) or random.randint(0, 10))
from math import sqrt, floor, ceil as roof, pi
print(sqrt(2))
print(floor(9.8))
print(roof(3.14))

from math import *
print(sqrt(2))

import pprint

import random
print(dir(random))
print(random.random())
print(random.randint(0, 10))

n = random.randint(0, 10)
lottery = []
for i in range(7):
    n = random.randint(0, 10)
    lottery.append(n)
print(lottery)

def get_luck_numbers(n):
    import random
    lottery = []
    for i in range(n):
        n = random.randint(0, 10)
        lottery.append(n)
    return lottery
print(get_luck_numbers(7))




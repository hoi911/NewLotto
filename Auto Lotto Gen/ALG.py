from random import *

loop = 0
number = [0, 0, 0, 0, 0, 0]

while loop < 6:
    number[loop] = randint(0, 45)
    loop += 1

print(f"{number}")
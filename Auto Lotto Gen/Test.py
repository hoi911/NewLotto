from random import randint

number = [0, 0, 0, 0, 0, 0]
loop = 0

def isDuplicate(num):
    return num in number


for x in range(0, 6):
    x = randint(0, 45)
    while isDuplicate(x):
        x = randint(0, 45)
    number[loop] = x
    loop += 1

print(f"{number}")

a = 0
listA = []

while a <= 5:
    #listA[a] = randint(0, 45)
    listA.insert(a, randint(0,45))
    #print(f"listA[{a}]에 {listA[a]}를 대입합니다.")
    #print(f"listA[{a}] = randint(0, 45)")
    a += 1

print(f"{listA}")

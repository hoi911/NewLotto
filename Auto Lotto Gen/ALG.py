# 단순하게 0부터 45까지 무작위 숫자 출력
# 각 숫자들은 중복되지 않게 중복 필터 함수를 만들어서 검사

from random import *

loop = 0
number = [0, 0, 0, 0, 0, 0]

def DuplicationCheck(num):
    i, z = 0, 0
    while i < 6:
        while z < 6:
            if not z == i:
                check = 0
                check = num[i] - num[z]
                if check == 0:
                    return True
            z += 1
        i += 1
    return False


while True:
    loop = 0
    while loop < 6:
        number[loop] = randint(0, 45)
        loop += 1
    if DuplicationCheck(number):
        continue
    else:
        break

print(f"자동 번호는 {number} 입니다.")

# 반복문이 너무 많습니다. 아래 코드랑 비교해보면서 생각해보십시오.
loop = 0
number = [0, 0, 0, 0, 0, 0]

def isDuplicate(num):
    return num in number

while loop < 6:
    newNumber = randint(0, 45)
    while isDuplicate(newNumber):
        newNumber = randint(0, 45)
    number[loop] = newNumber
    loop += 1

print(f"자동 번호는 {number} 입니다.")
    

for x in number:
    x = randint(0, 45)
    while isDuplicate(x)
        x = randint(0, 45)
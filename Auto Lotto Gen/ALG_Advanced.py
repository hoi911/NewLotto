# 로또 번호를 기반으로 만든 가상 복권 서비스
# 사용자는 임의의 숫자를 입력하거나 무작위 숫자를 배정 받는다
# 무작위 당첨 숫자를 뽑아 최대 3 번 해당 숫자를 맞출 기회가 주어지며, 3 번을 넘어가면 당첨 숫자는 다시 무작위 숫자로 변한다
# 또한 중복 필터링으로 중복되는 숫자들을 배제했다

from random import *

loop = 0
number = [0, 0, 0, 0, 0, 0]
AINumber = [0, 0, 0, 0, 0, 0]
count = 0
countNum = 0

def DuplicationCheck(num):
    i, z = 0, 0
    while i < 6:
        while z < 6:
            if z != i:
                check = 0
                check = num[i] - num[z]
                if check == 0:
                    return True
            z += 1
        i += 1
        z = 0
    return False

def AILotto():
    AIList = [0, 0, 0, 0, 0, 0]
    loopFn = 0
    while loopFn < 6:
        AIList[loopFn] = randint(0, 45)
        loopFn += 1
    return AIList


def Correct(userList, AIList):
    if userList == AIList:
        print("축하합니다! 사용자의 번호와 이번 회차 행운의 번호는 일치합니다! 짝짝짝")
    else:
        print("아쉽네요... 사용자의 번호와 이번 회차 행운의 번호는 불일치합니다... 다음 기회에!")


while True:
    print("원하시는 서비스를 선택해주세요.\n자동 생성은 1번 수동 입력은 2번 당첨 결과 확인은 3번 종료는 4번")
    userSelection = int(input("번호를 입력해주세요: "))
    print("----------")

    if userSelection == 1:
        while True:
            loop = 0
            while loop < 6:
                number[loop] = randint(0, 45)
                loop += 1
            if DuplicationCheck(number):
                continue
            else:
                break

        print(f"생성된 번호는 {number}입니다")
        print("----------")

    elif userSelection == 2:
        while True:
            loop = 0
            print("0부터 45까지의 숫자를 6개 입력해주세요.")
            while loop < 6:
                number[loop] = int(input())
                if number[loop] > 45 or number[loop] < 0:
                    print("0과 45 사이의 숫자만 입력해주세요.")
                    continue
                loop += 1
            if DuplicationCheck(number):
                print("중복이 발생했습니다. 다시 입력해주세요.")
                print("----------")
                continue
            else:
                break
        print(f"입력하신 번호는 {number}입니다.")
        print("----------")

    elif userSelection == 3:
        if number == [0, 0, 0, 0, 0, 0]:
            print("입력된 값이 없습니다. 자동 혹은 수동으로 번호를 먼저 입력해주세요!")
        else:
            print("당첨 결과를 확인합니다!\n행운의 번호는 3회 마다 변경됩니다!")
            if count == 0 or not count % 3:
                while True:
                    AINumber = AILotto()
                    if DuplicationCheck(AINumber):
                        continue
                    else:
                        break
                countNum += 1
            print(f"{countNum} 회차 행운의 번호는! {AINumber} 입니다!")
            Correct(number, AINumber)
            count += 1
            print("----------")

    elif userSelection == 4:
        print("프로그램을 종료합니다.")
        break
    else:
        print("1부터 4의 숫자만 입력해주세요!")
        print("----------")
        continue
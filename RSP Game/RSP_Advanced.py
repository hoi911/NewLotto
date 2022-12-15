# 가위바위보와 묵찌빠 게임
# 플레이어는 일반 가위바위보 아니면 묵찌빠로 컴퓨터와 대결하게 된다
# 묵찌빠의 경우 플레이어가 공격권을 가지는 경우 Flag를 참으로 만들어 경기가 끝날 시 누구의 승리인가를 판단하게 끔 설계

from random import *

AI = ['주먹', '가위', '보']
AI2 = ['묵', '찌', '빠']
AINumber = 0
userFlag = bool

rspWinC = 0
rspLoseC = 0
rspDrawC = 0
rsp2WinC = 0
rsp2LoseC = 0

def RSP(AIList, ListNum):
    print("묵! 찌! 빠!\n어떤 걸 내시겠습니까?")
    user2 = input()

while True:
    print("가위바위보 게임입니다. 어떤 게임을 하실건가요?\n일반 가위바위보는 1번 묵찌빠는 2번 승점 조회는 3번 종료는 4번")
    userSelection = int(input())

    if userSelection == 1:
        print("가위바위보 게임을 시작합니다.\n'가위', '바위', '보'로만 입력해주세요!")
        user = input("무엇을 내실건가요?: ")

        while user != '바위' and user != '가위' and user != '보':
            print("정확하게 입력해주세요...")
            user = input("무엇을 내실건가요?: ")

        AINumber = randint(0, 2)

        print(f"컴퓨터는 {AI[AINumber]}을(를) 냈습니다!")

        if AI[AINumber] == user:
            print("무승부")
            rspDrawC += 1
        else:
            if AI[AINumber-2] == user:
                print("컴퓨터 승리!")
                rspLoseC += 1
            elif AI[AINumber-1] == user:
                print("플레이어 승리!")
                rspWinC += 1
        print("----------")

    elif userSelection == 2:
        print("묵찌빠 게임을 시작합니다.\n'가위', '바위', '보'로만 입력해주세요!")
        user = input("무엇을 내실건가요?: ")

        while user != '바위' and user != '가위' and user != '보':
            print("정확하게 입력해주세요...")
            user = input("무엇을 내실건가요?: ")

        while True:
            AINumber = randint(0, 2)

            print(f"컴퓨터는 {AI[AINumber]}을(를) 냈습니다!")

            if AI[AINumber] == user:
                print("무승부")
                print("다시 입력해주세요!")
                user = input("무엇을 내실건가요?: ")

                while user != '바위' and user != '가위' and user != '보':
                    print("정확하게 입력해주세요...")
                    user = input("무엇을 내실건가요?: ")
                continue

            else:
                if AI[AINumber - 2] == user:
                    print("컴퓨터가 선공합니다!")
                    print("----------")
                    userFlag = False
                    break
                elif AI[AINumber - 1] == user:
                    print("플레이어가 선공합니다!")
                    print("----------")
                    userFlag = True
                    break

        while True:
            print("묵! 찌! 빠!\n어느 걸 내시겠습니까?")
            user2 = input()
            while user2 != '묵' and user2 != '찌' and user2 != '빠':
                print("정확하게 입력해주세요...")
                user = input("무엇을 내실건가요?: ")
            AINumber = randint(0, 2)

            print(f"컴퓨터는 {AI2[AINumber]}를 냈습니다!")

            if AI2[AINumber] == user2:
                if userFlag:
                    print("플레이어 승리!")
                    print("----------")
                    rsp2WinC += 1
                    break
                else:
                    print("컴퓨터 승리!")
                    print("----------")
                    rsp2LoseC += 1
                    break
            else:
                if AI2[AINumber - 2] == user2:
                    print("컴퓨터가 공격합니다!")
                    print("----------")
                    userFlag = False
                elif AI2[AINumber - 1] == user2:
                    print("플레이어가 공격합니다!")
                    print("----------")
                    userFlag = True
        print("----------")

    elif userSelection == 3:
        print("현재 승점을 알려드립니다!")
        print(f"컴퓨터의 가위바위보 점수는 {rspWinC+rspLoseC+rspDrawC}전 {rspDrawC}무 {rspLoseC}승 {rspWinC}패")
        print(f"컴퓨터의 묵찌빠 점수는 {rsp2LoseC+rsp2WinC}전 {rsp2LoseC}승 {rsp2WinC}패")
        print("----------")
        print(f"플레이어의 가위바위보 점수는 {rspWinC + rspLoseC + rspDrawC}전 {rspDrawC}무 {rspWinC}승 {rspLoseC}패")
        print(f"플레이어의 묵찌빠 점수는 {rsp2LoseC + rsp2WinC}전 {rsp2WinC}승 {rsp2LoseC}패")
        print("----------")

    elif userSelection == 4:
        print("게임을 종료합니다.")
        break
    else:
        print("정확한 숫자를 입력해주세요!")
        print("----------")
        continue
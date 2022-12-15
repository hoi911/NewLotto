# 평범한 가위바위보 게임
# 리스트에 무작위 숫자를 대입해 컴퓨터의 손모양을 결정한다
# 플레이어와 컴퓨터의 손모양이 똑같다면 무승부
# 다를 시 리스트의 어떤 것과 일치하냐에 따라 승패 결정

from random import *

while True:
    AI = ['주먹', '가위', '보']
    print("가위바위보 게임을 시작합니다.\n'가위', '바위', '보'로만 입력해주세요!")
    user = input("무엇을 내실건가요?: ")

    while user != '바위' and user != '가위' and user != '보':
        print("정확하게 입력해주세요...")
        user = input("무엇을 내실건가요?: ")

    if user == 'exit':
        break

    AINumber = randint(0, 2)

    print(f"컴퓨터는 {AI[AINumber]}을(를) 냈습니다!")

    if AI[AINumber] == user:
        print("무승부")
    else:
        if AI[AINumber-2] == user:
            print("패배")
        elif AI[AINumber-1] == user:
            print("승리")
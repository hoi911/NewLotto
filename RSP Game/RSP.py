from random import *

allowedCommand = ['rock', 'scissors', 'paper', 'exit']

while True:
    AI = ['rock', 'scissors', 'paper']
    print("Enter your choice\nOnly 'rock', 'scissors', 'paper'")
    user = input("Make your decisions: ")

    while !(user in allowedCommand):
        print("Please Enter correct word!")
        user = input("Make your decisions: ")

    if user == 'exit':
        break

    AINumber = randint(0, 2)

    print(f"AI picks {AI[AINumber]}")

# 승패 로직 최적화 버전
# 파이썬의 리스트에서 마이너스로 가면 제일 마지막 숫자로 넘어가는 걸 발견 및 이용
# AI[0-2] == AI[1]
# 따라서 9가지의 경우의 수 모두를 따지지 않아도 된다.
# 단 리스트의 순서가 변경된다면 로직을 다시 고민해봐야 한다.
# 현재는 '바위', '가위', '보' 순서 (미국식)로 작성되어 있다.
# 가위 바위 보
    if AI[AINumber] == user:
        print("DRAW")
    else:
        if AI[AINumber-2] == user:
            print("LOSE")
        elif AI[AINumber-1] == user:
            print("WIN")
# 9가지 경우의 수 모두를 대입해보는 일반적인 승패 로직
# 코드가 쓸데없이 길어진다.
    if AINumber == 0:
        if user == 'rock':
            print("DRAW")
        elif user == 'scissors':
            print("LOSE")
        elif user == 'paper':
            print("WIN")
    elif AINumber == 1:
        if user == 'rock':
            print("WIN")
        elif user == 'scissors':
            print("DRAW")
        elif user == 'paper':
            print("LOSE")
    else:
        if user == 'rock':
            print("LOSE")
        elif user == 'scissors':
            print("WIN")
        elif user == 'paper':
            print("DRAW")

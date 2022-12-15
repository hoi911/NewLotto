# 사용자는 현재 연도를 기준으로 윤년인지 판단할 수 있게 된다.
# 음수를 사용해 현재를 기준으로 과거도 가능하다
# 사용자가 원하는 임의의 연도 또한 입력 가능하다

from datetime import date

def LeapYear(year):
    if not year % 4 and not year % 100:
        if not year % 400:
            print(f"{year}년은 윤년입니다.")
            print("----------")
        else:
            print(f"{year}년은 평년입니다.")
            print("----------")
    elif not year % 4:
        print(f"{year}년은 윤년입니다.")
        print("----------")
    else:
        print(f"{year}년은 평년입니다.")
        print("----------")

to = date.today()

while True:
    print("윤년 판별기입니다! 원하시는 서비스를 선택해주세요.\n현재 연도 기준은 1번 원하시는 연도 입력은 2번 종료는 3번")
    userSelection = int(input())

    if userSelection == 1:
        print(f"지금은 {to.year}년 입니다.")
        print("몇 년 뒤가 궁금하신가요? 금년이라면 0을 입력해주세요! 음수를 입력하면 과거도 가능합니다.")
        yearAdd = int(input())
        LeapYear(to.year+yearAdd)

    elif userSelection == 2:
        print("원하시는 연도를 입력해주세요!")
        userYear = int(input())
        LeapYear(userYear)

    elif userSelection == 3:
        print("프로그램을 종료합니다.")
        break

    else:
        print("올바른 숫자를 입력해주세요!")
        continue
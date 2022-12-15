# 특정 연도를 입력하게 되면 해당되는 값을 출력
# 4, 100, 400 모두로 나누어 떨어지면 윤년
# 4, 100 으로 나누어 떨어지면 평년
# 4 로 나누어 떨어지면 윤년
# 그외는 모두 평년

year = int(input("원하시는 연도를 입력해주세요: "))

if not year % 4 and not year % 100:
    if not year % 400:
        print("윤년입니다.")
    else:
        print("평년입니다.")
elif not year % 4:
    print("윤년입니다.")
else:
    print("평년입니다.")
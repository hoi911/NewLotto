# A는 전문 은행 털이범
# 첫 출력에서 1 <= N <= 300 000의 난수가 출력된다
# 이후 X T C가 N만큼 출력된다
# X는 좌표 값으로 0부터 N까지 증가한다
# T는 시간 값으로 0부터 N까지 증가한다
# C는 해당 은행을 털었을 경우 습득 가능한 돈의 액수
# A가 좌표 값을 1씩 진행할 경우 시간 값도 1씩 증가한다
# 좌표 X에 있는 은행이 T시간에 오픈하면 T시간에 A가 X로 도착할 경우에만 털 수 있다
# A는 전문적이라서 은행을 털 경우 시간이 소모되지 않는다
# A는 열려있는 은행을 지나치지 않으며 무조건 턴다
# X에 도착한 A는 은행이 열려있지 않은 경우 무조건 지나친다

from random import randint

numberOfBank = randint(1, 300000)
robbedMoney = 0

print(f"{numberOfBank}입니다")

for locationBank in range(1, numberOfBank+1):
	timeBank = randint(0, numberOfBank)
	moneyBank = randint(0, numberOfBank)
	print(f"{locationBank} {timeBank} {moneyBank}")
	if locationBank == timeBank:
		robbedMoney += moneyBank

print(f"총 획득한 금액은 {robbedMoney}원 입니다.")
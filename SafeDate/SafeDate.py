from random import randint

mon31 = [1, 3, 5, 7, 8, 10, 12]
mon30 = [4, 6, 9, 11]
mon28 = 2

def dayCalc(month, year):
	if month in mon31:
		# print("이곳") For Debug
		return 31
	elif month in mon30:
		# print("저곳") For Debug
		return 30
	elif month == mon28:
		if leapYear(year):
			# print("그곳") For Debug
			return 29
		else:
			# print("어느곳") For Debug
			return 28

def asiaCountry(presentDate, foodDate):
	if foodDate[1] == 0 or foodDate[2] == 0: return None
	if foodDate[1] > 12: return None
	elif foodDate[2] > dayCalc(foodDate[1], foodDate[0]): return None
	if sum(presentDate) <= sum(foodDate): return 1
	else: return 0

def mostCountry(presentDate, foodDate):
	if foodDate[1] == 0 or foodDate[0] == 0: return None
	if foodDate[1] > 12: return None
	elif foodDate[0] > dayCalc(foodDate[1], foodDate[2]): return None
	if sum(presentDate) <= sum(foodDate): return 1
	else: return 0

def restCountry(presentDate, foodDate):
	if foodDate[1] == 0 or foodDate[0] == 0: return None
	if foodDate[0] > 12: return None
	elif foodDate[1] > dayCalc(foodDate[0], foodDate[2]): return None
	if sum(presentDate) <= sum(foodDate): return 1
	else: return 0

def leapYear(year: int):
	if year % 4:
		# print("왜 여기임") For Debug
		return False
	else:
		# print("이건 왜 여기임") For Debug
		return True

def FoodDate():
	foodA = randint(0, 99)
	foodB = randint(0, 99)
	foodC = randint(0, 99)
	return foodA, foodB, foodC

def presentDate():
	presentYear = randint(0, 99)
	presentMonth = randint(1, 12)
	# presentMonth = 2 For Debug
	presentDay = randint(1, dayCalc(presentMonth, presentYear))

	"""if presentMonth in mon31:
		presentDay = randint(1, 31)
	elif presentMonth in mon30:
		presentDay = randint(1, 30)
	elif presentMonth == mon28:
		if leapYear(presentYear):
			presentDay = randint(1, 29)
			#print("Here")
		else:
			presentDay = randint(1, 28)
			print("Why")
	최적화 시켜서 일단 주석처리"""

	return presentYear, presentMonth, presentDay

def safeDateCheck(date: int, food: int):
	safe = [0 , 0, 0]
	safe[0] = asiaCountry(date, food)
	safe[1] = mostCountry(date, food)
	safe[2] = restCountry(date, food)

	if 0 in safe:
		return 0
	elif 1 in safe:
		return 1
	else:
		return None


numberOfFood = randint(1, 300000)
preDate = presentDate()
safeCount, unSafeCount, invalidCount = 0, 0, 0

print(f"오늘의 날짜는 {preDate[0]+2000}년 {preDate[1]}월 {preDate[2]}일 입니다.")
# print(dayCalc(preDate[1], preDate[0])) For Debug

for i in range(1, numberOfFood+1):
	foodDate = FoodDate()
	# print(foodDate) For Debug
	# safeDateCheck(preDate, foodDate) For Debug
	if safeDateCheck(preDate, foodDate) == 1:
		print(f"{foodDate[0]} {foodDate[1]} {foodDate[2]} safe")
		safeCount += 1
	elif safeDateCheck(preDate, foodDate) == 0:
		print(f"{foodDate[0]} {foodDate[1]} {foodDate[2]} unsafe")
		unSafeCount += 1
	else:
		print(f"{foodDate[0]} {foodDate[1]} {foodDate[2]} invalid")
		invalidCount += 1

print(f"총 음식의 갯수는 {numberOfFood}개 입니다.\nsafe: {safeCount} unsafe: {unSafeCount} invalid: {invalidCount}")
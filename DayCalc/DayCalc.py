mon31 = [1, 3, 5, 7, 8, 10, 12]
mon30 = [4, 6, 9, 11]
mon28 = 2

def calcDate(fromDate: str, toDate: str):
	loop = 1
	remainDay = 0

	fromMonth = int(fromDate[0])  # from month
	fromDay = int(fromDate[1])  # from day

	toMonth = int(toDate[0])  # to month
	toDay = int(toDate[1])  # to day

	if fromMonth == toMonth:
		return toDay - fromDay
	else:
		while fromMonth < toMonth:
			remainDay += getDayOfMonth(fromMonth)
			fromMonth += 1
		return remainDay - fromDay + toDay

def parseDate(date: str):
	results = date.split("/")
	print(results)
	if len(results) != 2:
		print("여기도 걸려용")
		return None
	return results

def getDayOfMonth(month: int) -> int:
	if month in mon31:
		return 31
	elif month in mon30:
		return 30
	elif month == mon28:
		return 28
	else:
		print("잘못된 입력입니다.")

def countDays(fromDate: str, toDate: str):
	parsedFromDate = parseDate(fromDate)
	parsedToDate = parseDate(toDate)
	if parsedFromDate == None or parsedToDate == None :
		print("여기 걸려용")
		return None

	return calcDate(parsedFromDate, parsedToDate)




userGetF = input("시작 날을 입력해주세요: ")
userGetT = input("끝나는 날을 입력해주세요: ")

print(countDays(userGetF, userGetT))
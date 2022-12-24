mon31 = [1, 3, 5, 7, 8, 10, 12]
mon30 = [4, 6, 9, 11]
mon28 = 2

def getDaysOfMonth(month: int) -> int:
    if month in mon31:
        return 31
    elif month in mon30:
        return 30
    elif month == mon28:
        return 28
    else:
        print("올바르지 않은 입력입니다.")


def countDays(f: str, t: str) -> int:
    if f[2] == '/':
        mon_fir = f[0] + f[1]
        if len(f) == 4:
            day_fir = f[3]
        elif len(f) == 5:
            day_fir = f[3] + f[4]
    else:
        mon_fir = f[0]
        if len(f) == 3:
            day_fir = f[2]
        elif len(f) == 4:
            day_fir = f[2] + f[3]

    if t[2] == '/':
        mon_sec = t[0] + t[1]
        if len(t) == 4:
            day_sec = t[3]
        elif len(t) == 5:
            day_sec = t[3] + t[4]
    else:
        mon_sec = t[0]
        if len(t) == 3:
            day_sec = t[2]
        elif len(t) == 4:
            day_sec = t[2] + t[3]

    mon_fir, day_fir, mon_sec, day_sec = int(mon_fir), int(day_fir), int(mon_sec), int(day_sec)

    if mon_fir == mon_sec:
#        print("1")
        return day_sec - day_fir
    else:
#        print("2")
        if mon_sec - mon_fir == 1:
#            print("3")
            return getDaysOfMonth(mon_fir) - day_fir + day_sec
        else:
#            print("4")
            loop = 1
            p, q = 0, mon_fir
            while loop < mon_sec - mon_fir:
                p += getDaysOfMonth(q)
                q += 1
                loop += 1
            p += getDaysOfMonth(q) - day_fir + day_sec
            return p

    return mon_fir, day_fir, mon_sec, day_sec

print("입력 예시: 12/25 12/26")
a = input("시작하는 날짜를 입력해주세요: ")
b = input("끝나는 날짜를 입력해주세요: ")

print(f"{countDays(a, b)}일")
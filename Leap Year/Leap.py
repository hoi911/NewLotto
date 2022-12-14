year = int(input("Enter a year: "))

if not year % 4 and not year % 100:
    if not year % 400:
        print("LEAP Year")
    else:
        print("just year")
elif not year % 4:
    print("LEAP YEAR")
else:
    print("just year")
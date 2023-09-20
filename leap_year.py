year = int(input("Enter the year you want to check(enter '0' if u want to quit): "))

run = True


if year==0:
    quit()
elif year % 4 == 0 & year % 100 == 0 & year % 400 == 0:
    print("its a leap year")
else:
    print("its not a leap year")
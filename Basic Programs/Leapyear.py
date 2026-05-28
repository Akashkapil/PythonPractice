x = int(input("Enter the year to check if its leap year or not : "))

if (x % 400 == 0) and (x % 100 == 0):
    print("{} year is leap year ".format(x))

elif (x % 4 == 0) and (x % 100 != 0):
    print("{} year is a leap year ".format(x))

else:
    print("{} not a leap year ".format(x))

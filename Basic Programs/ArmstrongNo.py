num = int(input("Enter the no : "))

sum = 0

# find the sum of the cube of each digit
temp = num
while temp > 0:
    digit = temp % 10
    print("digit : ", digit)
    sum += digit ** 3
    print("sum : ", sum)
    temp //= 10
    print("temp : ", temp)

if num == sum:
    print(num, "is a Armstrong")
else:
    print(num, "is not a armstrong number")


#below is code for reverse of a no
#
# num = 1234
# reversed_num = 0
#
# while num != 0:
#     digit = num % 10
#     reversed_num = reversed_num * 10 + digit
#     num //= 10
#
# print("Reversed Number: " + str(reversed_num))
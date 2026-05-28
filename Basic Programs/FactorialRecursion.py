def rec_fact(n):
    if n == 1:
        return n
    else:
        return n * rec_fact(n-1)


num = int(input("Enter the no of which you need to calculate the factorial of : "))

if num < 0:
    print("Enter a valid no")

elif num == 0:
    print("The Factorial of the no is 1")

else:
    print("The factorial of the no : ", num, " is : ", rec_fact(num))


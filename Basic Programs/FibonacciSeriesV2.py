x = int(input("Enter the no of terms you want to print : "))

a, b = 0, 1
count = 0

if x <= 0:
    print("Enter a valid no")

elif x == 1:
    print("The values are : ", x)

else:
    print("The fibonacci series is : ")
    while count < x:
        print(a)
        last = a + b
        a = b
        b = last
        count += 1

x = int(input("Enter the 1st no: "))
y = int(input("Enter the 2nd no: "))

if x > y:
    smaller = y
else:
    smaller = x

HCF = 0

for i in range(1, smaller+1):
    if(x % i == 0 ) and (y % i == 0 ):
        HCF = i

# return HCF

print("The HCF is : ", HCF)

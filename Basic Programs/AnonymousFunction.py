
n = int(input("Enter the no of terms : "))

result = list(map(lambda x : 2 ** x, range(n)))

print("Total no of terms are : ", n)

for i in range(n):
    print("2 raised to the power of ", i, "is", result[i])

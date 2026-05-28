x = input("Enter the first no : ")
y = input("Enter the second no : ")

try:
    z = int(x)/int(y)

# except Exception as e: (This can also be used)

except ZeroDivisionError as e:
    print("Exception occurred: ", e)
    z = 'none'

# to find the type of exception you are getting we can use this
# except Exception as e:
#     print("Exception type is : ", type(e).__name__)
# here __name__ is the entry point of a program in python just as a main() method is in a java program

print("Division is : ", z)

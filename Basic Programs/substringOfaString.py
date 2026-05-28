fullstring = "StackAbuse"
substring = "tack"

# or we can use this also both if condition is true
# if fullstring.find(substring) == True:
if fullstring.find(substring) != -1:
    print("Found!")
else:
    print("Not found!")


# OR We can do it like this also

from re import search

fullstring2 = "StackAbuse"
substring = "tack"

if search(substring, fullstring2):
    print ("Found!")
else:
    print ("Not found!")
#  THIS WILL CONTAIN THE OPERATIONS WHICH ARE A BIT COMPLEX TO UNDERSATND REGARDING STRINGS

# String slicing
s = "ABCDEF"
print(s[1:4])    
print(s[:3])     
print(s[3:])    
print(s[:])
print(s[:-1])
print(s[::-1])  # Here it will select all the elements from start : Last and then reverse it by using '-1' ---> (start : end : start from last)


# Looping through string
s = "ABCDEF"
for char in s:
    print(char)

# String are immutable (if we perform an operation on them then a new string is created, the original string is untouched)
s = "aBCDEF"
s = "A" + s[1:]
print(s)

s = "aBCDEF"
s = "A" + s[:]
print(s)

s = "aBCDEF"
s = "A" + s
print(s)

s = "aBCDEF"
s = "A" + s[:2]
print(s)

s = "aBCDEF"
s = "A" + s[2:]
print(s)

s = "aBCDEF"
s = "A" + s[3]
print(s)

# check the above program condition to undersand how the operation is performed on a string

# Deleting a string
s = "aBCDEF"
del s # (NOTE : if we try to call the 's' now the python will raise an 'NameError' since the variable no longer exists in the memory)

# Updating the string
s = "ABCD EF"
s1 = "H" + s[1:]                  
s2 = s.replace("ABC", "abc")  

print(s1)
print(s2)

# Common string methods

#  to find length of a string
s = "GeeksforGeeks"
print(len(s))

# to change the CASE of a string
s = "Hello World"
print(s.upper())
print(s.lower())

# strip() - This replaces all the leading and trailing white spaces from the string
# replace() - This replaces all occurances of a specific substring with another

s = "   ABC   "
print(s.strip())    

s = "Python is fun"
print(s.replace("fun", "awesome"))

# concatinating strings with '+' operator
s1 = "Hello"
s2 = "World"
print(s1 + " " + s2)

#  repeating a string using '*' operator
s = "Hello "
print(s * 3)

# Formatting string using f'string - this allows to directly insert variables and expressions in a string
name = "Jake"
age = 22
print(f"Name: {name}, Age: {age}")

# using format() method, this allows to insert the values in the variables present in the string
s = "My name is {} and I am {} years old.".format( "Emily", 22)
print(s)

# String membership testing
# 'in' keyword is used to check whether a substring exists in the string or not. This will return a boolean value
s = "GeeksforGeeks"
print("Geeks" in s)
print("GfG" in s)

# String comparison in python 
s1 = "apple"
s2 = "banana"

print(s1 == s2)
print(s1 != s2)
print(s1 < s2)

#  '==' operator for equality check
s1 = "Python"
s2 = "Python"

print(s1 == s2)

# '!=' operator for inequality check
s1 = "Python"
s2 = "Java"

print(s1 != s2)

# Lexicographical Comparison
# Lexicographical comparison checks if one string appears before or after another in alphabetical order. This is especially useful for sorting.

s1 = "apple"
s2 = "banana"

print(s1 < s2)
print(s2 > s1)


# Case-Insensitive Comparison
# Strings in Python can be compared case-insensitively by converting both strings to either lowercase or uppercase.
s1 = "Apple"
s2 = "apple"

print(s1.lower() == s2.lower())

# Using startswith() and endswith() Methods
# The startswith() and endswith() methods in Python are used to check if a string begins or ends with a specific substring.

s = "hello world"

print(s.startswith("hello"))
print(s.endswith("world"))

# To convert a string in to list using .split() method
s = "Geeks for Geeks"

a = s.split()
print(a)

# using list() method
s = "Geeks for Geeks"

a = list(s)
print(a)

# Using list comprehension 
s = "Geeks for Geeks"
a = [ch for ch in s]
print(a)
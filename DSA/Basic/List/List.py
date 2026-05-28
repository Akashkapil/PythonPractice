# THIS FILE HAVE BASIC LIST PROGRAMS HAVING ALL THE OPERATIONS WE CAN DO WITH A LIST

#  Type 1 : Directly initilaizing the list
a = [1,2,3]
print(a)

b = ['apple', 'banana']
print(b)

#  Type 2 : using 'list()' constructor

a = list((1, 2, 3, 'apple', 'mango', 10.8))
print(a)

b = list('akash') # or can be used b = list(('akash')) will give same answer
print(b)


c = list(('akash',))
print(c)

# creating list with repeated elements
d = [2]*5
print(d)

e = ['akash']*3
print(e)

f = ['z']*5
print(f)

# printing and accessing using index
g = [1,23,5,2,6,8]
print(g[3]) #index number 3
print(g[-1]) #index of last number in the list
print(g[:2]) #this means till index 2 but not including index 2 itself
print(g[2:5]) #this means the values will start with index 2 and will go till index 5 but the value at index 5 will not be included


# adding elements to the list using append() method
a = [1,2]
a.append(3) # this will append/add the element to the last of the List
print(a)

# addng elements using insert() method
a = [11,12,13,14,15]
a.insert(2,3) # insert(index, element : int)
print(a)

# adding multiple elements at the end of the list using extend() method
# append() can only add 1 element, extend() can add multiple elements but both of them add the elements at the end of the list
a = [1, 2, 3, 4, 5]
a.extend([6,7])
print(a)

# updating the elements in the list
a = [1, 2, 3, 4, 5]
a[2] = 25
print(a)

# removing elements from the list using remove() method
a = [1, 2, 3, 4, 5, 2]
a.remove(2) #removes the first occurance of the element
print(a)

# removing elements from the list using pop()
# pop() method removes the element from the specified index or from the last if no index is specified
a = [1, 2, 3, 4, 5]
a.pop() # removed element from the last of the list
a.pop(1) #removed element from the index 1
print(a)

# we can also get the element which we have popped from the list using pop()
a = [1, 2, 3, 4, 5]
element = a.pop(2)
print(element)


# removing elements using del
a = [1, 2, 3, 4, 5]
del a[2]
print(a)

# The difference between pop() and del is that when we pop() an element we can get its value and use it where as in del we simply delete the element

# clearing all the elements in a list using clear()
a = [1, 2, 3, 4, 5]
a.clear()
print(a) # This will give us a empty list

# Iterating over a list
a = ['apple', 'banana', 'cherry']
for i in a:     # In this case we simple iterated over the values present in the list 'a'.
    print(i)

a = ['apple', 'banana', 'cherry']
for i in range(len(a)):     # In this case we iterated over the reange of values present in the list 'a'. Here range will be of 0 to 2 index so total 3.
    print(a[i])             # Here 'i' contains the range of number equalling to the length of list 'a'.

# nested list

a = [[1,2],[3,4]]
print(a[0])
print(a[1][0])

# this list can be imagined as a = [(0,0) (0,1)]
                                #  [(1,0) (1,1)]
# so here we have requested for index no a[1][0] which is = 3

a[1].insert(0,2)
print(a)
a[0].insert(1,4)
print(a)

a.insert(0,9)
print(a)
a.insert(2,[0,1])
print(a)

# to find the index of an element present in the list
a = [1, 2, 3, 4, 5]
ind = a.index(2) # This will give error if the element is not present in the list.
print(ind) 


# concatinating 2 list into 2 lists
first = [1,2,3]
second = [4,5,6]
final_l = first + second
print(final_l)


f = open("C://Users//AKASH//Desktop//book.txt","r")
s = f.read()
print(s)

import json
book = json.loads(s)
print(book)
print(type(book))

print(book['Tom'])

for p in book:
    print(book[p])
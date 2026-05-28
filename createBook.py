book = {}
book['Tom'] = {
    'name':'Tom',
    'address':'85jsdfnasd',
    'phone':'12123123'
}
book['bob'] = {
    'name':'bob',
    'address':'23sadpoksfdv',
    'phone':'6435634573'
}

import json
j = json.dumps(book)
print(j)

with open("C://Users//AKASH//Desktop//book.txt","w") as o:
    o.write(j)
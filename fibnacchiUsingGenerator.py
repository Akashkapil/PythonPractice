def fib():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a+b


# for loop internally uses generators to iterate over anything
for f in fib():
    if f > 50:
        break
    print(f)

# generators are better than class based iterators
# 1. You don't need to define __iter__ and __next__ methods
# 2. You don't need to raise a StopIteration exception

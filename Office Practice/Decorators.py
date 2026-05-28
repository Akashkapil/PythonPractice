# defining a decorator
def python_decorator(func):
   def wrapper():
      print("Text before calling the function")
      func()
      print("Text after calling the function")
   return wrapper

@python_decorator
def tutorials_decorator():
   print("Hello tutorials Point!!!")

tutorials_decorator()
class Accident(Exception):
    def __init__(self, message):
        self.message = message

    def print_exception(self):
        print("user defined exception : ", self.message)


try:
    # we use raise keyword when we want to throw an exception to user
    raise Accident('Accident occurred between two cars')


except Accident as e:
    e.print_exception()

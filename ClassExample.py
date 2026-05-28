class Human:
    # here the __init__ function have the same purpose as a constructor in java and self keyword is the class itself
    # it is present in all the methods by default
    def __init__(self,name, occ):
        self.name = name
        self.occupation = occ

    def do_work(self):
        if self.occupation == "tennis player":
            print(self.name, "plays tennis")
        elif self.occupation == "actor":
            print(self.name, "shoots a film")

    def speaks(self):
        print(self.name, "says how are you?")

tom = Human("Tom curze","actor")
tom.do_work()
tom.speaks()

maria = Human("maria sharpova", "tennis player")
maria.do_work()
maria.speaks()
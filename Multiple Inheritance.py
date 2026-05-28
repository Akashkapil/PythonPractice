class Father():
    def guardening(self):
        print("Enjoy guardening")


class Mother():
    def cooking(self):
        print("Enjoy cooking")


class Child(Father, Mother):
    def play(self):
        print("Enjoy playing")


c = Child()
c.guardening()
c.cooking()
c.play()

class Hello:
    def __init__(self,name):
        self.name = name

    def prog(self):
        print("Hello %s!" %(self.name))

name1 = Hello("World")

name1.prog()


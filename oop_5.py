class Computer:

    def __init__(self):
        self.name = 'Irshad'
        self.age = 19

    def update(self):
        self.age = 30
    def compare(self,other):
        if self.age == other.age:
            return True
        else:
            return False

c1 = Computer()
c1.age = 20
c2 = Computer()

#c1.age = 20
if c1.compare(c2):
    print("They are same")
else:
    print("They are different")




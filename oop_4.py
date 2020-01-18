class Computer:

    def __init__(self):
        self.name = 'Irshad'
        self.age = 19

    def update(self):
        self.age = 30

c1 = Computer()
c2 = Computer()

c1.name = 'Imran'
c1.age = 25

c1.update()

print(c1.name)
print(c2.name)
print(c1.age)
print(c2.age)

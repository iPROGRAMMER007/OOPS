class Car:

    wheels  = 4

    def __init__(self):
        self.mil = 10
        self.com = 'BMW'

c1 = Car()
c2 = Car()

c1.mil = 12

Car.wheels = 5

print(c1.mil,c1.com,Car.wheels)
print(c2.mil,c2.com,Car.wheels)











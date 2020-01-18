class Student:

    def __init__(self,name,rollno):
        self.name = name
        self.rollno = rollno
        self.lap = self.Laptop()

    def show(self):
        print(self.name,self.rollno)

    class Laptop:

        def __init__(self):
            self.brand = 'HP'
            self.cpu = 'i5'
            self.ram = 8


s1 = Student("Irshad",10)
s2 = Student('Vikash',20)

print(s1.name,s1.rollno)

s1.show()
s2.show()

lap1 = s1.lap

print(s1.lap.brand)

print(lap1.ram)
print(lap1.cpu)
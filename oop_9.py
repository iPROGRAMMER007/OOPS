class Student:

    def __init__(self,name,rollno):
        self.name = name
        self.rollno = rollno
        self.lap = self.Laptop()


    def show(self):
        print(self.name,self.rollno)
        self.lap.show()

    class Laptop:

        def __init__(self):
            self.brand = 'ASUS'
            self.cpu = 'i7'
            self.ram = 8

        def show(self):
            print(self.brand,self.cpu,self.ram)


s1 = Student("Irshad",10)
s2 = Student('Vikash',20)

print(s1.name,s1.rollno)

s1.show()
s2.show()

#lap1 = Student.Laptop()
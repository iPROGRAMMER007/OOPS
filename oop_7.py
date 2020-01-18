class Student:

    school  = "ISchool"

    def __init__(self,m1,m2,m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def avg(self):
        return (self.m1 + self.m2 + self.m3)/3

    @classmethod
    def getSchool(cls):
        return cls.school

    @staticmethod
    def info():

        print("This is static method ... of abc module")
s1 = Student(56,78,90)
s2 = Student(45,23,89)
print(Student.avg(s1))
print(s2.avg())
print(Student.getSchool())

Student.info()

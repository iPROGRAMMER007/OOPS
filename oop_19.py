class A:
    def show(self):
        print("in A Show")

class B(A):

    def show(self):
        print("in B Show")

   # pass

a1 = B()

a1.show()

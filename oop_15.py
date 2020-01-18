class Pycharm:

    def execute(self):
        print("Compiling")
        print("Running")

class MyEditor:
    def execute(self):
        print("Spell check")
        print("Convention check")
        print("Compiling")
        print("Running")

class Laptop:
    def code(self,ide):
        print("hi")
        ide.execute()


ide = MyEditor()

lap1 = Laptop()

lap1.code(ide)







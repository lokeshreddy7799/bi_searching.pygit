class Main():

    def _init_(self):
        print("It's and _init_ of superclass(Main)")

    def demo(self):
        print("class1 of method1")

    def demo1(self):
        print("class1 of method2")

class Subclass(Main):

    def demo2(self):
        print("class2 of method1")

    def demo3(self):
        print("class2 of method2")

s1 = Subclass()

s1.demo()
s1.demo1()
s1.demo2()
s1.demo3()




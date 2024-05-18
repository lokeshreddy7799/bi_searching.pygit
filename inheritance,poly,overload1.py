class A:
    def add(self,*args):
        if args:
            sum = type(args[0])()
            for i in args:
                sum+=i
            return sum
obj=A()
print(obj.add(1,2))
print(obj.add(1,3,4,6,))
print(obj.add("loki","reddy"))
print(obj.add([1,2,3],[4,5,6,]))



class A:
    def fun(self):
        print("this is class A")
class B:
    def fun(self):
        print("this is class B")

class C:
    def fun(self):
        print("this is class C")
def poly(obj):
    obj.fun()

obj1 = A()
obj2 = B()
obj3 = C()

poly(obj1)
poly(obj2)
poly(obj3)



















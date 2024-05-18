def display(name, age, salary):
    print("name :" , name)
    print("age : " , age)
    print("salary : ", salary)
n="loki"
a=25
s=20000
display(salary=s,age=a,name=n)


def update(x):
    x=8
    print(x)
update(10)


def update(x):
    x=8
    print("x",x)

a = 10
update(a)
print("a",a)




def update(lst):
    print(id(lst))
    lst[1]=25
    print(id(lst))
    print("lst",lst)
lst=[20,30,40]
print(id(lst))
update(lst)
print("lst",lst)

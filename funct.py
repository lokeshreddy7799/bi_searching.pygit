def greet():
    print("hello")
    print("good")

greet()

def greet():
    print("hello")
    print("good")
def add(x,y):
    c = x+y
    print(c)
greet()
result = add(5,7)




def add_sub(x,y):
    c = x+y
    d = x-y
    return c,d
result1,result2 = add_sub(5,7)
print(result1,result2)




def add_numbers(a, b):
    return a + b
result = add_numbers(3, 5)
print("Result:", result)



def sum_all(*args):
    total = 0
    for num in args:
        total += num
    return total

print(sum_all(1, 2, 3))
print(sum_all(5, 10, 15))

def total(a,b):
    result=(a+b)
    print('sum of', a, 'and', b ,'=' , result)
a = int(input('enter the frist number :'))
b = int(input('enter the  second number : '))
total(a,b)











#
# import sys
# sys.setrecursionlimit(1000)
# print(sys.getrecursionlimit())
# def greet():
#     print("hello")
#     greet()
# greet()




import sys
sys.setrecursionlimit(1000)
print(sys.getrecursionlimit())
i=0
def greet():
    global i
    i+=1
    print("hello",i)

greet()



def count_down(n):
    if n == 0:
        print("Liftoff!")
    else:
        print(n)
        count_down(n - 1)
count_down (20)



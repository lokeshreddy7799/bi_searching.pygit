from numpy import *

arr = array([1,3,5,7,9,])
arr = arr+7
print(arr)


arr1= array([1,3,5,7,9,])
arr2= array([4,5,6,7,9,])
arr3 = arr1+arr2                   
print(arr3)


arr= array([1,3,5,7,9,])
print(log(arr))

arr= array([1,3,5,7,9,])
print(sin(arr))


arr1= array([1,3,5,7,9,])
arr2= array([4,5,6,7,9,])

print(concatenate([arr1,arr2]))



arr1 = array([2,4,6,7,9,])
arr2 = arr1
print(arr1)
print(arr2)


arr1 = array([2,4,6,7,9,])
arr2 = arr1.view()                  
print(arr1)
print(arr2)
print(id(arr1))
print(id(arr2))


arr1 = array([2,4,6,7,9,])
arr2 = arr1.view()
arr[1] = 7                           
print(arr1)
print(arr2)
print(id(arr1))
print(id(arr2))


arr1 = array([2,4,6,7,9,])
arr2 = arr1.copy()
arr[1] = 7                           
print(arr1)
print(arr2)
print(id(arr1))
print(id(arr2))





















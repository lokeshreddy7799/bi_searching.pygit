from numpy import *

arr1 = array ([[1,2,3,],[4,5,6,]])
print(arr1)

arr1 = array ([[1,2,3,],[4,5,6,]])
print(arr1.size)

arr1 = array ([[1,2,3,],[4,5,6,]])
print(arr1.ndim)


arr1 = array ([[1,2,3,],[4,5,6,]])
print(arr1.shape)


arr1 = array ([[1,2,3,],[4,5,6,]])
arr2 = arr1.flatten()
print(arr2)



arr1 = array ([[1,2,3,8,9,3],[4,5,6,1,2,6]])
arr2 = arr1.flatten()
arr3 = arr2.reshape(2,2,3)
print(arr3)


m = matrix('1 2 3 4 ;5 6 7 8')
print(m)


m = matrix('1 2 ;3 4 ;5 6; 7 8')
print(m)

m = matrix('1 2 3 4 ;5 6 7 8')
print(diagonal(m))

m = matrix('1 2 3 4 ;5 6 7 8')
print(m.min())


m = matrix('1 2 3 4 ;5 6 7 8')
print(m.max())

m1 = matrix('2 3 4 5;6 7 8 9')
m2 = matrix('9 8 7 6 ;5 4 3 2')
m3 = m1+m2;
print(m3)
















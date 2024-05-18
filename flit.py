from functools import reduce
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)


squared_numbers = list(map(lambda x: x ** 2, numbers))
print(squared_numbers)

sum_of_numbers = reduce(lambda x, y: x + y, numbers)
print(sum_of_numbers)




numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

filtered_numbers = list(filter(lambda x: x > 5, numbers))
print("Numbers greater than 5:", filtered_numbers)

binary_numbers = list(map(lambda x: bin(x), numbers))
print(binary_numbers)



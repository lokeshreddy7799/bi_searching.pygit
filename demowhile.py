count = 5

while count > 0:
    print(count)
    count -= 1

print("Blast off!")


total = 0
number = 1

while number <= 10:
    total += number
    number += 1

print("The sum of numbers from 1 to 10 is:", total)


password = input("Enter your password: ")

while password != "secret":
    print("Incorrect password. Try again.")
    password = input("Enter your password: ")

print("Access granted!")
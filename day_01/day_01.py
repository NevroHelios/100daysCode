#Its day 1

# 1.Write a program to print "Hello, World!" to the console.
print('hello world')

# 2.Calculate the sum of two numbers entered by the user.
print(float(input()) + float(input()))

# 3.Swap the values of two variables without using a temporary variable.
a = 'hello'
b = 'world'
a, b = b, a
print(a, b)

# 4.Write a program to check if a number is even or odd.
num = int(input("Enter a number:"))
if num % 2 == 0:
    print(f"{num} is Even")
else:
    print(f"{num} is Odd")

# 5.Implement a simple calculator that can perform addition, subtraction, multiplication, and division based on user input.
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Cannot divide by zero!"
    return x / y

print("Select operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

while True:
    choice = input("Enter choice (1/2/3/4): ")

    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print("Result:", add(num1, num2))
        elif choice == '2':
            print("Result:", subtract(num1, num2))
        elif choice == '3':
            print("Result:", multiply(num1, num2))
        elif choice == '4':
            print("Result:", divide(num1, num2))
        break
    else:
        print("Invalid input. Please enter a valid number.")

# 6.Create a program that prints all prime numbers between 1 and 100.
from math import sqrt

prime_numbers = []

for num in range(2, 101): 
    flag = True
    for j in range(2, int(sqrt(num)) + 1):
        if num % j == 0:
            flag = False
            break
    if flag:
        prime_numbers.append(num)

print(prime_numbers)
## Create a simple Python program that asks the user to input two numbers and a mathematical operation (addition, subtraction, multiplication, or division).
## Perform the operation based on the user's input and print the result.
## Example: If a user inputs 10, 5, and +, your program should display 10 + 5 = 15.

print("------- Simple Calculator -------")
num1 = int(input("Type in the first number. "))
operator = (input("The operator symbol that you'd like to use i.e x,+,-,/ "))
num2 = int(input("Type in the second number. "))

if operator == 'x':
    print(f"{num1} multiplied to {num2} equals {num1 * num2}")
elif operator == '+':
    print(f"{num1} added to {num2} equals {num1 + num2}")
elif operator == '-':
    print(f"{num2} subtracted from {num1} equals {num1 - num2}")
elif operator == '/':
    print(f"{num1} divided by {num2} equals {num1 / num2}")
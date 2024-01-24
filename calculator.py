#Define four subroutines - add, subtract, multiply, divide that add multiply etc two numbers and return the result. Each should have two integer number arguments.


def add():
  num1 = int(input("Enter a number to add.\n"))
  num2 = int(input("Enter another number to add.\n"))
  sum = num1 + num2
  print("The sum is:")
  print(sum)

def subtract():
  num1 = int(input("Enter a number for subtraction.\n"))
  num2 = int(input("Enter another number to subtract from the first number.\n"))
  diff = num1 - num2
  print("The difference is:")
  print(diff)

def multiply():
  num1 = int(input("Enter a number to multiply.\n"))
  num2 = int(input("Enter another number to multiply.\n"))
  product = num1 * num2
  print("The product is:")
  print(product)

def divide():
  num1 = int(input("Enter a number for division.\n"))
  num2 = int(input("Enter another number to divide the first number by.\n"))
  quotient = num1 / num2
  print("The quotient is:")
  print(quotient)

operand = int(input("Enter 1 for addition, 2 for subtraction, 3 for multiplication or 4 for division.\n\n"))
if operand == 1:
  add()

elif operand == 2:
  subtract()

elif operand == 3:
  multiply()

elif operand == 4:
  divide()

#The user is asked to input two numbers.  These numbers will be passed as arguments into one of the subroutines.
#The user is asked to input 1 to add, 2 to subtract etc.
#If they input 1, call the ‘add’ subroutine, input 2 calls the ‘subtract’ subroutine etc
#Output the returned result as part of a sentence.

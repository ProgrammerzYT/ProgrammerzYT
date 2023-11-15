import math

Operator = input("Enter a operator >> ")
num1 = int(input("Enter 1st number >> "))
num2 = int(input("Enter 2nd number >> "))

#Rules

if Operator == '+':
    result1 = num1 + num2
    print("The addition is", result1)
elif Operator == '-':
    result2 = num1 - num2
    print("The subtraction is", result2)
elif Operator == '*':
    result3 = num1 * num2
    print("The multiplication is", result3)
elif Operator == '/':
    result4 = num1 / num2
    print("The Division is", result4)

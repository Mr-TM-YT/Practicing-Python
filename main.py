
# Start of Basic Calculator

num1 = int(input("Enter your first numers: "))
operator = input("Enter the operator: ")
num2 = int(input("Enter your second number: "))


if operator == '+':
    print(num1 + num2)
elif operator == '-':
    if (num1 - num2)  >= 0:
        print(num1 - num2)
    else:
        print("It's a negative value")
elif operator == '÷' or operator == '/':
    if num1 == 0:
        print("Math error (No deviding by 0)")
    else:
        print(num1 / num2)
elif operator == '*' or operator == 'x':
    print(num1 * num2)
else:
    print("You maybe did undefined operator or nonsense number")


# End of Basic Calculator

"""
  Ahmed have to print From Ahmed
  Then we will talk

"""

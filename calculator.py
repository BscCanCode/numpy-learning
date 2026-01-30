import numpy as np

def calculator():
    try:
        a = int(input("Enter the number: "))
        b = int(input("Enter the another number: "))

    except ValueError:
        print("Invalid input, enter the proper values and try again!")
        return None, None
    
    return a, b

print("This is the calculator program!")

while True:
    user_input = input("Enter the operation you want to perform\n1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n5.Exit\nYour input: ").lower()

    if user_input == "addition":
        a, b = calculator()
        if a is None:
            continue
        print(f"The addition of {a} + {b} is: {a+b}")
    elif user_input == "subtraction":
        a, b = calculator()
        if a is None:
            continue
        print(f"The subtraction of {a} - {b} is: {a-b}")
    elif user_input == "multiplication":
        a, b = calculator()
        if a is None:
            continue
        print(f"The multiplication of {a} x {b} is: {a*b}")
    elif user_input == "division":
        a, b = calculator()
        if a is None:
            continue
        if b == 0:
            print("Division Error, try again!")
            continue
        print(f"The division of {a} / {b} is: {a/b}")
    elif user_input == "exit":
        print("Program ended successfully!")
        break
    else:
        print("Enter the proper integer values and try again!")


from os import *
def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    return a/b

def calculator():
    num1=float(input("Enter first number: "))
    operation_dict={
        "+":add,
        "-":subtract,
        "*":multiply,
        "/":divide
    }

    flag=True
    while flag:
        for symbol in operation_dict:
            print(symbol)
        op_symbol = input("Enter operation: ")
        calculator_function=operation_dict[op_symbol]
        num2=float(input("Enter next number: "))
        output=calculator_function(num1,num2)
        print(f"{num1} {op_symbol} {num2} = {output}")
        should_continue=input(f"Enter 'y' to continue with {output},if not enter 'n',if want to exit enter 'x': ").lower()
        if should_continue=="y":
            num1=output
            flag=True
        elif should_continue=="n":
            flag=False
            system('cls')
            calculator()
        else:
            flag=False
            print("Bye!!")
calculator()
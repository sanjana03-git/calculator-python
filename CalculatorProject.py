def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    if n2 == 0:
        return "Error: Division by zero"
    return n1 / n2

def power(n1, n2):
    return n1 ** n2

def modulus(n1, n2):
    return n1 % n2  

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
    "**": power,
    "%": modulus,
}

print("Calculator")
while True:
    n1 = float(input("Enter first number: "))
    should_continue = True
    while should_continue:
        for symbol in operations:
            print(symbol)
        operation_symbol = input("Pick an operation (+, -, *, /, **, %): ")
        n2 = float(input("Enter second number: "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(n1, n2)
        print(f"{n1} {operation_symbol} {n2} = {answer}")

        choice = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ")

        if choice == 'y':
            n1 = answer
        elif choice == 'n':
            should_continue = False
        else:
            print("Invalid choice. Please enter 'y' or 'n'.")
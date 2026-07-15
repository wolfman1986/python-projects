def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def calculate(operation, num1, num2):
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    elif operation == "/":
        if num2 == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        return num1 / num2
    elif operation == "**":
        return num1 ** num2
    elif operation == "%":
        return num1 % num2
    elif operation == "//":
        if num2 == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        return num1 // num2
    else:
        raise ValueError("Invalid operation.")

def calculator():
    print("Simple Calculator")
    print("Operations: +  -  *  /  **  %  //")
    print("Type 'exit' to quit.\n")

    while True:
        op = input("Choose operation: ").strip()

        if op.lower() == "exit":
            print("Goodbye!")
            break

        if op not in {"+", "-", "*", "/", "**", "%", "//"}:
            print("Invalid operation. Try again.")
            continue

        num1 = get_number("Enter first number: ")
        num2 = get_number("Enter second number: ")

        try:
            result = calculate(op, num1, num2)
            print("Result:", result)
        except Exception as e:
            print("Error:", e)

        print()

if __name__ == "__main__":
    calculator()
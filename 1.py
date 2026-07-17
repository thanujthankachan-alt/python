a = int(input("Enter numerator: "))
b = int(input("Enter denominator: "))

if b == 0:
    print("Error: Division by zero is not allowed.")
else:
    result = a / b
    print("Result =", result)
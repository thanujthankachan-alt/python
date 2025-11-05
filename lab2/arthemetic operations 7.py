
a = int(input("Enter the first integer: "))
b = int(input("Enter the second integer: "))


addition = a + b
subtraction = a - b
multiplication = a * b
division = a / b if b != 0 else "Undefined (division by zero)"


print("\n--- Arithmetic Operations ---")
print(f"Addition: {a} + {b} = {addition}")
print(f"Subtraction: {a} - {b} = {subtraction}")
print(f"Multiplication: {a} * {b} = {multiplication}")
print(f"Division: {a} / {b} = {division}")

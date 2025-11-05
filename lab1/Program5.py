def string_copies(s, n):
    if n < 0:
        return "Please enter a non-negative integer."
    return s * n


string_input = input("Enter a string: ")
n = int(input("Enter a non-negative integer: "))

result = string_copies(string_input, n)
print("Result:", result)

a = 10
b = 5
print(f"before swap: a = {a}, b = {b}")
a = a + b
b = a - b
a = a - b
print(f"after swap: a = {a}, b = {b}")
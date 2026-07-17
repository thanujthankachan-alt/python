my_tuple = (10, "Python", 3.14, True)
print("Slicing")
print(my_tuple[1:3])
print("\nIteration")
for item in my_tuple:
    print("Element:", item)
print("\nPacking & Unpacking")
packed = ("Alice", 25, "Engineer")
print("Packed tuple:", packed)
name, age, job = packed
print("Name:", name)
print("Age:", age)
print("Job:", job)
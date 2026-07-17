student = {
    "name": "Alex",
    "age": 21,
    "course": "Computer Science"
}
print("Original Dictionary:", student)
name_value = student["name"]
print("Accessed Name:", name_value)
student["grade"] = "A"
print("After Adding Grade:", student)
student["age"] = 22
print("After Updating Age:", student)
student.pop("course")
print("After Removing Course:", student)
print("\n--- Displaying All Key-Value Pairs ---")
for key, value in student.items():
    print(f"{key}: {value}")
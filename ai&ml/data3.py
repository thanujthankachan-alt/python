import pandas as pd

student_data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Eva", "Frank"],
    "Marks": [88, 75, 92, 81, 67, 95]
}

df = pd.DataFrame(student_data)

print("Student Data:")
print(df)

filtered_students = df[df["Marks"] > 80]

print("\nStudents with Marks Greater Than 80:")
print(filtered_students)

sorted_students = df.sort_values(by="Marks", ascending=False)

print("\nStudents Sorted by Marks (Descending Order):")
print(sorted_students)
import pandas as pd

student_data = {
    "Student_ID": [101, 102, 103, 104, 105],
    "Name": ["Alice", "Bob", "Charlie", "David", "Eva"],
    "Course": ["Computer Science", "Mathematics", "Physics", "Biology", "Chemistry"],
    "Marks": [88, 75, 92, 81, 90]
}

df = pd.DataFrame(student_data)

df.to_csv("students.csv", index=False)

df_csv = pd.read_csv("students.csv")

print("Student Data:")
print(df_csv)

print("\nFirst Row:")
print(df_csv.head(1))

print("\nLast Row:")
print(df_csv.tail(1))
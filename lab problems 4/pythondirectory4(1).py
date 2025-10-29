# Dictionary of student marks
students = {
"Anu": 340,
"Teena": 458,
"John": 300
}
# Sort by keys (ascending)
asc_by_name = dict(sorted(students.items()))
print("Sorted by Name (Ascending):")
print(asc_by_name)
# Sort by keys (descending)
desc_by_name = dict(sorted(students.items(), reverse=True))
print("\nSorted by Name (Descending):")
print(desc_by_name)

# Contact dictionaries
contacts1 = {
"Anu": "9876543210",
"Teena": "8765432109"
}
contacts2 = {
"John": "7654321098",
"Priya": "6543210987"
}
print("Contact1:",contacts1)
print("Contact2:",contacts2)

# Merge dictionaries using update()
merged_contacts = contacts1.copy()
merged_contacts.update(contacts2)
print("Merged Contacts:")
print(merged_contacts)

# Program to maintain student records using a dictionary
# Keys - Student names
# Values - List of marks in 3 subjects
students = {
"Anu": [85, 90, 78],
"Gowri": [72, 88, 91],
"Vishnu": [95, 80, 85]
}
# Display student records
for name, marks in students.items():
    total = sum(marks) # total marks
    average = sum(marks) / len(marks) # average marks
    print(f"Student: {name}")
    print(f"Marks: {marks}")
    print(f"Total Marks: {total}")
    print(f"Average Marks: {average:.2f}")
    print("." * 20)
students = {"Anu": 340,"Teena": 458,"John": 300}

asc_by_name = dict(sorted(students.items()))
print("Sorted by Name (Ascending):")
print(asc_by_name)

desc_by_name = dict(sorted(students.items(), reverse=True))
print("\nSorted by Name (Descending):")
print(desc_by_name)
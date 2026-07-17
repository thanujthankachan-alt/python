import pandas as pd

employee_data = {
    "Department": ["MCA", "CSE", "MCA", "CSE", "ECA"],
    "EmployeeName": ["Alice", "Bob", "Charlie", "David", "Eva"],
    "Salary": [50000, 60000, 55000, 65000, 45000]
}

df = pd.DataFrame(employee_data)

print("Employee Details:")
print(df)

average_salary = df.groupby("Department")["Salary"].mean()

print("\nAverage Salary of Each Department:")
print(average_salary)
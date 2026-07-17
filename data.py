import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'Diana'],
    'Age': [25, 30, 35, 28],
    'City': ['New York', 'London', 'Paris', 'Sydney'],
    'Salary': [72000.50, 85000.00, 98000.00, 91000.50]
}


df = pd.DataFrame(data)


print("--- Visualizing the DataFrame ---")
print(df)
print("\n" + "="*40 + "\n")


print("--- DataFrame Structural Info ---")
df.info()
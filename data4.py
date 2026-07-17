import pandas as pd
import numpy as np

student_data = {
    "Name": ["Alice", "Bob", "Charlie", "David", np.nan],
    "Age": [20, 21, np.nan, 22, 19],
    "Marks": [88, np.nan, 92, 81, 75]
}

df = pd.DataFrame(student_data)

print("Student Data:")
print(df)

print("\nMissing Values in the DataFrame:")
print(df.isnull())
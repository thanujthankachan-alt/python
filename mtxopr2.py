import numpy as np

A, K = np.array([[10, 20, 30],
                 [40, 50, 60],
                 [70, 80, 90]]), 1

print("STATISTICS")
print(" Sum:", A.sum())
print(" Mean:", A.mean())
print(" Max:", A.max())
print("Min:", A.min())

print("\nCOLUMN STATISTICS (axis=0)")
print("Column Sums:", A.sum(axis=0))
print("Column Means:", A.mean(axis=0))
print("Column Maxes:", A.max(axis=0))
print("Column Mins:", A.min(axis=0))

print("\n ROW STATISTICS (axis=1)")
print("Row Sums:", A.sum(axis=1))
print("Row Means:", A.mean(axis=1))
print("Row Maxes:", A.max(axis=1))
print("Row Mins:", A.min(axis=1))

print("\nTRANSFORMATIONS")
print(f"Rotate Up by {K}:\n", np.roll(A, shift=-K, axis=0))
print("\nFlip Left-Right:\n", np.fliplr(A))
print("\nFlip Up-Down:\n", np.flipud(A))
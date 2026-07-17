import numpy as np

A = np.array([[1, 2],
              [3, 4]])

B = np.array([[5, 6],
              [7, 8]])

print("--- Original Matrices ---")
print("Matrix A:\n", A)
print("\nMatrix B:\n", B)


print("\n--- Operations on Matrix A ---")
print("Transpose:\n", A.T)
print(f"Determinant: {np.linalg.det(A):.4f}")
print("Inverse:\n", np.linalg.inv(A))
print("Reshaped (4x1):\n", A.reshape(4, 1))


print("\n--- Multi-Matrix Operations ---")
print("Addition (A + B):\n", A + B)
print("Subtraction (A - B):\n", A - B)
print("Matrix Multiplication (A @ B):\n", A @ B)
print("Element-wise Division (A / B):\n", A / B)
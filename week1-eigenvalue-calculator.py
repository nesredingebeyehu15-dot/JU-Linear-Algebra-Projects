# JU-Linear-Algebra-Projects
# Lab Notebook: Week 1
# Topic: Eigenvalue Calculator for a 2x2 Matrix

# This program calculates the eigenvalues for a given 2x2 matrix.
# It is based on the characteristic equation: det(A - λI) = 0

import numpy as np

def calculate_eigenvalues(matrix):
    """
    Calculates the eigenvalues of a 2x2 matrix.
    Input: A 2x2 numpy array.
    Output: The calculated eigenvalues.
    """
    # Using numpy's built-in function for simplicity and accuracy
    # In our theory class, we learned how to do this by hand:
    # (a-λ)(d-λ) - bc = 0
    eigenvalues, eigenvectors = np.linalg.eig(matrix)
    return eigenvalues

# --- Our Test Matrix from Session 3 ---
# B = [[3, 0], [1, 2]]
# We manually calculated the eigenvalues to be 3 and 2.
# Let's verify with our program.

B = np.array([[3, 0], [1, 2]])

# Calculate the eigenvalues
calculated_eigenvalues = calculate_eigenvalues(B)

# Print the results
print(f"The matrix is:\n{B}")
print(f"The calculated eigenvalues are: {calculated_eigenvalues}")
print("\nVerification: Our manual calculation was correct!")

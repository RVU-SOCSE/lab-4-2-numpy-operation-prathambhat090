import numpy as np

A = np.array([[1,2,3],
              [4,5,6],
              [7,8,9]])

B = np.array([[9,8,7],
              [6,5,4],
              [3,2,1]])

while True:

    print("\n---- MATRIX MENU ----")
    print("1. Display Matrices")
    print("2. Matrix Addition")
    print("3. Matrix Subtraction")
    print("4. Matrix Multiplication")
    print("5. Transpose of Matrix A")
    print("6. Determinant of Matrix A")
    print("7. Inverse of Matrix A")
    print("8. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("Matrix A:\n", A)
        print("Matrix B:\n", B)

    elif choice == 2:
        print("Addition:\n", A + B)

    elif choice == 3:
        print("Subtraction:\n", A - B)

    elif choice == 4:
        print("Multiplication:\n", np.dot(A, B))

    elif choice == 5:
        print("Transpose of A:\n", A.T)

    elif choice == 6:
        print("Determinant of A:", np.linalg.det(A))

    elif choice == 7:
        print("Inverse of A:\n", np.linalg.inv(A))

    elif choice == 8:
        print("Program Ended")
        break

    else:
        print("Invalid choice")
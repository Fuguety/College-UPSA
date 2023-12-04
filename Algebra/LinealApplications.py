# Author: Lucas Barreiro Gomes
import numpy as np
from scipy.linalg import null_space
from scipy.linalg import solve




out = True

while (out):

    print("Welcome\nWich question would you like to see the answer?")
    answer = input()

    while (not isinstance(answer, str) or not (answer.isnumeric() and 0 < int(answer) < 9)):
        print("Please insert a valid question number")
        answer = input()
    
    answer = int(answer)

    if (answer == 1):

        matrix = np.random.randint(1, 6, size=(8, 6))

        vector_in_R6 = np.ones(6)

        image_vector = np.dot(matrix, vector_in_R6)

        kernel_basis = null_space(matrix)

        image_basis = null_space(matrix.T)

        print("Matrix:")
        print(matrix)
        print("\nVector in R^6:")
        print(vector_in_R6)
        print("\nImage of the vector in R^6:")
        print(image_vector)
        print("\nBasis of ker(f) using scipy.linalg.null_space:")
        print(kernel_basis)
        print("\nBasis of Im(f) using scipy.linalg.null_space(matrix.T):")
        print(image_basis)

    elif (answer == 2):

        U_matrix = np.array([[1, 0, 0],
                            [3, -1, -1],
                            [-1, -1, 0]])

        V_matrix = np.array([[1, 1, 0],
                            [3, -1, -1],
                            [-1, -1, 1]])

        a_u_basis = np.array([2, 3, 2])

        a_v_basis = solve(U_matrix, a_u_basis)

        print("Vector a in the u-basis:", a_u_basis)
        print("Vector a in the v-basis:", a_v_basis)


    elif (answer == 3):

        B1 = np.array([[1, 1, 0], [1, 0, 1], [0, 1, 1]])
        B1_prime = np.array([[1, -1, 1], [-1, 1, 1], [1, 1, -1]])
        B2 = np.array([[1, 0, 1, 1], [0, 1, 1, 1], [1, 1, 0, 1], [1, 1, 1, 0]])

        coordinates_B1 = np.array([1, 2, -1])

        vector_R3_B1 = solve(B1, coordinates_B1)

        coordinates_B1_prime = solve(B1_prime, coordinates_B1)

        change_matrix_B1_to_B1_prime = solve(B1_prime, B1.T).T

        change_matrix_Bc_to_B2 = B2

        print("Vector in R^3 with respect to B1:", vector_R3_B1)
        print("Coordinates in B1_prime:", coordinates_B1_prime)
        print("\nChange of basis matrix from B1 to B1_prime:")
        print(change_matrix_B1_to_B1_prime)
        print("\nChange of basis matrix from Bc to B2:")
        print(change_matrix_Bc_to_B2)


    elif (answer == 4):

        B1 = np.array([[1, 1, 0], [1, 0, 1], [0, 1, 1]])
        B1_prime = np.array([[1, -1, 1], [-1, 1, 1], [1, 1, -1]])
        Bc = np.eye(4)
        B2 = np.array([[1, 0, 1, 1], [0, 1, 1, 1], [1, 1, 0, 1], [1, 1, 1, 0]])

        f_B1_Bc = np.array([[1, 0, 0, 0], [1, 1, 0, 0], [0, 1, 1, 0], [0, 0, 0, 1]])
        f_B1_B2 = np.array([[1, 0, 1, 1], [1, 1, 1, 1], [0, 1, 0, 1], [0, 0, 0, 0]])
        f_B1_prime_Bc = np.array([[1, -1, 1, 0], [-1, 1, 1, 0], [1, 1, -1, 0], [0, 0, 0, 0]])
        f_B1_prime_B2 = np.array([[1, -1, 1, 1], [-1, 1, 1, 1], [1, 1, -1, 0], [0, 0, 0, 0]])

        # Display the results
        print("Matrix of f with respect to B1 and Bc:")
        print(f_B1_Bc)
        print("\nMatrix of f with respect to B1 and B2:")
        print(f_B1_B2)
        print("\nMatrix of f with respect to B'1 and Bc:")
        print(f_B1_prime_Bc)
        print("\nMatrix of f with respect to B'1 and B2:")
        print(f_B1_prime_B2)


    elif(answer == 5):
        continue
        

    print("Do you wish to exit?")
    answer2 = input()
    
    if answer2.lower() == "yes":
        out = False
    else:
        continue
# Author: Lucas Barreiro Gomes

import numpy as np
import sympy as sp


out = True

while (out):

    print("Welcome\nWich question would you like to see the answer?")
    answer = input()

    while (not isinstance(answer, str) or not (answer.isnumeric() and 0 < int(answer) < 15)):
        print("Please insert a valid question number")
        answer = input()
    
    answer = int(answer)

    if (answer == 1):
       
        matrix = [
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12]
        ]

        num_rows = len(matrix)
        num_columns = len(matrix[0])  

        print(f"Number of rows: {num_rows}")
        print(f"Number of columns: {num_columns}")

    elif (answer == 2):

        vector1 = np.array([1, 2, 3])
        vector2 = np.array([4, 5, 6])

        columns = np.concatenate((vector1, vector2), axis=0)

        lines = np.vstack((vector1, vector2))

        print("Columns:")
        print(columns)

        print("\nLines:")
        print(lines)
    
    elif (answer == 3):

        matrix = np.array([
            [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
            [11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
            [21, 22, 23, 24, 25, 26, 27, 28, 29, 30],
            [31, 32, 33, 34, 35, 36, 37, 38, 39, 40],
            [41, 42, 43, 44, 45, 46, 47, 48, 49, 50],
            [51, 52, 53, 54, 55, 56, 57, 58, 59, 60],
            [61, 62, 63, 64, 65, 66, 67, 68, 69, 70],
            [71, 72, 73, 74, 75, 76, 77, 78, 79, 80],
            [81, 82, 83, 84, 85, 86, 87, 88, 89, 90],
            [91, 92, 93, 94, 95, 96, 97, 98, 99, 100]
        ])
        

        inverse_matrix = np.linalg.pinv(matrix)
        
        print("Original matrix:")
        print(matrix)
        
        print("\nInverse matrix:")
        print(inverse_matrix)

    elif (answer == 4):

        random_array = np.random.rand(4, 5)

        print("Array with random numbers")
        print(random_array)
    
    elif (answer == 5):

        random_array = np.random.normal(0, 1, (5, 4))

        print("Array with random numbers")
        print(random_array)

    elif (answer == 6):

        matrix = np.array([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]])

        inverse_matrix = np.linalg.pinv(matrix)

        print("Original:")
        print(matrix)

        print("\Inverted:")
        print(inverse_matrix)

    elif (answer == 7):

        matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        diagonal = [matrix[i][i] for i in range(3)]

        print("Original matrix:")
        for row in matrix:
            print(row)

        print("\nDiagonal of the matrix:")
        print(diagonal)

    elif (answer == 8):

        matrix = np.random.randint(1, 6, (5, 5))
        determinant = np.linalg.det(matrix)

        print("Random 5x5 matrix:")
        print(matrix)

        print("\nDeterminant of the matrix:")
        print(determinant)

    elif (answer == 9):

        matrix = np.array([[1, 2, 3],
                          [4, 5, 6],
                          [7, 8, 9]])

        rank = np.linalg.matrix_rank(matrix)

        print("Original matrix:")
        print(matrix)

        print("\nRank of the matrix:")
        print(rank)

    elif (answer == 10):

        matrix = sp.Matrix([[1, 2, 3],
                           [4, 5, 6],
                           [7, 8, 9]])

        rref_matrix = matrix.rref()

        print("\nReduced form:")
        print(rref_matrix[0])

    elif (answer == 11):

        vector = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])

        matrix = vector.reshape(3, 3)

        print("Matrix:")
        print(matrix)

    elif (answer == 12):

        matrix = [[1, 2, 3],
          [4, 5, 6]]

        element = matrix[1][1]

        print("Matrix:")
        for row in matrix:
            print(row)

        print("\nSecond element of second line:", element)

    elif (answer == 13):

        matrix = [[1, 2, 3],
          [4, 5, 6]]

        trace = matrix[0][0] + matrix[1][1]

        print("Matrix:")
        for row in matrix:
            print(row)

        print("\nSum of the diagonal:", trace)

    elif (answer == 14):

        matrix = [[1, 2, 3],
          [4, 5, 6]]

        transpose = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

        print("Original:")
        for row in matrix:
            print(row)

        print("\nTransposed:")
        for row in transpose:
            print(row)

    print("Do you wish to exit?")
    answer2 = input()
    
    if answer2.lower() == "yes":
        out = False
    else:
        continue

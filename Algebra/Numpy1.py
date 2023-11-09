# Author: Lucas Barreiro Gomes
import numpy as np
import cmath
from numpy import sqrt

def find_quadratic_roots(a, b, c):
    discriminant = b**2 - 4*a*c

    if discriminant > 0:

        root1 = (-b + cmath.sqrt(discriminant)) / (2*a)
        root2 = (-b - cmath.sqrt(discriminant)) / (2*a)
        print("Two real roots:")
        print("Root 1:", root1)
        print("Root 2:", root2)

    elif discriminant == 0:

        root = -b / (2*a)
        print("One real double root:")
        print("Root:", root)

    else:
        real_part = -b / (2*a)
        imaginary_part = cmath.sqrt(-discriminant) / (2*a)
        root1 = complex(real_part, imaginary_part)
        root2 = complex(real_part, -imaginary_part)
        print("Complex roots:")
        print("Root 1:", root1)
        print("Root 2:", root2)






out = True

while (out):

    print("Welcome\nWich question would you like to see the answer?")
    answer = input()

    while (not isinstance(answer, str) or not (answer.isnumeric() and 0 < int(answer) < 9)):
        print("Please insert a valid question number")
        answer = input()
    
    answer = int(answer)

    if (answer == 1):

        matrix = np.random.normal(0, 1, (10, 10))

        row_sums = np.sum(matrix, axis=1)
       
        column_sums = np.sum(matrix, axis=0)
       
        total_sum = np.sum(matrix)

        determinant = np.linalg.det(matrix)

        rank = np.linalg.matrix_rank(matrix)

        num_columns = matrix.shape[1]

        element_type = matrix.dtype

        print("Sum of rows:")
        print(row_sums)

        print("\nSum of columns:")
        print(column_sums)

        print("\nSum of all elements in the matrix:")
        print(total_sum)

        print("\nDeterminant of the matrix:")
        print(determinant)

        print("\nRank of the matrix:")
        print(rank)

        print("\nNumber of columns:")
        print(num_columns)

        print("\nType of elements in the matrix:")
        print(element_type)

    elif (answer == 2):

        matrix = np.random.randint(0, 10, (5, 5))

        row_sums = np.sum(matrix, axis=1)

        column_sums = np.sum(matrix, axis=0)

        total_sum = np.sum(matrix)

        determinant = np.linalg.det(matrix)

        rank = np.linalg.matrix_rank(matrix)

        num_rows = matrix.shape[0]

        element_type = matrix.dtype

        print("5x5 Matrix:")
        print(matrix)

        print("\nSum of rows:")
        print(row_sums)

        print("\nSum of columns:")
        print(column_sums)

        print("\nSum of all elements in the matrix:")
        print(total_sum)

        print("\nDeterminant of the matrix:")
        print(determinant)

        print("\nRank of the matrix:")
        print(rank)

        print("\nNumber of rows:")
        print(num_rows)

        print("\nType of elements in the matrix:")
        print(element_type)

    elif (answer == 3):

        A = np.array([[2, 0, 0, 0, 0],
                      [0, 3, 0, 0, 0],
                      [0, 0, 4, 0, 0],
                      [0, 0, 0, 5, 0],
                      [0, 0, 0, 0, 6]])

        diagonal_sum = np.trace(A)

        determinant = np.linalg.det(A)

        inverse_matrix = np.linalg.inv(A)

        print("Diagonal matrix A:")
        print(A)

        print("\nSum of diagonal elements:")
        print(diagonal_sum)

        print("\nDeterminant of matrix A:")
        print(determinant)

        print("\nInverse matrix of A:")
        print(inverse_matrix)

    elif (answer == 4):

        A = np.array([
            [1, 0, 0],
            [0, 1, 0],
            [0, 0, 1]])
        
        B = np.array([
            [1, 1, 1],
            [1, 2, 1],
            [1, 1, 1]])
        
        C = np.array([
            [1, 1, 1],
            [0, sqrt(2), -sqrt(2)],
            [1, -1, -1]])
        
        # AB - BA
        result1 = np.dot(A, B) - np.dot(B, A)

        # A^2 + B^2 + C^2
        result2 = np.dot(A, A) + np.dot(B, B) + np.dot(C, C)

        # sqrt(A) + sqrt(B) - sqrt(C)
        result3 = sqrt(A) + sqrt(B) - sqrt(C)
        
        # e^A * (e^B + e^C)
        eA = np.exp(A)
        eB = np.exp(B)
        eC = np.exp(C)
        result4 = np.dot(eA, eB + eC)

        #  rank, inverse, trace and determinant
        rank_A = np.linalg.matrix_rank(A)
        inv_A = np.linalg.inv(A)
        trace_A = np.trace(A)
        det_A = np.linalg.det(A)

        rank_B = np.linalg.matrix_rank(B)
        trace_B = np.trace(B)
        det_B = np.linalg.det(B)

        rank_C = np.linalg.matrix_rank(C)
        inv_C = np.linalg.inv(C)
        trace_C = np.trace(C)
        det_C = np.linalg.det(C)

        # printing time :)
        print("AB - BA:\n", result1)
        print("\nA^2 + B^2 + C^2:\n", result2)
        print("\nsqrt(A) + sqrt(B) - sqrt(C)\n", result3)
        print("\ne^A * (e^B + e^C):\n", result4)

        print("Rank, inverse, trace and determinant of A:")
        print("Rank", rank_A)
        print("Inverse:\n", inv_A)
        print("Trace:", trace_A)
        print("Determinant:", det_A)

        print("Rank, inverse, trace and determinant of B:")
        print("Rank", rank_B)
        print("Inverse:\n", "There is no inverse on B")
        print("Trace:", trace_B)
        print("Determinant:", det_B)

        print("Rank, inverse, trace and determinant of C:")
        print("Rank", rank_C)
        print("Inverse:\n", inv_C)
        print("Trace:", trace_C)
        print("Determinant:", det_C)
         

    elif (answer == 5):

        find_quadratic_roots(1, 0, -4)

    elif (answer == 6):

        vector = [1 + 4 * i / i ** 2 for i in range(1, 101)]

        sum_elements = sum(vector)

        sorted_vector = sorted(vector)

        reverse_sorted_vector = sorted(vector, reverse=True)

        max_element = max(vector)
        vector.remove(max_element)

        print("Vector (first 100 elements):", vector)
        print("Sum of the first 100 elements:", sum_elements)
        print("Sorted vector (ascending order):", sorted_vector)
        print("Sorted vector (descending order):", reverse_sorted_vector)
        print("Vector with the largest element removed:", vector)

    elif (answer == 7):

        A = np.random.rand(10, 10)

        determinant_A = np.linalg.det(A)


        if determinant_A != 0:
            print("Matrix is invertible")
        else:
            print("Singular matrix")

    elif (answer == 8):
        matrix = np.linspace(-1, 1, 25).reshape(5, 5)

        sum_of_elements = np.sum(matrix)

        max_in_columns = np.max(matrix, axis=0)
        normalized_matrix = matrix / max_in_columns

        columns_with_negatives = np.any(matrix < 0, axis=0)

        column_with_max_sum = np.argmax(np.sum(matrix, axis=0))

        print(matrix)
        print(sum_of_elements)
        print(normalized_matrix)
        print(columns_with_negatives)
        print(column_with_max_sum)



    print("Do you wish to exit?")
    answer2 = input()
    
    if answer2.lower() == "yes":
        out = False
    else:
        continue
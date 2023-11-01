import numpy as np
import sympy as sp
import cmath

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

        continue

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
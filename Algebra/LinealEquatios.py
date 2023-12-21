import numpy as np
import sympy as sp
import scipy
from sympy import Matrix, symbols, Eq, solve




out = True

while (out):

    print("Welcome\nWich question would you like to see the answer?")
    answer = input()

    while (not isinstance(answer, str) or not (answer.isnumeric() and 0 < int(answer) < 9)):
        print("Please insert a valid question number")
        answer = input()
    
    answer = int(answer)

    if (answer == 1):

        A_b = np.array([[-4, -2, 0,  2, -4,  4,  2],\
                [ 4,  1, 0, -3,  4, -4, -3],\
                [ 1, -2, 0, -3,  1, -1, -3],\
                [ 0, -2, 0, -2,  1, -1, -2]])

        print(A_b)

        rref_Ab, pivots = sp.Matrix(A_b).rref()
        rref_Ab = np.array(rref_Ab)

        print('\n', rref_Ab, '\n', pivots)

        if (rref_Ab.shape[1] - 1) in pivots:
            print('\n Sistema Incompatible')
        
        elif len(pivots) == rref_Ab.shape[1] - 1:
            print('\n Sistema Compatible Determinado')
        
        else:
            print('\n Sistema Compatible Indeterminado')


    elif (answer == 2):

        
        matrix_a = Matrix([
            [3, -1, 0, -1, -3, -1, -2, -3],
            [-2, 0, 0, 0, 2, 0, 2, 2],
            [3, 0, 0, -1, 1, -2, -1, -1],
            [0, 0, 0, 1, -2, 2, -2, -2],
            [3, 1, 0, 0, -1, -1, -2, -1],
            [1, -4, 0, -2, -5, 0, -1, -5]
        ])


        rref_matrix_a, pivot_columns_a = matrix_a.rref()

        print("Matrix (a) in row-reduced echelon form:")
        print(rref_matrix_a)
        print("\nPivot columns in (a):", pivot_columns_a)


        matrix_b = Matrix([
            [-2, -2, 2, -1, 1, -2, -1, -1, 0],
            [-1, -2, 2, 1, 3, -1, -2, -1, 0],
            [0, 0, 1, 0, 3, -2, -1, -1, 0],
            [1, 0, 0, 2, 2, 1, -1, 0, 0],
            [-2, 1, 0, -1, -2, -1, 0, 0, 0],
            [0, 1, -2, -1, -4, 1, 2, 1, 0],
            [0, 1, 2, 1, 2, -2, -1, -2, 0],
            [-2, -1, 0, 1, 0, -1, -1, -1, -1]
        ])


        rref_matrix_b, pivot_columns_b = matrix_b.rref()

        print("\nMatrix (b) in row-reduced echelon form:")
        print(rref_matrix_b)
        print("\nPivot columns in (b):", pivot_columns_b)


    elif (answer == 3):

        x1, x2, x3, x4, x5, x6 = symbols('x1 x2 x3 x4 x5 x6')

        A = Matrix([
            [1, 0, -1, 0, 1, 0],
            [-1, 1, 0, 0, 0, 0],
            [0, -1, 1, 0, 0, 0],
            [0, 0, -1, 1, 0, 0],
            [0, 1, 0, -1, 0, 0],
            [1, 0, 0, 0, -1, 0]
        ])

        B = Matrix([200, 0, 0, 0, 100, 200])

        X = Matrix([x1, x2, x3, x4, x5, x6])

        solution = solve(A * X - B, X)

        print("Solution of the system of equations:")
        print(solution)


        augmented_matrix = A.row_join(B)


        print("\nAugmented Matrix:")
        print(augmented_matrix)


        rref_matrix, pivot_columns = augmented_matrix.rref()


        print("\nReduced Row-Echelon Form:")
        print(rref_matrix)


    elif (answer == 4):
        grid = [
            [0, 0, 0, 0, 0],
            [0, 50, 50, 50, 0],
            [0, 50, 0, 50, 0],
            [0, 50, 50, 50, 0],
            [0, 0, 0, 0, 0]
        ]

        num_iterations = 10

        def calculate_average_temperature(grid):
            rows, cols = len(grid), len(grid[0])
            new_grid = [[0] * cols for _ in range(rows)]

            for i in range(1, rows - 1):
                for j in range(1, cols - 1):
                    average_temperature = (grid[i - 1][j] + grid[i + 1][j] + grid[i][j - 1] + grid[i][j + 1]) / 4
                    new_grid[i][j] = average_temperature

            return new_grid

        for _ in range(num_iterations):
            grid = calculate_average_temperature(grid)

        for row in grid:
            print(row)
         

    elif (answer == 5):


        A_B = np.array ( [ [1, 2, 5, 10, 400], [0, 1, -1, 0, 0], [1, 1, 1, 1, 100] ] )
        print(A_B)

        matrix_scaled = Matrix(A_B).rref()
        print (matrix_scaled)

    elif (answer == 6):
        continue



    print("Do you wish to exit?")
    answer2 = input()
    
    if answer2.lower() == "yes":
        out = False
    else:
        continue

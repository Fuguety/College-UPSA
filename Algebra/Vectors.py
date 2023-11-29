import numpy as np

def row_echelon_form(matrix):
    m, n = matrix.shape
    
    for i in range(m):
        # Find the pivot
        pivot_index = np.argmax(np.abs(matrix[i:, i])) + i
        matrix[[i, pivot_index]] = matrix[[pivot_index, i]]
        
        matrix[i] /= matrix[i, i]
        
        for j in range(i + 1, m):
            matrix[j] -= matrix[j, i] * matrix[i]
    
    for i in range(m - 1, 0, -1):
        for j in range(i - 1, -1, -1):
            matrix[j] -= matrix[j, i] * matrix[i]

    return matrix



out = True

while out:
    print("Welcome\nWhich question would you like to see the answer?")
    answer = input()

    while not (answer.isnumeric() and 0 < int(answer) < 8):
        print("Please insert a valid question number")
        answer = input()

    if int(answer) == 1:
        
        A = np.array([
            [2, 3, 4, -1, 1],
            [3, 4, 7, -2, -1],
            [1, 3, -1, 1, 8],
            [0, 5, 5, -1, 4]])

        # A)
        reduced_vectors, _ = np.linalg.qr(A.T)

        basis = reduced_vectors[:, np.abs(reduced_vectors).max(axis=0) > 1e-10]
        dimension = basis.shape[1]
        
        print("Dimension: ", dimension)

        # B)
        basis_matrix = np.hstack([A.T, basis])

        reduced_basis, _ = np.linalg.qr(basis_matrix, mode='complete')

        complementary_basis = reduced_basis[:, np.abs(reduced_basis).max(axis=0) > 1e-10]

        print(complementary_basis.T)

    elif int(answer) == 2:

        A = np.array([
            [2,3,-1],
            [0,0,1],
            [2,1,0]])
        
        if A.shape[0] == 3 and np.linalg.matrix_rank(A[:, :3]) == 3:
            basis_matrix = np.linalg.inv(A[:, :3])

            x_vector = np.array([3, 4, 1])

            components = np.dot(basis_matrix, x_vector)
        
            print(components)

        else:
            print("Is not on the R3 basis")
    
    elif int(answer) == 3:
        continue

    elif int(answer) == 4:

        basis_S = np.array([
            [1, 1, 0, 0],
            [0, 0, 1, 0],
            [0, 0, 0, 1]])

        basis_T = np.array([
            [1, 1, 2, 1],
            [2, 0, -1, 1]])
        
        basis_S, dimension_S = np.linalg.qr(basis_S.T)
        basis_T, dimension_T = np.linalg.qr(basis_T.T)

        print(f"Basis S {basis_S}, Dimention {dimension_S}")
        print(f"Basis T {basis_T}, Dimention {dimension_T}")



        basis_ST = np.concatenate((basis_S, basis_T), axis=1)
        basis_ST, dimension_ST = np.linalg.qr(basis_ST, mode="complete")

        print(f"Basis ST {basis_ST}, Dimension {dimension_ST}")

        intersection, _, _ = np.linalg.svd(basis_ST)
        dim_intersection = np.linalg.matrix_rank(intersection)

        print(f"Intersection {intersection}")

    elif int(answer) == 5:
        random_subspace = np.random.randn(100, 50)
        for j in range(50):
            random_subspace[:, j] = random_subspace[:, j] / np.linalg.norm(random_subspace[:, j])

        num_trials = 1000
        independent_count = 0
        for i in range(num_trials):
            random_matrix = np.random.randn(100, 50)
            if np.linalg.matrix_rank(random_matrix) == 50:
                independent_count += 1

        print(f"Probability of linear independence: {independent_count / num_trials}")

        random_vector = np.random.randn(100, 1)

        projection_coefficients = np.linalg.lstsq(random_subspace, random_vector, rcond=None)[0]

        print("Projection Coefficients:")
        print(projection_coefficients)

    elif int(answer) == 6:
        A = np.array([[1, 2, 0, 0], [2, 3, 1, -1], [1, 0, -1, 3]])

        row_echelon_A = row_echelon_form(A.copy())

        print("Original Matrix:")
        print(A)
        print("\nRow Echelon Form:")
        print(row_echelon_A)

    print("Do you wish to exit?")
    answer2 = input()
    
    if answer2.lower() == "yes":
        out = False

    else:
        continue

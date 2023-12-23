import numpy as np



def power_iteration(A, max_iter=1000, tol=1e-6):
    n = A.shape[0]
    
    q = np.random.rand(n, 1)
    
    for k in range(max_iter):
        z = A @ q
        q = z / np.linalg.norm(z)
        l = np.transpose(q) @ A @ q

        if np.linalg.norm(A @ q - l * q) < tol:
            break
    
    return l, q



out = True

while (out):

    print("Welcome\nWich question would you like to see the answer?")
    answer = input()

    while (not isinstance(answer, str) or not (answer.isnumeric() and 0 < int(answer) < 4)):
        print("Please insert a valid question number")
        answer = input()
    
    answer = int(answer)

    if (answer == 1):

        A = np.array([ [5, 2, 1] , [2, 7, 0] , [1, 0, -3] ])

        autovalues, P = np.linalg.eig(A)

        print("Autovalues: \n", autovalues)

        print("\nAuto vectos: \n", P[:, 0])
        print("\nAuto vector n2: \n", P[:, 1])
        print("\nAuto vector n3: \n", P[:,2])

        print("\n", P)

        print("\nDiagonal Matrix:\n", np.linalg.inv(P) @ A @ P)

   
    elif (answer == 2):

        A = np.array([[1, -1, 1], [-1, 1, -1], [1, -1, 1]])

        eigenvalues, eigenvectors = np.linalg.eig(A)
        change_of_basis_matrix = eigenvectors
        diagonalized_matrix = np.linalg.inv(eigenvectors) @ A @ eigenvectors

        print("\nEigenvalues:")
        print(eigenvalues)

        print("\nEigenvectors:")
        print(eigenvectors)

        print("\nDiagonalized Matrix:")
        print(diagonalized_matrix)


    elif (answer == 3):


        A = np.array([[2, 1], [1, 3]])

        l, q = power_iteration(A)

        eigvals, eigvecs = np.linalg.eig(A)

        print("Result from power iteration:")
        print("Eigenvalue:\n", l)
        print("\nEigenvector:\n", q)

        print("\nResult from NumPy's eig function:")
        print("Eigenvalues:\n", eigvals)
        print("\nEigenvectors:\n", eigvecs)

        

    print("Do you wish to exit?")
    answer2 = input()
    
    if answer2.lower() == "yes":
        out = False
    else:
        continue
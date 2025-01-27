# Written by Mustaeen Ahmed
# For CAP4611: Algorithms for Machine Learning

import matplotlib.pyplot as plt

def get_eigenvalue(matrix):
    a, b = matrix[0]
    c, d = matrix[1]
    
    t = a + d 
    determinant = (a * d) - (b * c)

    coef_a = 1
    coef_b = -t
    coef_c = determinant
    
    discriminant = coef_b**2 - 4 * coef_a * coef_c
    eigenvalue1 = (-coef_b + discriminant**0.5) / (2 * coef_a)
    eigenvalue2 = (-coef_b - discriminant**0.5) / (2 * coef_a)

    eigenvector1 = get_eigenvector(matrix, eigenvalue1)
    eigenvector2 = get_eigenvector(matrix, eigenvalue2)
    
    return (eigenvalue1, eigenvalue2), (eigenvector1, eigenvector2)

def get_eigenvector(matrix, eigenvalue):
    a, b = matrix[0]
    c, d = matrix[1]
    
    matrix_no_lambda = [
        [a - eigenvalue, b],
        [c, d - eigenvalue]
    ]
    
    if matrix_no_lambda[0][0] != 0:
        x = -matrix_no_lambda[0][1] / matrix_no_lambda[0][0]
        return [1, x]
    elif matrix_no_lambda[1][0] != 0:
        x = -matrix_no_lambda[1][1] / matrix_no_lambda[1][0]
        return [x, 1]
    else:
        return [1, 0]

def plot_vect(m, eval, evec):
    v1 = [1, 0]
    v2 = [0, 1]
    
    Fv1 = [m[0][0] * v1[0] + m[0][1] * v1[1], m[1][0] * v1[0] + m[1][1] * v1[1]]
    Fv2 = [m[0][0] * v2[0] + m[0][1] * v2[1], m[1][0] * v2[0] + m[1][1] * v2[1]]
    
    ev1 = [evec[0][0], evec[0][1]]
    ev2 = [evec[1][0], evec[1][1]]
    
    plt.figure(figsize=(8, 8))
    origin = [0, 0]
    
    plt.quiver(*origin, *v1, color='r', angles='xy', scale_units='xy', scale=1, label="Original v1")
    plt.quiver(*origin, *v2, color='b', angles='xy', scale_units='xy', scale=1, label="Original v2")
    
    plt.quiver(*origin, *Fv1, color='yellow', angles='xy', scale_units='xy', scale=1, label="Transformed v1")
    plt.quiver(*origin, *Fv2, color='pink', angles='xy', scale_units='xy', scale=1, label="Transformed v2")
    
    plt.quiver(*origin, *ev1, color='g', angles='xy', scale_units='xy', scale=1, label="Eigenvector 1")
    plt.quiver(*origin, *ev2, color='purple', angles='xy', scale_units='xy', scale=1, label="Eigenvector 2")
    
    plt.axhline(0, color='gray', linewidth=0.5, linestyle='dashed')
    plt.axvline(0, color='gray', linewidth=0.5, linestyle='dashed')
    plt.xlim(-3, 3)
    plt.ylim(-3, 3)
    plt.grid()
    plt.legend()
    plt.title("Transformation of Vectors")
    plt.xlabel("x-axis")
    plt.ylabel("y-axis")
    
    plt.show()


matrix = [[2, 1], [1, 2]] # can change if needed

eigenvalues, eigenvectors = get_eigenvalue(matrix)

print("Eigenvalues:", eigenvalues)
print("Eigenvectors:", eigenvectors)

plot_vect(matrix, eigenvalues, eigenvectors)

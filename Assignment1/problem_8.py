import numpy as np
import problem_8a as p8a
import problem_8b as p8b

#calculating condition number using 2-norm
def condition_number(A):
    return np.linalg.norm(A)*np.linalg.norm(np.linalg.inv(A))

#error from numpy.linalg.solve
def error_simple_solving(A,b,x):
    return np.linalg.norm(np.dot(A,x)-b)

#residual from numpy.linalg.solve
def residual_simple_solving(A,b,x):
    return np.linalg.norm(np.dot(A,x)-b)/np.linalg.norm(b)


print('-'*75)
print('-'*75)
for i in range(3):
    if(i==1):
        print("Output for A random matrix of size n × n with entries uniformly sampled from [0, 1) :")
        print()
        for j in range(1,5):
            print("n = ",10*j)
            print()
            matrix=np.random.random_sample((10*j,10*j))
            print("Condition number of matrix is: ",condition_number(matrix))
            print()
            x=np.ones(10*j).T
            b=np.dot(matrix,x)
            matrix_no_pivotting,b_no_pivotting=p8a.gaussian_elimination(matrix,b)
            x_result_no_pivotting=p8a.back_substitution(matrix_no_pivotting,b_no_pivotting)

            matrix_with_pivotting,b_with_pivotting=p8b.gaussian_elimination_pivoting(matrix,b)
            x_result_with_pivotting=p8b.back_substitution(matrix,b)

            print("Error from un-pivoted gaussian elimination is: ",p8a.error(matrix_no_pivotting,b_no_pivotting,x_result_no_pivotting))
            print("Residual from un-pivoted gaussian elimination is: ",p8a.residual(matrix_no_pivotting,b_no_pivotting,x_result_no_pivotting))
            print()
            print("Error from pivoted gaussian elimination is: ",p8b.error_pivoting(matrix_with_pivotting,b_with_pivotting,x_result_with_pivotting))
            print("Residual from pivoted gaussian elimination is: ",p8b.residual_pivoting(matrix_with_pivotting,b_with_pivotting,x_result_with_pivotting))

            print()
            x_result_numpy=np.linalg.solve(matrix,b)
            print("Error from numpy.linalg.solve is from: ",error_simple_solving(matrix,b,x_result_numpy))
            print("Residual from numpy.linalg.solve is: ",residual_simple_solving(matrix,b,x_result_numpy))
            print('-'*75)
        print('-'*75)
    
    elif(i==2):
        print("Output for A Hilbert matrix of size n × n :")
        print()
        for j in range(1,5):
            print("n = ",10*j)
            print()
            matrix=np.zeros((10*j,10*j))
            for k in range(10*j):
                for l in range(10*j):
                    matrix[k][l]=1/((k+1)+(l+1)-1)
            print("Condition number of matrix is: ",condition_number(matrix))
            print()
            x=np.ones(10*j).T
            b=np.dot(matrix,x)
            matrix_no_pivotting,b_no_pivotting=p8a.gaussian_elimination(matrix,b)
            x_result_no_pivotting=p8a.back_substitution(matrix_no_pivotting,b_no_pivotting)

            matrix_with_pivotting,b_with_pivotting=p8b.gaussian_elimination_pivoting(matrix,b)
            x_result_with_pivotting=p8b.back_substitution(matrix,b)

            print("Error from un-pivoted gaussian elimination is: ",p8a.error(matrix_no_pivotting,b_no_pivotting,x_result_no_pivotting))
            print("Residual from un-pivoted gaussian elimination is: ",p8a.residual(matrix_no_pivotting,b_no_pivotting,x_result_no_pivotting))
            print()
            print("Error from pivoted gaussian elimination is: ",p8b.error_pivoting(matrix_with_pivotting,b_with_pivotting,x_result_with_pivotting))
            print("Residual from pivoted gaussian elimination is: ",p8b.residual_pivoting(matrix_with_pivotting,b_with_pivotting,x_result_with_pivotting))

            print()
            x_result_numpy=np.linalg.solve(matrix,b)
            print("Error from numpy.linalg.solve is from: ",error_simple_solving(matrix,b,x_result_numpy))
            print("Residual from numpy.linalg.solve is: ",residual_simple_solving(matrix,b,x_result_numpy))
            print('-'*75)
        print('-'*75)

    elif(i==3):
        print("Output for A matrix of size n × n with entries aij = 1 if i ≤ j and aij = −1 otherwise :")
        print()
        for j in range(1,5):
            print("n = ",10*j)
            print()
            matrix=np.zeros((10*j,10*j))
            for k in range(10*j):
                for l in range(10*j):
                    if(k>l):
                        matrix[k][l]=-1
                    else:
                        matrix[k][l]=1
            print("Condition number of matrix is: ",condition_number(matrix))
            print()
            x=np.ones(10*j).T
            b=np.dot(matrix,x)
            matrix_no_pivotting,b_no_pivotting=p8a.gaussian_elimination(matrix,b)
            x_result_no_pivotting=p8a.back_substitution(matrix_no_pivotting,b_no_pivotting)

            matrix_with_pivotting,b_with_pivotting=p8b.gaussian_elimination_pivoting(matrix,b)
            x_result_with_pivotting=p8b.back_substitution(matrix,b)

            print("Error from un-pivoted gaussian elimination is: ",p8a.error(matrix_no_pivotting,b_no_pivotting,x_result_no_pivotting))
            print("Residual from un-pivoted gaussian elimination is: ",p8a.residual(matrix_no_pivotting,b_no_pivotting,x_result_no_pivotting))
            print()
            print("Error from pivoted gaussian elimination is: ",p8b.error_pivoting(matrix_with_pivotting,b_with_pivotting,x_result_with_pivotting))
            print("Residual from pivoted gaussian elimination is: ",p8b.residual_pivoting(matrix_with_pivotting,b_with_pivotting,x_result_with_pivotting))

            print()
            x_result_numpy=np.linalg.solve(matrix,b)
            print("Error from numpy.linalg.solve is from: ",error_simple_solving(matrix,b,x_result_numpy))
            print("Residual from numpy.linalg.solve is: ",residual_simple_solving(matrix,b,x_result_numpy))
            print('-'*75)
        print('-'*75)


























'''print("Condition number of matrix is: ",condition_number(matrix))
print()
x=np.ones(n).T
b=np.dot(matrix,x)


matrix_no_pivotting,b_no_pivotting=p8a.gaussian_elimination(matrix,b)
x_result_no_pivotting=p8a.back_substitution(matrix_no_pivotting,b_no_pivotting)

matrix_with_pivotting,b_with_pivotting=p8b.gaussian_elimination_pivoting(matrix,b)
x_result_with_pivotting=p8b.back_substitution(matrix,b)

print("Error from un-pivoted gaussian elimination is: ",p8a.error(matrix_no_pivotting,b_no_pivotting,x_result_no_pivotting))
print("Residual from un-pivoted gaussian elimination is: ",p8a.residual(matrix_no_pivotting,b_no_pivotting,x_result_no_pivotting))
print()
print("Error from pivoted gaussian elimination is: ",p8b.error_pivoting(matrix_with_pivotting,b_with_pivotting,x_result_with_pivotting))
print("Residual from pivoted gaussian elimination is: ",p8b.residual_pivoting(matrix_with_pivotting,b_with_pivotting,x_result_with_pivotting))

print()
x_result_numpy=np.linalg.solve(matrix,b)
print("Error from numpy.linalg.solve is from: ",error_simple_solving(matrix,b,x_result_numpy))
print("Residual from numpy.linalg.solve is: ",residual_simple_solving(matrix,b,x_result_numpy))'''
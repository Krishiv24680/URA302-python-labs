#Q1.
import numpy as np
arr1=np.arange(5,26)
print("1D array :",arr1)

arr2=np.random.randint(10,51,size=(3,4))
print("2D array:\n",arr2)

#Q2.
print("1D array",arr1)
print("Shape:",arr1.shape)
print("Size:",arr1.size)
print("Data type:",arr1.dtype)


print("2D array:\n",arr2)
print("Shape:",arr2.shape)
print("Size:",arr2.size)
print("Data type:",arr2.dtype)

#Q3.
import numpy as np
Array1=np.array([2,4,6,8,10])
Array2=np.array([1,3,5,7,9])
print("Array1:",Array1)
print("Array2:",Array2)

add=Array1+Array2
print("Addition:",add)
sub=Array1-Array2
print("Subtraction:",sub)
mul=Array1*Array2
print("Multipliation:",mul)
div=Array1/Array2
print("Division:",div)

#Q4.
import numpy as np
arr=np.arange(1,10).reshape(3,3)
print("2D array:\n",arr)

result=arr*5
print("After Broadcasting:\n",result)

#Q5.
import numpy as np
arr=np.arange(10,26).reshape(4,4)
print("Original array:\n",arr)

secondrow=arr[1,:]
lastcolumn=arr[:,-1]
print("Second row:",secondrow)
print("lastcolumn:",lastcolumn)

arr[0,:]=0
print("Array after replacing first row:\n",arr)

#Q6.
import numpy as np
arr=np.random.randint(20,41,size=10)
print("Original array:",arr)

greaterthan30=arr[arr>30]
print("Elements greater than 30:",greaterthan30)

#Q7.
import numpy as np
arr=np.arange(11,23)
print("1D array:",arr)

reshapedarr=arr.reshape(3,4)
print("Reshaped 2D array:\n",reshapedarr)

#Q8.
import numpy as np
A=np.array([[1,2,],[3,4]])
B=np.array([[5,6],[7,8]])
print("Matrix A:\n",A)
print("Matrix B:\n",B)

matmul=np.dot(A,B)
print("Matrix Multioplication:",matmul)

transposeA=A.T
print("Transpose of A:\n",transposeA)

#Q9.
import numpy as np
arr=np.random.randint(10,61,size=15)
print("Original array:",arr)

meanval=np.mean(arr)
medianval=np.median(arr)
stdval=np.std(arr)
print("Mean",meanval)
print("Medain",medianval)
print("Standard Deviation:",stdval)

#Q10.
import numpy as np
A = np.array([[2,1,3],[0,5,6],[7,8,9]], dtype=float)
det = np.linalg.det(A)
inv = np.linalg.inv(A)
eigvals, eigvecs = np.linalg.eig(A) 
print("det:", det)       
print("inv:\n", inv)
print("eigenvalues:\n", eigvals)
print("eigenvectors (cols):\n", eigvecs)

#Q11.
import numpy as np
P = np.array([[0,0],[2,3],[4,7],[7,10],[10,15]], dtype=float)
d_end_to_end = np.linalg.norm(P[-1] - P[0])

step_vectors = np.diff(P, axis=0)                 
total_distance = np.linalg.norm(step_vectors, axis=1).sum()










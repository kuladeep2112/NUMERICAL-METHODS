import numpy as np
from numpy.core.fromnumeric import transpose
A=np.array([[25,1,2],[1,3,0],[2,0,-4]])
V=transpose(np.array([1,1,1]))
#no of iterations
n=10
eigenvalues=[]
Dict={}
for i in range(n):

    temp=np.matmul(A,V)
    V=temp/np.max(temp)
    m=np.max(temp)
    eigenvalues.append(m)
    Dict[m]=(V)

for i in range(len(eigenvalues)-1):
    x=eigenvalues[i+1]-eigenvalues[i]
    if abs(x) < 0.0001:
        print("Eigen Value:",eigenvalues[i+1])
        print("Eigen Vector:",Dict[eigenvalues[i+1]])
        break


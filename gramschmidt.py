import numpy as np
V=np.array([[0,0,1],[0,1,1],[1,1,0],[1,0,0]])
Q=np.array([[0.0 for i in range(3)]for j in range(4)])
t=np.shape(V)
sum=0
for i in range(t[1]):
    A=V[:,i]
    for j in range(0,i):
        # sum=sum+((np.transpose(V[:,j])*A/(np.transpose(V[:,j])*V[:,j]))*V[:,j])
        d=np.matmul(np.transpose(V[:,j]),V[:,j])
        n=np.matmul(np.transpose(V[:,j]),A)
        sum=sum+(n/d)*V[:,j]
    B=A-sum
    q=np.linalg.norm(B)
    q1=np.true_divide(B, q)
    Q[:,i]=q1
print(Q)
# print(np.matmul(Q[:,0],Q[:,1]))to check orthogonality
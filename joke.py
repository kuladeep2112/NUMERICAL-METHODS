import numpy as np

x=np.array([[1,3,3],[4,5,6],[5,6,7]])
n=len(x)
b=np.zeros(n)
for i in range(n-1, -1, -1):
    print(i)
    for j in range(n-1,i,-1):
        print(j)
        print(x[j])
    print(x[i])

print(b)
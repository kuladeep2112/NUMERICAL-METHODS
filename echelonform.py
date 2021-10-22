import numpy as np
arr = np.array([[1, 2, 3,0], [4, 5, 6,3],[7,8,9,10],[4,5,6,7]])
# arr=np.array([[6.0,2.0,3.0],[4.0,5.0,6.0],[0.0,8.0,9.0]])
#arr =np.array([[1,2,3],[1,9,6],[6,7,8]])

for i in range(len(arr)):

    temp=0
    if i<len(arr)-1:
        for j in range(len(arr)):
            if arr[i+1][0]==0 and temp==0:
                temp=1
                k=0
            elif arr[i+1][0] !=0:
                k=arr[i+1][0]
                temp=1

            p=float(arr[i+1][j]-float((arr[0][j]/arr[0][0])*k))
            arr[i+1][j]=p
for i in range(len(arr)):
     temp=0
     if i<=len(arr)-1 and (i>=len(arr)-2 and len(arr)%2==0) or i<=len(arr)-1 and (i>len(arr)-2 and len(arr)%2!=0):
         for j in range(len(arr)):
            if j<len(arr)-1:
                if arr[i][j+1] ==0 and temp==0:
                    temp=1
                    k=0
                elif arr[i][j+1] !=0:
                    k=arr[i-1][j+1]
                    if temp==0:
                        t=arr[i][j+1]

                    temp=1

                p=float(arr[i-1][j+1]-float((arr[i][j+1]/t)*k))
                arr[i][j+1]=p
for i in range(len(arr)):
    temp=0
    if i==len(arr)-1 and len(arr)==4:
        for j in range(len(arr)):
            if j<len(arr)-2:
                if arr[i][j+2] ==0 and temp==0:
                    temp=1
                    k=0
                elif arr[i][j+2] !=0:
                    k=arr[i-1][j+2]
                    if temp==0:
                        t=arr[i][j+2]

                    temp=1

                p=float(arr[i-1][j+2]-float((arr[i][j+2]/t)*k))
                arr[i][j+2]=p


print(arr)
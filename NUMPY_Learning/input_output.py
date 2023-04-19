import numpy as np
r=int(input("Enter row"))
c=int(input("Enter col"))


tem_mat=[]
for i in range(r):
     single_row = list(map(int, input().split())) 

     tem_mat.append(single_row) 

x=np.array(tem_mat)


print(x)

import numpy as np

linha = int(3)
col = linha+1
matrix = np.array([[0,2,1,6], [4,5,6,8], [9,8,11,9]], dtype=np.longdouble)

#linha = int(3)
#col = linha+1
#matrix = [[3,2,1], [4,5,6], [9,8,11], [11,22,35]]
mat = np.array(matrix[:, :-1], dtype=np.longdouble)

print(matrix, "\n")
print(mat)
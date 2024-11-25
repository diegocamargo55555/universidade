import numpy as np

def print_matriz(linha, col, matrix):
    print("------")
    for row in range(linha):
        for column in range(col):
            print("{:.4f}".format(matrix[row][column]), end=" ")
        print()



#linha = int(input("insira quantas linhas a matrix terá "))
#col = int(input("insira quantas colunas a matrix terá "))
#matrix = []
#print("insira o valor de:")   
#for l in range(linha):    #3 1 4 5
#    a = []
#    for c in range(col):
#        a.append(float(input("A{}{}: " .format(l+1, c+1))))
#    matrix.append(a)
#


# APENAS PARA TESTES
linha = int(3)
col = linha+1
matrix = [[3,2,1,6], [4,5,6,8], [9,8,11,9]]

#linha = int(3)
#col = int(3)
#matrix = [[3,2,1], [4,5,6], [9,8,11], [11,22,35]]

# APENAS PARA TESTES
for i in range(linha-1):
    print("\n\n")
    print_matriz(linha, col, matrix)
    li = 0
    #while li < linha-1:
    for li in range(linha-1):
        print("li:", li)
        l = li + i
        print("i:{}   l:{}".format(i,l+1))
        print(l)
        if l+1 >= linha:
            print("break")
            break
        m = matrix[l+1][i] / matrix[i][i]
        print("m = ", matrix[l+1][i], "/",matrix[i][i] , "\nm: ",m)

        for c in range(col):
            print("A{}{} = {} - {}*{}".format(l+1, c, matrix[l+1][c], m ,matrix[i][c]))
            matrix[l+1][c] = matrix[l+1][c] - m*matrix[i][c]
        
        print_matriz(linha, col, matrix)

x = np.zeros(linha)

x[linha-1] = matrix[linha-1][linha]/matrix[linha-1][linha-1]
print("\n\n\n")
print(x[linha-1])

for i in range(linha-2,-1,-1):
    x[i] = matrix[i][linha]

    for j in range(i+1,linha):
        x[i] = x[i] - matrix[i][j]*x[j]

    x[i] = x[i]/matrix[i][i]
    print(x[i])


print('\nRequired solution is: ')
for i in range(linha):
    print('X%d = %0.2f' %(i,x[i]), end = '\t')





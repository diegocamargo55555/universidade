import numpy as np

def print_matriz(linha, col, matrix):
    print("------")
    for l in range(linha):
        for c in range(col):
            print("{:.4f}".format(matrix[l][c]), end=" ")
        print()
        
def main():


    linha = int(input("insira quantas linhas a matrix terá "))
    col = linha+1
    matrix = []
    print("insira o valor de:")   
    for l in range(linha):    #3 1 4 5
        a = []
        for c in range(col):
            a.append(float(input("A{}{}: " .format(l+1, c+1))))
        matrix.append(a)
    
    matrix = np.array(matrix, dtype=np.longdouble)
    
    # APENAS PARA TESTES
    #linha = int(3)
    #col = linha+1
    #matrix = np.array([[0,2,1,6], [4,5,6,8], [9,8,11,9]], dtype=np.longdouble)
    
    #linha = int(3)
    #col = linha+1
    #matrix = [[3,2,1,9], [4,5,6,1], [9,8,11,15], [11,22,35,55]]

    mat = np.array(matrix[:, :-1], dtype=np.double)
    det = np.linalg.det(mat) 
    print("determinante = ", det)

    if det == 0: 
        print("nao é possivel resolver sistemas de equações lineares co metodo de Gauss")
        return 0
    
    for i in range(linha-1): 
        print("\n\n iteração", i)
        print_matriz(linha, col, matrix)
        li = 0
        #while li < linha-1:
        for li in range(linha-1):
            l = li + i
            if l+1 >= linha:
                print("break")
                break
            
            if matrix[i][i] == 0: #troca linha
                ii = i
                print("troca linhas")
                for _ in range(linha - i):
                    ii += 1
                    if matrix[ii][i] != 0:
                        matrix [[i,ii]] = matrix[[ii,i]]
                        print_matriz(linha, col, matrix)
                        break

            m = matrix[l+1][i] / matrix[i][i]
            print("m = ", matrix[l+1][i], "/",matrix[i][i] , "\nm: ",m)


            for c in range(col):# calcula o novo valor da linha
                print("A{}{} = {} - {}*{} = {}".format(l+1, c, matrix[l+1][c], m ,matrix[i][c], (matrix[l+1][c] - m*matrix[i][c])))
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


    print('\nSolução: ')
    for i in range(linha):
       print('X%d = %0.2f' %(i,x[i]), end = '\t')


main()

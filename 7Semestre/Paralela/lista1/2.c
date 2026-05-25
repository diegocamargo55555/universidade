/*
2. Identifique o que o código a seguir faz. Identifique qual técnica de otimização de uso de memória
está sendo utilizada. Se possível deixe o código mais legível usando comandos do OpenMP.
*/

#include <stdio.h>
#include <stdlib.h>
#include <omp.h>
// O tamanho da matriz deve ser idealmente múltiplo do tamanho do bloco
#define N 1024
#define BLOCK_SIZE 64 // Tamanho do bloco (ajustável conforme o tamanho do cache L1/L2)
void inicializar_matrizes(double **A, double **B, double **C)
{
    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < N; j++)
        {
            A[i][j] = 1.0;
            B[i][j] = 2.0;
            C[i][j] = 0;
        }
    }
}
int main()
{
    // Alocação dinâmica para evitar estouro de pilha (Stack Overflow)
    double **A = (double **)malloc(N * sizeof(double *));
    double **B = (double **)malloc(N * sizeof(double *));
    double **C = (double **)malloc(N * sizeof(double *));
    for (int i = 0; i < N; i++)
    {
        A[i] = (double *)malloc(N * sizeof(double));
        B[i] = (double *)malloc(N * sizeof(double));
        C[i] = (double *)malloc(N * sizeof(double));
    }
    inicializar_matrizes(A, B, C);
    double tempo_inicio = omp_get_wtime();
// Paralelização no loop mais externo de blocos
// 'collapse(2)' distribui os blocos de i e j entre as threads do OpenMP
#pragma omp parallel for collapse(2) schedule(static)
    for (int sj = 0; sj < N; sj += BLOCK_SIZE)
    {
        for (int si = 0; si < N; si += BLOCK_SIZE)
        {
            for (int sk = 0; sk < N; sk += BLOCK_SIZE)
            {

                // Multiplicação tradicional aplicada apenas dentro do bloco atual
                for (int i = si; i < si + BLOCK_SIZE; i++)
                {
                    for (int k = sk; k < sk + BLOCK_SIZE; k++)
                    {
                        // Variável auxiliar para carregar A[i][k] em um registrador
                        double r = A[i][k];
                        for (int j = sj; j < sj + BLOCK_SIZE; j++)
                        {
                            C[i][j] += r * B[k][j];
                        }
                    }
                }
            }
        }
    }
    double tempo_fim = omp_get_wtime();
    printf("Multiplicação de Matriz (%dx%d) com Blocking finalizada.\n", N, N);
    printf("Tamanho do bloco: %dx%d\n", BLOCK_SIZE, BLOCK_SIZE);
    printf("Tempo de execução: %f segundos\n", tempo_fim - tempo_inicio);
    // Validação simples do resultado (Esperado em cada posição de C: N * 1.0 * 2.0 = 2048.0)
    printf("Resultado na posição C[0][0]: %f (Esperado: %f)\n", C[0][0], (double)N * 2.0);
    // Liberação de memória
    for (int i = 0; i < N; i++)
    {
        free(A[i]);
        free(B[i]);
        free(C[i]);
    }
    free(A);
    free(B);
    free(C);
    return 0;
}
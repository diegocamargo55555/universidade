#include <stdio.h>
#include <stdlib.h>
#include <omp.h>
#define N 50000000 // 50 milhões de elementos para justificar o uso da GPU
int main()
{
    double tempo_inicio, tempo_fim;
    double *A = (double *)malloc(N * sizeof(double));
    double *B = (double *)malloc(N * sizeof(double));
    double *C = (double *)malloc(N * sizeof(double));
    if (A == NULL || B == NULL || C == NULL)
    {
        printf("Erro ao alocar memória.\n");
        return 1;
    }
    for (int i = 0; i < N; i++)
    {
        A[i] = 1.5;
        B[i] = 2.5;
        C[i] = 0.0;
    }
    tempo_inicio = omp_get_wtime();
    // soma de vetores via offloading gpu

    /* antigo
    #pragma omp target teams distribute parallel for simd
        for (int i = 0; i < N; i++)
        {
            C[i] = A[i] + B[i];
        }
    */
    // certo
#pragma omp target data map(to : A[0 : N]) map(to : B[0 : N]) map(from : C[0 : N])
#pragma omp teams distribute parallel for simd
    for (int i = 0; i < N; i++)
    {
        C[i] = A[i] + B[i];
    }

    tempo_fim = omp_get_wtime();
    printf("Soma de vetores com Offloading concluída.\n");
    printf("Tempo total (incluindo transferência de dados): %f segundos\n", tempo_fim - tempo_inicio);
    printf("Resultado na posição C[0]: %f\n", C[0]);
    printf("Resultado na posição C[%d]: %f\n", N - 1, C[N - 1]);
    free(A);
    free(B);
    free(C);
    return 0;
}
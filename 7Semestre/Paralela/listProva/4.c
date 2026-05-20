#include <stdio.h>
#include <stdlib.h>
#include <omp.h>

#define N 10000000 // 10 milhões de elementos

// resposta: vetorizacao da funcao
#pragma omp declare simd
double soma(double a, double b)
{
    return a + b;
}

int main()
{
    double tempo_inicio, tempo_fim;

    // Alocação de memória alinhada (64 bytes) para otimizar o carregamento nos registradores AVX-512/AVX2
    // Se o seu compilador não suportar aligned_alloc, use malloc tradicional.
    double *A = (double *)aligned_alloc(64, N * sizeof(double));
    double *B = (double *)aligned_alloc(64, N * sizeof(double));
    double *C = (double *)aligned_alloc(64, N * sizeof(double));

    if (A == NULL || B == NULL || C == NULL)
    {
        printf("Erro ao alocar memória.\n");
        return 1;
    }

    // Inicialização dos vetores
    for (int i = 0; i < N; i++)
    {
        A[i] = 1.0;
        B[i] = 2.0;
        C[i] = 0.0;
    }

    tempo_inicio = omp_get_wtime();

// Diretiva SIMD pura do OpenMP
// 'simdlen(8)' sugere ao compilador processar 8 elementos por vez (ideal para AVX-512 com double)
// 'aligned(A, B, C : 64)' avisa ao compilador que os ponteiros estão alinhados em 64 bytes
#pragma omp simd simdlen(8) aligned(A, B, C : 64)
    for (int i = 0; i < N; i++)
    {
        C[i] = soma(A[i], B[i]);
    }

    tempo_fim = omp_get_wtime();

    printf("Soma de vetores finalizada.\n");
    printf("Tempo de execução (SIMD): %f segundos\n", tempo_fim - tempo_inicio);

    // Validação simples
    printf("Resultado na posição C[0]: %f (Esperado: 3.00)\n", C[0]);

    // Liberação da memória
    free(A);
    free(B);
    free(C);

    return 0;
}
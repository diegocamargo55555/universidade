/*
1) Determine no código abaixo o que está prejudicando o seu desempenho (tempo de execução) e
sugira melhorias.
*/

#include <stdio.h>
#include <omp.h>
#define MAX_THREADS 4
#define ITERACOES 100000000
int main() {
    long long passos[MAX_THREADS] = {0};
    double tempo_inicio, tempo_fim;
    omp_set_num_threads(MAX_THREADS);
    tempo_inicio = omp_get_wtime();
    #pragma omp parallel
    {
        int id_thread = omp_get_thread_num();
        for (long long i = 0; i < ITERACOES; i++) {
            passos[id_thread]++;
        }
    }
    tempo_fim = omp_get_wtime();
    printf("Tempo de execução: %f segundos\n", tempo_fim - tempo_inicio);
    return 0;
}
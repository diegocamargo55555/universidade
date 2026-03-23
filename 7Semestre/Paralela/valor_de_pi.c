#include <omp.h>
#include <stdio.h>

#define NUM_PASSOS 100000
#define MAX_THREADS 32

int main() {
    double largura_passo = 1.0 / (double)NUM_PASSOS;
    double resultados_parciais[MAX_THREADS];
    double pi = 0.0;
    int nthreads_real;

    for (int i = 0; i < MAX_THREADS; i++) {
        resultados_parciais[i] = 0.0;
    }

    #pragma omp parallel
    {
        int id = omp_get_thread_num();
        int nthreads = omp_get_num_threads();
        
        if (id == 0) nthreads_real = nthreads;

        int carga = (NUM_PASSOS + (nthreads - 1)) / nthreads;
        int inicio = id * carga;
        int fim = (inicio + carga < NUM_PASSOS) ? (inicio + carga) : NUM_PASSOS;

        double soma_local = 0.0;
        double x;

        for (int i = inicio; i < fim; i++) {
            x = (i + 0.5) * largura_passo;
            soma_local += 4.0 / (1.0 + x * x);
        }

        resultados_parciais[id] = soma_local;

        printf("Thread %d: inicio=%d, fim=%d, soma_local=%f\n", id, inicio, fim, soma_local);
    }

    for (int i = 0; i < nthreads_real; i++) {
        pi += resultados_parciais[i];
    }

    pi *= largura_passo;

    printf("\nValor aproximado de Pi: %f\n", pi);

    return 0;
}
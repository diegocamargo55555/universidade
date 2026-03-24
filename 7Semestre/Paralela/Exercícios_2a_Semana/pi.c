#include <omp.h>
#include <stdio.h>

#define NUM_PASSOS 100000

int main() {
    double largura_passo = 1.0 / (double)NUM_PASSOS;
    double pi = 0.0;

    #pragma omp parallel for reduction(+:pi)
    for (int i = 0; i < NUM_PASSOS; i++) {
        double x = (i + 0.5) * largura_passo;
        pi += 4.0 / (1.0 + x * x);
    }

    pi *= largura_passo;

    printf("\nValor aproximado de Pi: %f\n", pi);

    return 0;
}
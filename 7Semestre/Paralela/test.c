#include <omp.h>
#include <stdio.h>

int main() {
    long interpolação = 100000;
    double largura_passo = 1.0 / (double) interpolação;;
    double x, pi, soma = 0.0;
    double tempo_inicio, tempo_fim;

    #pragma omp parallel for reduction(+:soma) private(x)

    for (int i = 0; i < interpolação; i++) {
        // f(x) = 4 / (1 + x^2)
        x = (i + 0.5) * largura_passo;       
        soma = soma + 4.0 / (1.0 + x * x);
    }

    pi = largura_passo * soma;
    printf("Valor aproximado de Pi: %f\n", pi);
    return 0;
}






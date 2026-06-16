#include <stdio.h>
#include <omp.h>

int main() {
    long num_passos = 100000; // Cem mil pontos de interpolação
    double passo;
    double x, soma = 0.0, pi;
    double tempo_inicio, tempo_fim, tempo_total_ms;

    passo = 1.0 / (double) num_passos;

    // Inicializa a contagem de tempo
    tempo_inicio = omp_get_wtime();

    // Paralelização com OpenMP
    #pragma omp parallel for private(x) reduction(+:soma)
    for (long i = 0; i < num_passos; i++) {
        x = (i + 0.5) * passo; // Ponto médio do retângulo
        soma = soma + 4.0 / (1.0 + x * x);
    }

    pi = passo * soma;
    tempo_fim = omp_get_wtime();

    // Calcula o tempo total e converte para milissegundos
    tempo_total_ms = (tempo_fim - tempo_inicio) * 1000.0;

    printf("Valor aproximado de Pi: %.15f\n", pi);
    printf("Tempo de execução: %.3f ms\n", tempo_total_ms);

    return 0;
}
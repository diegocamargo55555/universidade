#include <stdio.h>
#include <omp.h>

#define NUM_PASSOS 100000000 
#define NUM_PONTOS 100000000 
#define M 2147483647L        
#define A 48271L            

void calcular_pi_integracao() {
    double x, soma = 0.0;
    double passo = 1.0 / (double)NUM_PASSOS;

    #pragma omp target teams distribute parallel for reduction(+:soma) map(tofrom: soma)
    for (int i = 0; i < NUM_PASSOS; i++) {
        double x = (i + 0.5) * passo;
        soma += 4.0 / (1.0 + x * x);
    }

    double pi = passo * soma;
    printf("[Integração] Valor de Pi: %.10f\n", pi);
}

void calcular_pi_monte_carlo() {
    int dentro_do_circulo = 0;

    #pragma omp target teams distribute parallel for reduction(+:dentro_do_circulo) map(tofrom: dentro_do_circulo)
    for (int i = 0; i < NUM_PONTOS; i++) {
        unsigned int x_seed = (A * i) % M;
        unsigned int y_seed = (A * x_seed) % M;

        double x = (double)x_seed / M;
        double y = (double)y_seed / M;

        if (x * x + y * y <= 1.0) {
            dentro_do_circulo++;
        }
    }

    double pi = 4.0 * (double)dentro_do_circulo / NUM_PONTOS;
    printf("[Monte Carlo] Valor de Pi: %.10f\n", pi);
}

int main() {
    int num_devices = omp_get_num_devices();
    if (num_devices > 0) {
        printf("Acelerador encontrado! Utilizando %d dispositivo(s).\n\n", num_devices);
    } else {
        printf("Nenhum acelerador encontrado. Rodando no Host (CPU).\n\n");
    }

    double inicio = omp_get_wtime();
    calcular_pi_integracao();
    double fim = omp_get_wtime();
    printf("Tempo Integração: %.4f segundos\n\n", fim - inicio);

    inicio = omp_get_wtime();
    calcular_pi_monte_carlo();
    fim = omp_get_wtime();
    printf("Tempo Monte Carlo: %.4f segundos\n", fim - inicio);

    return 0;
}
#include <stdio.h>
#include <omp.h>
#include <math.h>

#define M 2147483647L // (2^31) - 1
#define A 48271L
#define C 0L
#define NUM_PONTOS 1000000
#define NUM_THREADS 8

long proximo_valor(long atual) {
    return (A * atual + C) % M;
}

long pot_mod(long base, int exp) {
    long res = 1;
    base %= M;
    while (exp > 0) {
        if (exp % 2 == 1) res = (__int128)res * base % M;
        base = (__int128)base * base % M;
        exp /= 2;
    }
    return res;
}

void monte_carlo_pi(int modo) {
    int pontos_no_circulo = 0;
    const char* tecnica = (modo == 0) ? "Leapfrog" : "Leapfrog Modificado";

    long a_salto = pot_mod(A, NUM_THREADS);

    #pragma omp parallel num_threads(NUM_THREADS) reduction(+:pontos_no_circulo)
    {
        int id = omp_get_thread_num();
        long x_seed, y_seed;

        if (modo == 0) {
            x_seed = 12345; 
            y_seed = 67890;
            for (int i = 0; i < id; i++) {
                x_seed = proximo_valor(x_seed);
                y_seed = proximo_valor(y_seed);
            }
        } else {
            x_seed = 12345;
            y_seed = 67890;
            int saltos = id * (NUM_PONTOS / NUM_THREADS);
            long a_bloco = pot_mod(A, saltos);
            x_seed = ((__int128)x_seed * a_bloco) % M;
            y_seed = ((__int128)y_seed * a_bloco) % M;
        }

        int pontos_por_thread = NUM_PONTOS / NUM_THREADS;
        for (int i = 0; i < pontos_por_thread; i++) {
            double x = (double)x_seed / M;
            double y = (double)y_seed / M;

            if (x * x + y * y <= 1.0) {
                pontos_no_circulo++;
            }

            if (modo == 0) {
                x_seed = ((__int128)x_seed * a_salto) % M;
                y_seed = ((__int128)y_seed * a_salto) % M;
            } else {
                x_seed = proximo_valor(x_seed);
                y_seed = proximo_valor(y_seed);
            }
        }
    }

    double pi = 4.0 * (double)pontos_no_circulo / NUM_PONTOS;
    printf("[%s] Valor de Pi: %.10f\n", tecnica, pi);
}

int main() {
    printf("Calculando Pi com %d pontos e %d threads...\n\n", NUM_PONTOS, NUM_THREADS);
    
    monte_carlo_pi(0); 
    monte_carlo_pi(1); 

    return 0;
}
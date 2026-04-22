#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <math.h>
#include <omp.h>

#define CASAS 100

int main() {
    bool primos[CASAS + 1];

    #pragma omp parallel for
    for (int i = 0; i <= CASAS; i++) {
        primos[i] = true;
    }

    primos[0] = false;
    primos[1] = false;

    int raiz = sqrt(CASAS);

    for (int p = 2; p <= raiz; p++) {
        if (primos[p] == true) {
            #pragma omp parallel for
            for (int i = p * p; i <= CASAS; i += p) {
                primos[i] = false;
            }
        }
    }

    printf("Numeros primos de 1 a 100:\n");
    int count = 0;
    for (int p = 2; p <= CASAS; p++) {
        if (primos[p]) {
            printf("%d ", p);
            count++;
        }
    }
    
    printf("\n\nTotal de numeros primos encontrados: %d\n", count);

    return 0;
}
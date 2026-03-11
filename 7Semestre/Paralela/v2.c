#include <omp.h>
#include <stdio.h>
#define tamanho 100

int main(){
    int a[tamanho], b[tamanho], c[tamanho];
    for (int i = 0; i < tamanho; i++)
    {
        a[i] = i;
    }
    
    int resultado = 0;
    for (int i = 0; i < tamanho; i++)
    {
        resultado += a[i];
    }
    
    
    printf("acumulado = %d\n ", resultado);
}
#include <omp.h>
#include <stdio.h>
#define tamanho 100

int main(){
    int a[tamanho], b[tamanho], c[tamanho];
    for (int i = 0; i < tamanho; i++)
    {
        a[i] = i;
        b[i] = 2*i;
    }
    
    for (int i = 0; i < tamanho; i++)
    {
        c[i] = a[i] + b[i];
    }
    
    
    for (int i = 0; i < tamanho; i++)
    {
        printf("%d ", c[i]);
    }
    printf("\n");
}
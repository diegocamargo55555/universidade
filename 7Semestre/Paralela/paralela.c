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
    
    #pragma omp parallel 
    {
        int nthreads = omp_get_num_threads();
        int carga = tamanho  + (nthreads -1) / nthreads;

        int id = omp_get_thread_num();
        int inicio = id * carga;
        int fim = (inicio + carga) < tamanho ? inicio + carga : tamanho;
        
        for (int i = inicio; i < fim; i++)
        {
            c[i] = a[i] + b[i];
        }
    }
    
    for (int i = 0; i < tamanho; i++)
    {
        printf("%d ", c[i]);
    }
    printf("\n");
}
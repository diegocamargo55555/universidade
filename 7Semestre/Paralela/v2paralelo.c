#include <omp.h>
#include <stdio.h>

#define tamanho 100
#define max_threads 32

int main(){
    int a[tamanho], b[tamanho], c[tamanho];
    int resultado = 0;
    int resultados_paraciais[max_threads];
    int nthreads;

    for (int i = 0; i < tamanho; i++)
    {
        a[i] = i;
    }

    #pragma omp parallel 
    {
        nthreads = omp_get_max_threads();
        int carga = (tamanho  + (nthreads -1)) / nthreads;
        int id = omp_get_thread_num();
        int inicio = id * carga;
        int fim = ((inicio + carga) < tamanho) ? inicio + carga : tamanho;
        resultados_paraciais[id] = 0;
        int resultado_temp = 0;
        for (int i = 0; i < fim; i++)
        {
            resultado_temp += a[i];
        }        
        resultados_paraciais[id] += resultado_temp;

        printf("id:%d \n fim%d    inicio%d    resultado%d",  id, fim, inicio, resultados_paraciais[id]);

    }

    for (int i = 0; i < nthreads; i++)
    {
        resultado += resultados_paraciais[i];
    }   
    printf("\nacumulado = %d\n ", resultado);
}
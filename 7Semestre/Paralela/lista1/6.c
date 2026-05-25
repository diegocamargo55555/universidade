/*
1 o conceito envolvido é dependencia de tarefas, ela é importante pois a descrição do paralelismo é 
mais simples(em termos de dependencias)
2 Menor retencao das tarefas (maior paralelismo entre as tarefas).
*/

#include <stdio.h>
#include <stdlib.h>
#include <omp.h>
#include <unistd.h> // Para a função sleep()
int main()
{
    int x = 0;
    int y = 0;
    printf("[Main] Iniciando região paralela...\n");
    #pragma omp parallel
    {
        #pragma omp single
        {
            #pragma omp task depend(out : x)
            {
                printf("[Thread %d] Tarefa A: Gerando valor para X...\n", omp_get_thread_num());
                sleep(2); // Simula um cálculo demorado
                x = 10;
                printf("[Thread %d] Tarefa A: Concluída! X = %d\n", omp_get_thread_num(), x);
            }
            #pragma omp task depend(in : x) depend(out : y)
            {
                printf("[Thread %d] Tarefa B: Calculando quadrado de Y...\n", omp_get_thread_num());
                y = x * x;
                printf("[Thread %d] Tarefa B: Concluída! Y = %d\n", omp_get_thread_num(), y);
            }
            #pragma omp task depend(in : y)
            {
                printf("[Thread %d] Tarefa C: Imprimindo resultado final...\n", omp_get_thread_num());
                printf("[Resultado Final] O quadrado de %d é %d\n", x, y);
            }
        }
    }

    return 0;
}
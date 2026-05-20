#include <stdio.h>
#include <stdlib.h>
#include <omp.h>

// Definição da estrutura do nó da árvore
typedef struct No
{
    int dado;
    struct No *esquerda;
    struct No *direita;
} No;

// Função auxiliar para criar um novo nó
No *criar_no(int dado)
{
    No *novo = (No *)malloc(sizeof(No));
    novo->dado = dado;
    novo->esquerda = NULL;
    novo->direita = NULL;
    return novo;
}

// Função para construir uma árvore binária balanceada de forma simples
No *construir_arvore(int altura)
{
    if (altura <= 0)
        return NULL;
    // Cada nó recebe o valor 1 para facilitar a checagem da soma total
    No *raiz = criar_no(1);
    raiz->esquerda = construir_arvore(altura - 1);
    raiz->direita = construir_arvore(altura - 1);
    return raiz;
}

// NOVA FUNÇÃO: Processamento sequencial puro para evitar overhead de tasks em subárvores pequenas
int somar_arvore_seq(No *raiz)
{
    if (raiz == NULL)
        return 0;
    return raiz->dado + somar_arvore_seq(raiz->esquerda) + somar_arvore_seq(raiz->direita);
}

// Função recursiva que usa tarefas OpenMP para somar os nós
// OTIMIZAÇÃO: Recebe a 'profundidade' para controlar a recursão
int somar_arvore_tasks(No *raiz, int profundidade)
{
    if (raiz == NULL)
        return 0;

    // Lida com a recursão: se a árvore já foi dividida o suficiente (ex: profundidade > 6),
    // resolvemos o resto da subárvore sequencialmente, sem criar novas tarefas OpenMP.
    if (profundidade > 6)
    {
        return somar_arvore_seq(raiz);
    }

    int soma_esq = 0;
    int soma_dir = 0;

// Criamos uma tarefa independente para processar a subárvore esquerda
#pragma omp task shared(soma_esq)
    {
        soma_esq = somar_arvore_tasks(raiz->esquerda, profundidade + 1);
    }

// Criamos outra tarefa independente para processar a subárvore direita
#pragma omp task shared(soma_dir)
    {
        soma_dir = somar_arvore_tasks(raiz->direita, profundidade + 1);
    }

// Barreira local: espera que as duas sub-tarefas acima terminem
// antes de somar os resultados neste nível da recursão
#pragma omp taskwait

    return raiz->dado + soma_esq + soma_dir;
}

// Função auxiliar para liberar a memória da árvore
void liberar_arvore(No *raiz)
{
    if (raiz == NULL)
        return;
    liberar_arvore(raiz->esquerda);
    liberar_arvore(raiz->direita);
    free(raiz);
}

int main()
{
    int altura_arvore = 15; // Uma árvore de altura 15 terá (2^15 - 1) = 32767 nós
    int total_nos_esperado = (1 << altura_arvore) - 1;
    printf("Construindo árvore binária com altura %d (%d nós)...\n", altura_arvore, total_nos_esperado);
    No *raiz = construir_arvore(altura_arvore);
    int soma_total = 0;
    double tempo_inicio = omp_get_wtime();

// O paralelismo de tarefas exige uma região paralela com apenas UMA thread master/single
// para disparar a primeira tarefa raiz. As outras threads pegam o trabalho da fila.
#pragma omp parallel
    {
#pragma omp single
        {
            // OTIMIZAÇÃO: Começa a recursão com profundidade 0
            soma_total = somar_arvore_tasks(raiz, 0);
        }
    }
    double tempo_fim = omp_get_wtime();

    printf("\n--- Resultado da Avaliação ---\n");
    printf("Soma total calculada: %d\n", soma_total);
    printf("Soma total esperada: %d\n", total_nos_esperado);
    printf("Tempo de execução: %f segundos\n", tempo_fim - tempo_inicio);

    liberar_arvore(raiz);
    return 0;
}
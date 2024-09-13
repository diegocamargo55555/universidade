#include <iostream>

struct fila {
    int info;
    int prior;
    fila *link;
};

fila *inicializaFP(fila *L)
{
    L = nullptr;
    return L;
}

fila *insereFP(fila *L, int valor, int prior)
{
    fila *N, *P, *ANT;

    N = new fila;
    N->info = valor;
    N->prior = prior;

    if (L == nullptr) {
        L = N;
        N->link = nullptr;
    }
    else {
        P = L;

        while ((P != nullptr) && (prior >= P->prior)) {
            ANT = P;
            P = P->link;
        }
        if (P == L) {
            N->link = L;
            L = N;
        }
        else {
            ANT->link = N;
            N->link = P;
        }
    }
    return L;
}

fila *removeFP(fila *L, int *n, int * prior) {
	fila *AUX;

	if (L != nullptr) {
		*n = L->info;
		*prior = L->prior; 
		AUX = L;
		L = L->link;
		delete AUX;
	}
	return L;
}

int verificaSeVazia(fila *L) {
	if (L == nullptr)
		return 1;
	else
		return 0;
}


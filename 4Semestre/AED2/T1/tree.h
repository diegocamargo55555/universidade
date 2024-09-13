#include <iostream>
using namespace std;

struct no {
	int info;
	no *Llink;
	no *Rlink;
	
};

no *ini_AB(no *T) {
	return nullptr;
}

no *novoNo_AB(no *T, int x) {
	T = new no;
	if (T != nullptr) {
		T->info = x;
		T->Llink = nullptr;
		T->Rlink = nullptr;
	}
	return T;
}

no *insere_AB(no *T, int x) {
	if (T == nullptr){
		T = novoNo_AB(T,x);
		return T;
	}
	else {
		if (x < T->info){ 
			T->Llink = insere_AB(T->Llink, x);
		}
		else {	 
				T->Rlink = insere_AB(T->Rlink, x);
		}
		return T;
	}
}



struct fila {
    int info;
    int prior;
    fila *link;
};

void exibe(fila *L)
{
    fila *P = L;

	for (int i = 0; P != NULL; i++)
	{
		while (P->prior == i)
		{
			printf("nivel: %i  valor: %i \t",P->prior, P->info);
        	P = P->link;
		}
		cout << endl;
	}
}

fila *inicializaFP(fila *L)
{
    L = nullptr;
    return L;
}

fila *insereFP(fila *L, int info, int prior)
{
    fila *N, *P, *ANT;

    N = new fila;
    N->info = info;
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

fila *removeFP(fila *L, int n, int * prior) {
	fila *AUX;

	if (L != nullptr) {
		n = L->info;
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

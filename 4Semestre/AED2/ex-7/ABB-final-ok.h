/*
 * ABB.h
 */

#include <cstddef>
#include <iostream>
using namespace std;

typedef struct TreeNo
{
	int info;
	struct TreeNo *Llink;
	struct TreeNo *Rlink;
} no;

no *ini_AB(no *T)
{
	return nullptr;
}

// insere NO
no *insere_AB(no *T, int x)
{
	if (T == nullptr)
	{
		T = (no *)malloc(sizeof(no));
		T->info = x;
		T->Llink = nullptr;
		T->Rlink = nullptr;
		return T;
	}
	else
	{
		if (x < T->info)
			T->Llink = insere_AB(T->Llink, x);
		else
		{
			T->Rlink = insere_AB(T->Rlink, x);
		}
		return T;
	}
}

// percurso EMORDEM
void emOrdem_AB(no *T)
{
	if (T != nullptr)
	{
		emOrdem_AB(T->Llink);
		cout << T->info << " ";
		emOrdem_AB(T->Rlink);
	}
}

// percurso PREORDEM
void preOrdem_AB(no *T)
{
	if (T != nullptr)
	{
		cout << T->info << " ";
		preOrdem_AB(T->Llink);
		preOrdem_AB(T->Rlink);
	}
}

// percurso POSORDEM
void posOrdem_AB(no *T)
{
	if (T != nullptr)
	{
		posOrdem_AB(T->Llink);
		posOrdem_AB(T->Rlink);
		cout << T->info << " ";
	}
}

// percurso EM LARGURA (por nivel)
void mostraPorNivel(no *T, int nivel, int prox_nivel)
{
	if (T == nullptr)
		return;
	if (nivel == prox_nivel)
	{
		cout << T->info << " - ";
	}
	else if (nivel < prox_nivel)
	{
		mostraPorNivel(T->Llink, nivel + 1, prox_nivel);
		mostraPorNivel(T->Rlink, nivel + 1, prox_nivel);
	}
}

// retorna altura da arvore

// conta nro de NOS da arvore binaria (versao 1)
int conta_AB(no *T, int x)
{
	if (T != nullptr)
	{
		x++;
		x = conta_AB(T->Llink, x);
		x = conta_AB(T->Rlink, x);
	}
	return x;
}

/* conta nro de NOS da arvore binaria (versao 2)
void conta_AB(no *T, int *x) {
	if(T != nullptr) {
		(*x)++;
		conta_AB(T->Llink, x);
		conta_AB(T->Rlink, x);
	}
} */

// apaga NOS da árvore e libera a memoria
no *apaga_AB(no *T)
{
	no *p;
	if (T != nullptr)
	{
		apaga_AB(T->Llink);
		apaga_AB(T->Rlink);
		printf("apagando - %d - ", T->info);
		p = T;
		delete p;
		T = nullptr;
	}
	return T;
}

// retorna endereço do MAIOR NO da arvore
no *maior_AB(no *T)
{
	no *p;
	if (T != nullptr)
	{
		while (T->Rlink != nullptr)
		{
			T = T->Rlink;
		}
		return T;
	}
	else
		return nullptr;
}

/* retorna endereço do MAIOR NO da arvore (versao recursiva)
no *maior_AB(no *T) {
	no *p;
	if (T != nullptr){
		if(T->Rlink != nullptr)
			p = maior_AB(T->Rlink);
		else
			p=T;
		return p;
	}
}*/

// retorna endereço do MENOR NO da arvore
no *menor_AB(no *T)
{
	no *p;
	if (T != nullptr)
	{
		while (T->Llink != nullptr)
		{
			T = T->Llink;
		}
		return T;
	}
	else
		return nullptr;
}

// remove NO da arvore
no *remove_AB(no *T, int x)
{
	no *p;

	if (T == nullptr)
	{
		return nullptr;
	}
	else
	{
		if (x < T->info)
			T->Llink = remove_AB(T->Llink, x);
		else
		{
			if (x > T->info)
				T->Rlink = remove_AB(T->Rlink, x);
			else
			{
				// no folha
				if ((T->Llink == nullptr) && (T->Rlink == nullptr))
				{
					p = T;
					free(p);
					T = nullptr;
					return T;
				}
				else
				{
					// so tem o filho da direita
					if (T->Llink == nullptr)
					{
						p = T;
						T = T->Rlink;
						free(p);
						return T;
					}
					else
					{
						// so tem o filho da esquerda
						if (T->Rlink == nullptr)
						{
							p = T;
							T = T->Llink;
							free(p);
							return T;
						}
						else
						{
							// NO tem 2 filhos
							p = maior_AB(T->Llink);
							T->info = p->info;
							T->Llink = remove_AB(T->Llink, p->info);
						}
					}
				}
			}
		}
		return T;
	}
}

// rotacao a Direita do NO p
no *rodaDireita(no *p)
{
	no *temp, *q;
	q = p->Llink;
	temp = q->Rlink;
	q->Rlink = p;
	p->Llink = temp;
	return q;
}

// rotacao a Direita do NO com valor igual a x
no *rodaDir(no *T, int x)
{
	if (T == nullptr)
	{
		return nullptr;
	}
	else
	{
		if (x < T->info)
			T->Llink = rodaDir(T->Llink, x);
		else
		{
			if (x > T->info)
				T->Rlink = rodaDir(T->Rlink, x);
			else
			{
				no *temp, *q;
				q = T->Llink;
				temp = q->Rlink;
				q->Rlink = T;
				T->Llink = temp;
				return q;
			}
		}
		return T;
	}
}

// busca NO na arvore e retorna o endereco do NO se encontrar
no *busca(no *T, int x)
{
	no *p;
	if (T == nullptr)
	{
		return nullptr;
	}
	else
	{
		if (T->info == x)
			return T;
		else
		{
			if (x < T->info)
			{
				p = (busca(T->Llink, x));
				return p;
			}
			else
			{
				p = (busca(T->Rlink, x));
				return p;
			}
		}
	}
}

no *imprime_PAI_rec(no *T, int x)
{
	no *p;
	if (T == nullptr)
	{
		return nullptr;
	}
	else
	{
		if (T->info == x)
			return T;
		else
		{
			if (x < T->info)
			{
				p = (imprime_PAI_rec(T->Llink, x));
				if (T->Llink->info == x)
					cout << "PAI:" << T->info;
				return p;
			}
			else
			{
				p = (imprime_PAI_rec(T->Rlink, x));
				if (T->Rlink->info == x)
					cout << "PAI:" << T->info << " \n";
				return p;
			}
		}
	}
}

void imprime_PAI(no *T, int x)
{
	no *p = nullptr;
	while ((T != nullptr) && (T->info != x))
	{
		p = T;
		if (x < T->info)
			T = T->Llink;
		else
			T = T->Rlink;
	}
	if ((T != nullptr) && (p != nullptr))
		cout << " \nPAI: " << p->info << " \n";
}

void imp2filhos(no *T)
{
	if (T != nullptr)
	{
		imp2filhos(T->Llink);
		imp2filhos(T->Rlink);
		if ((T->Llink != nullptr) && (T->Rlink != nullptr))
			cout << T->info;
	}
}


void sum_all(no *T, int *sum)
{

	if (T != nullptr)
	{
		*sum = T->info;
		sum_all(T, sum);
	}

}


int sumNodes(no* root) {
    if (root == nullptr) {
        return 0;
    }

    // Soma o valor do nó atual, o total da subárvore esquerda e o total da subárvore direita
    return root->info + sumNodes(root->Llink) + sumNodes(root->Rlink);
}


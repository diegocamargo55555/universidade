#include "tree.h"
#include <cstdio>
#include <vector>
#include <queue>
using namespace std;


void print_nivel(no* t, int i)
{
    int nivel = 0;
    level p;
    p.nivel = 0;


    queue<pair<no*, int> > Fila_2;
    queue<no*> fila;

    fila.push(t);
    Fila_2.push({t, nivel});

    if (t != nullptr) {
        printf("%i\n", t->info);
    }

    while (!fila.empty())
    {
        no* atual = fila.front();
        printf("%i\t", atual->info);
        
        if (atual->Llink != nullptr)
        {
            Fila_2.push({atual->Llink, nivel});
        }
        if (atual->Rlink != nullptr)
        {
            Fila_2.push({atual->Rlink, nivel});
        }

        fila.pop();
    }

        nivel++;
        fila.pop();
        printf("\n");
        if ()
        {
            /* code */
        }
        
    
}


int main(){
    no *t;
    int i = 0;
    t = ini_AB(t);
    vector<int> v;

    t = insere_AB(t, 9);
    t = insere_AB(t, 65);
    t = insere_AB(t, 4);
    t = insere_AB(t, 2);
    t = insere_AB(t, 7);
    t = insere_AB(t, 99);
    t = insere_AB(t, 56);
    t = insere_AB(t, 23);
    t = insere_AB(t, 11);
    t = insere_AB(t, 79);
    t = insere_AB(t, 1);
    t = insere_AB(t, 9);
    print_nivel(t, i);
    //preOrdem_AB(t);
}

#include <iostream>
#include "tree.h"
#include <vector>
#include <queue>
#include <unordered_map>


using namespace std;

int nivel =0 ;

void print_nivel(no* t, int i)
{
    queue<no*> fila;
    fila.push(t);

    while (!fila.empty())
    {
        no* atual = fila.front();
        printf("%i\t", atual->info);
        
        if (atual->Llink != nullptr)
        {
            fila.push(atual->Llink);
        }
        if (atual->Rlink != nullptr)
        {
            fila.push(atual->Rlink);
        }

        fila.pop();
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






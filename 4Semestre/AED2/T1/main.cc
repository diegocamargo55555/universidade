#include <iostream>
#include "tree.h"
#include <queue>


using namespace std;

int nivel =0 ;


fila *asdf(no* t, int nivel, fila *f){
    if (t != nullptr)
    {
        f = insereFP(f, t->info, nivel);

        if(t->Llink != NULL){
            asdf(t->Llink, nivel + 1, f);
        }

        if(t->Rlink != NULL){
            asdf(t->Rlink, nivel + 1, f);
        }
    }
    return f;
}

int main(){
    no *t;
    t = ini_AB(t);
    
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

    fila *f;
    f = inicializaFP(f);
    f = asdf(t, 0, f);
    cout << "test" << endl;
    exibe(f);



}






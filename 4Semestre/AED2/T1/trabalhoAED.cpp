#include <iostream>
#include "ABB.h"
#include "FilaPrioridadesLE.h"
using namespace std;


fila* traversal(no* T, int aux, fila *F){
    if(T != NULL){
        F = insereFP(F, T->info, aux);
        if(T->Llink != NULL){
            cout << "L" << T->Llink->info << endl;
            traversal(T->Llink, aux + 1, F);
        }
        if(T->Rlink != NULL){
            traversal(T->Rlink, aux + 1, F);
        }
    }
    return F;
}
void imprimeTransversal(no *T){
    fila *F;
    F = inicializaFP(F);
    F = traversal(T, 0, F);
    //exibe(F);
}

int main(){
    no *T;
    T = ini_AB(T);
    T = insere_AB(T, 31);
    T = insere_AB(T, 12);
    T = insere_AB(T, 1);
    T = insere_AB(T, 76);
    T = insere_AB(T, 43);
    T = insere_AB(T, 82);
    imprimeTransversal(T);
}
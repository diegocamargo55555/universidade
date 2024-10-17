
#include <stdio.h>

#include <stdlib.h>

#include <iostream>
using namespace std;

#include "ABB-final-ok.h"

int main(void)
{
    no *T, *p;
    int x, c;
    int conta = 0;
    int *sum = 0;
    no *pmaior, *pmenor;

    T = ini_AB(T);

    insere_AB(T, 55);
    insere_AB(T, 32);

    insere_AB(T, 54);

    insere_AB(T, 76);

    insere_AB(T, 11);

    insere_AB(T, 33);

    insere_AB(T, 5);

    insere_AB(T, 8);

    sum_all(T, sum);

    int totalSum = sumNodes(T);
    cout << "Soma de todos os nós: " << totalSum << endl;






}


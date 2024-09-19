#include <iostream>
#include <math.h>
using namespace std;

double moduloDOIS(double a, double b);
double moduloUM(double a);
double funcao(double valor);

int main(){
    double precisao, x1, x0, x2, raiz;
    int k = 0, n;   
    x0 = 0;
    x1 = 1;
    precisao = 0.01;
    n = 100;
    cout << "Qual o valor de x0? ";

    if (moduloUM(funcao(x0)) > precisao)
    {
        if(moduloUM(funcao(x1)) < precisao && moduloDOIS(x1,x0) < precisao){
            raiz = x1;
        }
        else{
            while (moduloUM(funcao(x1)) > precisao && k<n && moduloDOIS(x1,x0) > precisao)
            {
                k++;
                x2 = x1 - (funcao(x1)*(x1-x0))/(funcao(x1) - funcao(x0));
                x0 = x1;
                x1 = x2;
            }
            raiz = x2;
        }
    }
    else{
        raiz = x0;
    }

    cout  << "\nValor final da raiz: " << raiz;
    cout << "\nNumero total de interacoes: " << k;
    cout << "\nx0: " << x0 << "\nx1: " << x1 << "\nx2: " << x2;
}

double moduloUM(double a){
    if (a<0)
    {
        return (a*(-1));
    }
    else{
        return a;
    }
}

double moduloDOIS(double a, double b){
    if (a-b < 0)
    {
        return ((a-b)*(-1));
    }
    else{
        return a-b;
    }
}

double funcao(double valor){
    return(pow(valor, 3.0) - (1.0/2.0));
};
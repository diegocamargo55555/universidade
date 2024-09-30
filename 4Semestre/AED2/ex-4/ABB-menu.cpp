#include <stdio.h>
#include <stdlib.h>

#include <iostream>
using namespace std;

#include "ABB.h"

int main(void)
{
	no *T;

   
	T=ini_AB(T);
   
   
      
	T =  insere_AB(T,15); 
	T =  insere_AB(T,12); 
	T =  insere_AB(T,32); 
	T =  insere_AB(T,41); 
	T =  insere_AB(T,31); 
	T =  insere_AB(T,5); 
	T =  insere_AB(T,8); 
	T =  insere_AB(T,4); 
	T =  insere_AB(T,99); 
	T =  insere_AB(T,87); 
	T =  insere_AB(T,55); 
	T =  insere_AB(T,19); 
	T =  insere_AB(T,0); 

//15,12,32,41,31,5,8,4,99,87,55,19,0


	print_if2_filhos(T);
	  

}

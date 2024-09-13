#include <iostream>
using namespace std;

struct level
{
	no *no;
	int nivel;
};


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



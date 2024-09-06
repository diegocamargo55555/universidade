/*
 * ABB.h
  */

struct no {
	int info;
	no *Llink;
	no *Rlink;
};

no *ini_AB(no *T) {
	return NULL;
}

no *novoNo_AB(no *T, int x) {
	T = new no;
	if (T != NULL) {
		T->info = x;
		T->Llink = NULL;
		T->Rlink = NULL;
	}
	return T;
}

void buscaAB(no *t, int x){
	if (t != nullptr)
	{
		if (x == t->info  )
		{
			//return true;
			cout << "\n\nO valor existe na arvore!\n";
		}	
		else if (x > t->info)
		{
			buscaAB( t->Rlink, x);

		}	
		else if (x < t->info)
		{
			buscaAB( t->Llink, x);
		}	
	}else
	{
		//return false;
		cout << "\nValor nao encontrado nesse nivel.\n";
	}
}



bool buscaAB1(no *t, int x){
	if (t != nullptr)
	{
		if (x == t->info  )
		{
			return true;
		}	
		else if (x > t->info)
		{
			buscaAB1( t->Rlink, x);

		}	
		else if (x < t->info)
		{
			buscaAB1( t->Llink, x);
		}	
	}else
	{
		return false;
	}
}



void existe(no *T, int x){
	no* t = T;
	if(t!= NULL){
		if(x > t->info){
			t = T->Rlink;
			existe(t, x);
		}
		else if(x < t->info){
			t = T->Llink;
			existe(t, x);
		}
		else if(x == t->info){
			cout << "\n\nO valor existe na arvore!\n";
		}
		
	}
	else{
			cout << "\nValor nao encontrado nesse nivel.\n";
	}
}


no *insere_AB(no *T, int x) {
	if (T == NULL){
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

void emOrdem_AB(no *T) {
	if(T != NULL) {
		emOrdem_AB(T->Llink);
		cout << T->info << " ";
		emOrdem_AB(T->Rlink);
	}
}

void preOrdem_AB(no *T) {
	if(T != NULL) {
		cout << T->info << " ";
		preOrdem_AB(T->Llink);
		preOrdem_AB(T->Rlink);
	}
}

void posOrdem_AB(no *T) {
	if(T != NULL) {
		posOrdem_AB(T->Llink);
		posOrdem_AB(T->Rlink);
		cout << T->info << " ";
	}
}

// ** PERCURSO EM LARGURA - TRABALHO AVALIATIVO 1 **

// ** funcao buscaAB - a ser desenvolvida pelo aluno **


enum Pessoa {
  ana('Ana', 25),
  bruno('Bruno', 17),
  carlos('Carlos', 30),
  daniela('Daniela', 18),
  eduardo('Eduardo', 15),
  fernanda('Fernanda', 22);

  final String nome;
  final int idade;

  const Pessoa(this.nome, this.idade);
}
void imprimirMaioresDeIdade() {
  for (var pessoa in Pessoa.values) {
    if (pessoa.idade >= 18) {
      print(pessoa.nome);
    }
  }
}

void main() {
  imprimirMaioresDeIdade();
}
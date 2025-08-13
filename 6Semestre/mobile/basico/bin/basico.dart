import 'package:basico/basico.dart' as basico;

void main(List<String> arguments) {
  saudacoes("Carlos Eduardo", sobrenome: adicionarSobrenome);
}

void adicionarSobrenome(){
  print('Iatskiu');
  
}

void saudacoes(String nome, {required Function sobrenome}){
  print("seja bem vindo: $nome");
  sobrenome();
}

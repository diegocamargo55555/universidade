void main() {
  List<String> frutas = ['Maçã', 'Banana', 'Laranja', 'Morango', 'Uva'];
  print(frutas); // ex 1

  //ex2
  print("terceiro item:" + frutas[2]);

  //ex3
  frutas.add("laranja");
  print(frutas);

  frutas.remove('Maçã');
  print(frutas);

  //ex4
  for (var i = 0; i < frutas.length; i++) {
    print(frutas[i].toUpperCase());
  }

  //ex5
  for (var fruta in frutas) {
    print(fruta.toUpperCase());
  }

  // ex6
  List<String> frutas_A = [];

  for (var fruta in frutas) {
    if (fruta[0] == "a" || fruta[0] == "A") {
      frutas_A.add(fruta);
    }
  }
  print(frutas_A);

  //ex7
  Map<String, double> precosFrutas = {
    'Maçã': 2.50,
    'Banana': 1.80,
    'Laranja': 2.00,
    'Morango': 5.00,
    'Uva': 4.50,
  };
  print(precosFrutas);
  
  
  
}

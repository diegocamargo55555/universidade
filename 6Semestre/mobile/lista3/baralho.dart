import 'carta.dart';

class Baralho {
  List<Card> cartas = [];

  Baralho() {
    for (Naipe naipe in Naipe.values) {
      for (Valor valor in Valor.values) {
        cartas.add(Card(naipe, valor));
      }
    }
  }

  void embaralhar() {
    cartas.shuffle();
    print("\nBaralho embaralhado!\n");
  }

  Card comprar() {
    if (cartas.isEmpty) {
      throw Exception("\nNão há cartas no baralho.\n");
    }
    return cartas.removeLast();
  }
  

  void cartas_restantes() {
    print("cartas restantes: " + cartas.length.toString());
  }
}
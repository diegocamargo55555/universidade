
import 'baralho.dart';
import 'carta.dart';

class Main {
  void main() {
    Baralho deck = Baralho();
    deck.embaralhar();
    print(deck.comprar());
    print(deck.comprar());
    print(deck.comprar());
    deck.cartas_restantes();
  }
}

void main(List<String> args) {
  Main().main();
}
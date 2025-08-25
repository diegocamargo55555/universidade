enum Naipe { copas, ouro, espada, paus }

enum Valor {
  as,
  dois,
  tres,
  quatro,
  cinco,
  seis,
  seven,
  eight,
  nove,
  dez,
  valete,
  dama,
  rei,
}

class Card {
  Naipe naipe;
  Valor valor;

  Card(this.naipe, this.valor);

  String toString() {
    String value;
    switch (valor) {
      case Valor.as:
        value = 'Ás';
      case Valor.dois:
        value = '2';
      case Valor.tres:
        value = '3';
      case Valor.quatro:
        value = '4';
      case Valor.cinco:
        value = '5';
      case Valor.seis:
        value = '6';
      case Valor.seven:
        value = '7';
      case Valor.eight:
        value = '8';
      case Valor.nove:
        value = '9';
      case Valor.dez:
        value = '10';
      case Valor.valete:
        value = 'Valete';
      case Valor.dama:
        value = 'Dama';
      case Valor.rei:
        value = 'Rei';
    }
    String nome = naipe.toString().toString().split('.').last;


    return '$value de $nome';
  }
}

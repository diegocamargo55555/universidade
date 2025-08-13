import 'dart:ffi';

void main(List<String> args) {
  double a, b, c;
  a = 0.5;
  b = 22;
  c = 32;
  print(operacao(a, b));
  
}

double operacao(double a, double b) {
  double c = a == b ? a+b : a*b;
  return c ;
}
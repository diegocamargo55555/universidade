import 'dart:ffi';

void main(List<String> args) {
  
  par_impar (55.5);
}

void par_impar(double n) {
  String value = n % 2 == 0? "par" : "impar";
  print(value);
}


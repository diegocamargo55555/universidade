import 'dart:ffi';

void main(List<String> args) {
  double a, b, c;
  a = 0.5;
  b = 22;
  c = 32;
  var arr = [a,b,c];
  arr.sort();
  var invert = arr.reversed;
  print(invert); 
}
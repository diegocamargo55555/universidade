void main(List<String> args) {
  double n;
  n = 5;
  tabuada(n);
}

void tabuada(double n){
  for (var i = 1; i <= 10; i++) {
    print("$i x $n = ${i*n}");
  }
}
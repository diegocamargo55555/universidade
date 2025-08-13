void main(List<String> args) {
  int n;
  n = 5;
  print(fatorial(n));
}

int fatorial(int n){
  int fat = n;
  for (var i = 1; i < n; i++) {
    fat *= i;
  }
  return fat;
}
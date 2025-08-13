
void main(List<String> args) {
  double a, b, c;
  a = 0.5;
  b = 22;
  c = 32;
  if (Sum(a, b) < c) {
    print("A + B é menor que C");
  }
}

double Sum(double a, double b) {
  return a + b;
}
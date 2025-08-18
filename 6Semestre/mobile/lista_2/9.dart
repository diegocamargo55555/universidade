void main() {
  List<int> list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12];

  var par = list.where((numero) => numero % 2 == 0).toList();

  print(par);
}

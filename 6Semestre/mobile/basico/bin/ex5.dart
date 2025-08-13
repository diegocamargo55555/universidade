void main(List<String> args) {
  int arr = 0;
  for (var i = 1; i < 501; i++) {
    if (i%3 == 0 && i%2 !=0) {
      arr += i;
    }
  }
  
  print(arr);
}
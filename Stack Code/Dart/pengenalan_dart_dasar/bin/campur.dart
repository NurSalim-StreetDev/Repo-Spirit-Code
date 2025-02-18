///ini adalah file untuk latihan berbagai block
void main() {
  print('\nTipe Data Boolean');
  bool data = true; //ini adalah tipe data boolean
  data = false;
  print(data);

  print('\nTipe Data String');
  String firstName = 'Nur';
  String lastName = 'Salim';
  // print('$firsName $lastName');
  // string di atas juga dapat dilakukan dengan interpolasi string seperti berikut
  var fullName = '$firstName $lastName';
  print(fullName);

  print('\nTipe data Dynamic'); //block yang menampung tipe data apapun
  dynamic bebas;
  bebas = 'salim';
  print(bebas);
  bebas = false;
  print(bebas);
  bebas = 1234;
  print(bebas);

  print('\nMetode Konversi data');
  var typeString = '12345';
  var typeDouble = double.parse(typeString);
  var typeInt = int.parse(typeString);
  var typeIntToDouble = typeInt.toDouble();

  print(typeDouble);
  print(typeInt);
  print(typeIntToDouble);
}

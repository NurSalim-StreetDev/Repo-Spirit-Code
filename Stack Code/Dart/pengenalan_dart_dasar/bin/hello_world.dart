
void main() {
  String nameSaya = 'Nur Salim';
  var kelasSaya = 'Sistem Informasi';
  final jenisKelamin = 'Laki-Laki';
  print(nameSaya);
  nameSaya = 'Gumming';
  print(nameSaya);
  print(kelasSaya);
  print(jenisKelamin);

  final array1 = [1,2,3,4,5]; //Final memungkinkan kamu dapat merubah isinya tapi tidak dengan deklarasi ulang variabel
  const array2 = [6,7,8,9,0]; // sedangkan Constanta tidak dapat melakukan keduanya sama sekali
  print(array1);
  print(array2);

  late var value = getvalue();
  print('pembatas');
  print(value);
}

String getvalue() {
  print('Get value() di panggil!');
  return 'Nur Salim Fungsi';
}


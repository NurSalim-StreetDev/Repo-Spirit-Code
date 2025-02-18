console.log('Hello World')

// Menuliskan kode JavaScript dan menampilkannya ke konsol
// Memahami penggunaan komentar pada kode
// Memahami konsep variabel pada JavaScript
// Memahami beberapa jenis tipe data pada JavaScript
// Mengenal operator pada JavaScript dan bagaimana menggunakannya
// Memahami konsep percabangan pada pemrograman
// Memahami konsep perulangan pada pemrograman
let Tes = 'aku';
console.log(`Tes ${Tes}`);

let Tes_2 = 'aku';
console.log(`Tes_2 ${Tes_2}`);

// condition ? true expression : false expression

const isMember = false;
const discount = isMember ? 1 : 4;
console.log(`Anda mendapatkan diskon sebesar ${discount * 100}%`)

let kondisi = true;
let hasil;

if (kondisi) {
    hasil = "Jika Benar";
} 
else {
    hasil = "Jika Salah";
}
console.log(hasil)

let kondisi2 = 2;
let hasil2;
if (kondisi2 >= 3) {
    console.log('Jika Benar Itu')
}
else if (kondisi2 <= 3) {console.log('Jika Salah Itu')}


if (true) {console.log('contoh aneh')}

// Menggunakan BigInt
let angkaBesar = 42n;

// Menghitung faktorial dengan menggunakan BigInt
function hitungFaktorial(n) {
    if (n === 0n || n === 1n) {
        return 1n;
    } else {
        return n * hitungFaktorial(n - 1n);
    }
}

// Menghitung faktorial dari angkaBesar
let hasilFaktorial = hitungFaktorial(angkaBesar);

console.log(`Faktorial dari ${angkaBesar} adalah: ${hasilFaktorial}`);

let a = 42n;
let b = 10; // JavaScript dapat mengidentifikasi bahwa ini adalah tipe data Number
let hasil3 =BigInt(a+3); // Hasilnya adalah BigInt
console.log(hasil3)

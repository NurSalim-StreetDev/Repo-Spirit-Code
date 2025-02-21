// Menambahkan event listener ke formulir
document.getElementById('form-kontak').addEventListener('submit', function (e) {
    e.preventDefault(); // Mencegah pengiriman form default
    alert('Terima kasih! Pesan Anda telah dikirim.');
    // Reset formulir setelah dikirim
    this.reset();
});
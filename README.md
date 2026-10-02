# Pertemuan 05 Perulangan Python
- Nama: Tantri Widya Solehati
- NIM: 2225250114
- Kelas: 3F
## Tujuan
Menggunakan for dan while untuk menyelesaikan masalah iteratif.
## Cara Menjalankan
python3 kuis/kuis2_deret_aritmetika.py
## Algoritma Kuis 2
1. Mulai program deret aritmetika
2. Input nilai suku pertama a
3. Input nilai beda d
4. Input jumlah suku n
5. Jika n <= 0, tampilkan pesan "n harus bilangan bulat positif" lalu minta input ulang n
6. Set total = 0
7. Lakukan perulangan dari i = 0 sampai i < n:
    - Hitung suku ke-i+1 dengan rumus: suku = a + i * d
    - Tambahkan suku ke dalam total
    - Cetak nilai suku ke-i+1
8. Setelah perulangan selesai, tampilkan hasil jumlah deret: total
9. Selesai
## Hasil Pengujian
| a  | d  | n | keluaran yang diharapkan          | keluaran aktual                     | status  |
|----|----|---|-----------------------------------|-------------------------------------|---------|
| 2  | 3  | 5 | suku: 2, 5, 8, 11, 14 ; jumlah:40 | suku: 2, 5, 8, 11, 14 ; jumlah: 40  | Sesuai  |
| 10 | -2 | 4 | suku: 10, 8, 6, 4 ; jumlah: 28    | suku: 10, 8, 6, 4 ; jumlah: 28      | Sesuai  |
|1.5 |0.5 | 3 | suku: 1.5, 2.0, 2.5 ; jumlah: 6.0 | suku: 1.5, 2.0, 2.5 ; jumlah: 6.0   | Sesuai  |
## Refleksi
- Kesalahan:
    1. Pada kode awal, semua input ditulis dengan int().
    2. Akibatnya, kalau pengguna memasukkan bilangan desimal untuk a atau d, program akan error karena int() hanya menerima bilangan bulat.
    3. Perulangan for i in range(n) sendiri berjalan benar, tetapi nilai suku yang dihitung tidak bisa menampung desimal.
- Cara Memperbaiki:
    1. Gunakan float() untuk input yang boleh berupa bilangan desimal (a dan d).
    2. Tetap gunakan int() untuk n, karena jumlah suku harus bilangan bulat.
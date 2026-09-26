# Aplikasi Kriptografi (CLI)

Aplikasi baris perintah (Command Line Interface) yang mengimplementasikan berbagai algoritma kriptografi klasik dan modern, sebagai tugas kelompok mata kuliah Kriptografi.

## Deskripsi

Aplikasi ini menyediakan 5 (lima) menu utama yang masing-masing merepresentasikan satu skema enkripsi/dekripsi, mulai dari algoritma klasik hingga algoritma modern, serta satu menu tambahan yang menggabungkan seluruh algoritma tersebut secara berlapis (super enkripsi).

## Struktur Menu

| Menu | Nama File | Algoritma | Jenis |
|------|-----------|-----------|-------|
| 1 | `menu_klasik_1.py` | Caesar Cipher | Klasik |
| 2 | `menu_klasik_2.py` | Vigenere Cipher | Klasik |
| 3 | `menu_modern_1.py` | RSA | Modern (Asimetris) |
| 4 | `menu_modern_2.py` | AES-128 | Modern (Simetris) |
| 5 | `menu_super_enkripsi.py` | Gabungan Caesar -> Vigenere -> RSA -> AES | Super Enkripsi |

## Fitur

- Enkripsi dan dekripsi untuk masing-masing algoritma pada menu 1-4
- Tampilan detail tahapan proses (log perhitungan) pada setiap operasi, agar mudah ditelusuri dan diverifikasi
- Validasi input (teks kosong, format kunci, format ciphertext) pada setiap menu
- Menu klasik (Caesar Cipher) dilengkapi fitur brute force dekripsi untuk kasus kunci tidak diketahui
- Menu Super Enkripsi menggabungkan keempat algoritma secara berurutan untuk membentuk enkripsi berlapis (multi-layer encryption)
- Program dapat mengulang proses tanpa perlu dijalankan kembali dari awal

## Instalasi

Aplikasi ini membutuhkan pustaka `pycryptodome` untuk keperluan algoritma AES-128. Instalasi dapat dilakukan melalui perintah berikut:

```bash
pip install pycryptodome
```

## Cara Menjalankan

1. Pastikan seluruh file modul (`menu_klasik_1.py`, `menu_klasik_2.py`, `menu_modern_1.py`, `menu_modern_2.py`, `menu_super_enkripsi.py`) berada dalam satu folder yang sama.
2. Jalankan file utama (`main.py` atau file yang memuat menu navigasi) melalui terminal:

```bash
python main.py
```

3. Pilih menu yang diinginkan (1-5) sesuai dengan algoritma yang akan digunakan.
4. Masukkan teks, kunci (apabila diperlukan), dan pilih aksi (Enkripsi/Dekripsi) sesuai instruksi pada layar.

## Penjelasan Singkat Algoritma

### 1. Caesar Cipher
Algoritma substitusi klasik yang menggeser posisi setiap huruf/angka sejauh nilai kunci tertentu. Bersifat simetris (kunci enkripsi sama dengan kunci dekripsi).

### 2. Vigenere Cipher
Pengembangan dari Caesar Cipher, dengan nilai pergeseran yang berbeda-beda mengikuti setiap huruf pada kata kunci yang diulang sepanjang teks.

### 3. RSA
Algoritma kriptografi asimetris yang menggunakan sepasang kunci berbeda, yaitu kunci publik untuk enkripsi dan kunci privat untuk dekripsi, berdasarkan operasi modular pada bilangan prima besar.

### 4. AES-128
Algoritma kriptografi simetris berbasis block cipher, memproses data dalam blok berukuran 128 bit (16 byte) menggunakan satu kunci yang sama untuk enkripsi maupun dekripsi.

### 5. Super Enkripsi
Menggabungkan keempat algoritma di atas secara berurutan (Caesar -> Vigenere -> RSA -> AES) pada proses enkripsi, dan urutan terbalik (AES -> RSA -> Vigenere -> Caesar) pada proses dekripsi, guna meningkatkan tingkat keamanan melalui pelapisan enkripsi.

## Catatan

- Nilai bilangan prima (p, q) pada modul RSA dan key pada modul AES yang digunakan dalam aplikasi ini masih berukuran kecil, sehingga hanya sesuai untuk keperluan pembelajaran dan demonstrasi, bukan untuk penggunaan produksi.
- Mode ECB yang digunakan pada AES-128 dipilih karena kesederhanaannya untuk keperluan pembelajaran.

## Anggota Kelompok
- Rio
- Ifsal
- Erlan
- Nahdia

## Mata Kuliah

Kriptografi
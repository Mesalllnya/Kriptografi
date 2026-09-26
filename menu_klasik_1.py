# ================================================
# CAESAR CIPHER - Algoritma Klasik Kriptografi 
# ================================================
# Konsep dasar: setiap karakter digeser sejauh N posisi dalam urutan abjad/angka
# Nilai ASCII acuan:
#   'A' = 65, 'Z' = 90   -> huruf kapital
#   'a' = 97, 'z' = 122  -> huruf kecil
#   '0' = 48, '9' = 57   -> angka (dihitung menggunakan int(), bukan ord())

def caesarChiper_enkripsi(plaintext: str, kunci: int) -> str:
    """
    Algoritma Caesar Cipher: menggeser posisi abjad ke kanan sebanyak kunci

    Args:
        plaintext (str) : Plain Text yang akan dienkripsi
        kunci (int) : jumlah pergeseran karakter (dapat berupa nilai negatif, akan otomatis digeser ke kiri)

    Returns:
        str: Ciphertext hasil enkripsi (hanya berupa string murni)
    """
    cipherText = ""  # variabel penampung, hasil enkripsi dibangun karakter demi karakter di sini

    # kunci di-casting ke int untuk berjaga-jaga apabila dikirim dalam bentuk string (misalnya dari input())
    kunci = int(kunci)

    # kunci dinormalisasi terlebih dahulu ke rentang 0-25 menggunakan modulo
    # tujuannya agar kunci negatif (misalnya -3) atau kunci yang melebihi 26 (misalnya 30)
    # tetap menghasilkan pergeseran yang benar tanpa perlu penanganan kasus khusus di bawah
    kunci = kunci % 26

    # perulangan dilakukan terhadap setiap karakter yang ada di dalam plaintext, satu per satu
    for karakter in plaintext:
        # pengecekan apakah karakter yang sedang diproses termasuk huruf (a-z / A-Z)
        if karakter.isalpha():
            # jika huruf kapital
            if karakter.isupper():
                # Rumus: C = (P - A + K) mod 26 + A
                # - ord(karakter) - ord('A')  -> mengubah huruf menjadi posisi urut 0-25 (A=0, B=1, ..., Z=25)
                # - + kunci                   -> menggeser posisi tersebut sebanyak nilai kunci
                # - % 26                      -> memastikan hasil tetap dalam rentang 0-25 (apabila melewati Z, kembali ke A)
                # - + ord('A')                -> mengembalikan nilai ke rentang kode ASCII huruf kapital
                chiper = ((ord(karakter) - ord('A') + kunci) % 26) + ord('A')
            # jika huruf kecil
            else:
                # rumus identik dengan huruf kapital, hanya acuannya menggunakan 'a', bukan 'A'
                chiper = ((ord(karakter) - ord('a') + kunci) % 26) + ord('a')

            # chr() mengubah kode ASCII (bilangan) hasil perhitungan di atas kembali menjadi karakter huruf
            # hasilnya langsung ditambahkan ke variabel cipherText
            cipherText += chr(chiper)

        # apabila karakter bukan huruf, dilakukan pengecekan apakah karakter tersebut merupakan angka (0-9)
        elif karakter.isdigit():
            # untuk angka, rentang yang tersedia hanya 0-9 (10 digit), sehingga modulonya menggunakan 10, bukan 26
            # int(karakter) mengubah karakter angka menjadi nilai integer aslinya sebelum dihitung
            chiper = ((int(karakter) + kunci) % 10)
            # str() mengubah hasil perhitungan (bilangan) kembali menjadi karakter string sebelum digabungkan
            cipherText += str(chiper)

        # apabila karakter bukan huruf maupun angka (spasi, tanda baca, simbol, dan sejenisnya)
        else:
            # karakter dibiarkan tanpa perubahan, tidak ikut diproses dalam enkripsi
            cipherText += karakter

    # mengembalikan nilai akhir cipherText yang telah lengkap terbentuk
    return cipherText


def caesarChiper_dekripsi(chipertext: str, kunci: int) -> str:
    """
    Algoritma Caesar Cipher: menggeser posisi abjad ke kiri sebanyak kunci

    Args:
        chipertext (str) : Cipher Text yang akan didekripsi
        kunci (int) : jumlah pergeseran karakter (dapat berupa nilai negatif)

    Returns:
        str: Plaintext hasil dekripsi (hanya berupa string murni)
    """
    # proses ini pada dasarnya merupakan kebalikan dari proses enkripsi
    # apabila enkripsi menggeser ke kanan (+kunci), maka dekripsi menggeser ke kiri (-kunci)
    # agar karakter dapat dikembalikan ke bentuk aslinya
    plainText = ""
    kunci = int(kunci)
    kunci = kunci % 26

    for karakter in chipertext:
        if karakter.isalpha():
            if karakter.isupper():
                # Rumus: P = (C - A - K) mod 26 + A
                # tanda minus di depan kunci inilah yang membedakan proses ini dari proses enkripsi
                plain = ((ord(karakter) - ord('A') - kunci) % 26) + ord('A')
            else:
                plain = ((ord(karakter) - ord('a') - kunci) % 26) + ord('a')
            plainText += chr(plain)

        elif karakter.isdigit():
            # rumus dekripsi untuk angka: P = (C - K) mod 10
            plain = ((int(karakter) - kunci) % 10)
            plainText += str(plain)

        else:
            # karakter selain huruf dan angka tetap dibiarkan sama seperti aslinya
            plainText += karakter

    return plainText


def proses_caesar_enkripsi(plaintext: str, kunci: int):
    """
    Menampilkan tahapan pergeseran karakter satu per satu pada saat proses enkripsi,
    sehingga pengguna dapat melihat prosesnya, bukan hanya hasil akhirnya saja

    Args:
        plaintext (str) : teks asli yang akan dienkripsi
        kunci (int) : jumlah pergeseran karakter
    """
    kunci = int(kunci) % 26
    print(f"\n[PROSES] Menggeser karakter sebanyak {kunci} langkah ke kanan...")

    # perulangan ini dilakukan kembali, namun kali ini bertujuan untuk menampilkan
    # setiap tahapan perubahan karakter ke layar, bukan menyimpan hasilnya
    for karakter in plaintext:
        if karakter.isalpha():
            if karakter.isupper():
                chiper = ((ord(karakter) - ord('A') + kunci) % 26) + ord('A')
            else:
                chiper = ((ord(karakter) - ord('a') + kunci) % 26) + ord('a')
            # menampilkan perubahan dari karakter asli menjadi karakter hasil pergeseran
            print(f"{karakter} -> {chr(chiper)}")

        elif karakter.isdigit():
            chiper = ((int(karakter) + kunci) % 10)
            print(f"{karakter} -> {str(chiper)} (Angka)")

        else:
            # menandakan bahwa karakter ini tidak diproses/diubah
            print(f"{karakter} -> {karakter} (Dibiarkan)")
    print("-" * 30)  # garis pemisah agar tampilan output lebih rapi


def proses_caesar_dekripsi(chipertext: str, kunci: int):
    """
    Menampilkan tahapan pergeseran karakter satu per satu pada saat proses dekripsi

    Args:
        chipertext (str) : teks acak (cipher) yang akan dikembalikan ke bentuk asli
        kunci (int) : jumlah pergeseran karakter
    """
    kunci = int(kunci) % 26
    print(f"\n[PROSES] Menggeser karakter sebanyak {kunci} langkah ke kiri...")

    for karakter in chipertext:
        if karakter.isalpha():
            if karakter.isupper():
                plain = ((ord(karakter) - ord('A') - kunci) % 26) + ord('A')
            else:
                plain = ((ord(karakter) - ord('a') - kunci) % 26) + ord('a')
            print(f"{karakter} -> {chr(plain)}")

        elif karakter.isdigit():
            plain = ((int(karakter) - kunci) % 10)
            print(f"{karakter} -> {str(plain)} (Angka)")

        else:
            print(f"{karakter} -> {karakter} (Dibiarkan)")
    print("-" * 30)


def brute_force_dekripsi(chipertext: str):
    """
    Fitur tambahan: mencoba seluruh kemungkinan kunci (1 sampai 25) untuk proses dekripsi.
    Fitur ini berguna apabila hanya tersedia ciphertext tanpa mengetahui kuncinya,
    karena pada Caesar Cipher jumlah kemungkinan kunci hanya terbatas 25 (untuk huruf A-Z).
    Pengguna cukup memeriksa baris mana yang membentuk kalimat bermakna.

    Args:
        chipertext (str) : teks acak (cipher) yang akan dicoba didekripsi
    """
    print("\n[BRUTE FORCE] Mencoba seluruh kemungkinan kunci (1-25):")
    print("-" * 40)
    # perulangan dari kunci 1 sampai 25, karena kunci 0 dan 26 sama artinya dengan tanpa pergeseran
    for kunci_coba in range(1, 26):
        hasil = caesarChiper_dekripsi(chipertext, kunci_coba)
        # :>2 pada f-string digunakan agar angka kunci rata kanan sebanyak 2 digit, supaya tampilan rapi
        print(f"Kunci {kunci_coba:>2}: {hasil}")
    print("-" * 40)


def jalankan():
    """
    Fungsi utama yang menjalankan program dari sisi pengguna (menu interaktif pada terminal)
    Alur program: input teks -> pemilihan aksi -> (input kunci apabila diperlukan) ->
    menampilkan tahapan proses -> menampilkan hasil akhir -> menawarkan pengulangan
    """
    print("\n--- Algoritma KLASIK Caesar Chiper ---")

    # perulangan utama, agar program dapat mengulang proses tanpa harus dijalankan kembali dari luar
    while True:
        teks = input("\nMasukkan teks (Plaintext/Ciphertext): ")

        # validasi agar teks yang kosong (hanya berisi spasi atau tidak diisi sama sekali) tidak diproses
        if teks.strip() == "":
            print("Teks tidak boleh kosong. Silakan coba kembali.")
            continue  # melewati sisa perulangan ini dan kembali meminta input teks

        print("\nPilih Aksi:")
        print("1. Enkripsi")
        print("2. Dekripsi")
        print("3. Brute Force Dekripsi (kunci tidak diketahui)")
        aksi = input("Pilihan (1/2/3): ")

        if aksi == "3":
            # aksi brute force tidak memerlukan input kunci sama sekali, sehingga langsung dipanggil
            brute_force_dekripsi(teks)

        elif aksi in ("1", "2"):
            # perulangan khusus untuk validasi kunci, dipisah dari perulangan utama
            # supaya hanya bagian input kunci saja yang diulang apabila input tidak valid
            while True:
                kunci_input = input("Masukkan kunci (geser, dapat berupa nilai negatif): ")

                # isdigit() saja tidak cukup karena metode tersebut tidak dapat mendeteksi
                # bilangan negatif (misalnya "-3" akan dianggap tidak valid oleh isdigit())
                # sehingga dilakukan pengecekan manual:
                # - lstrip("-") menghapus tanda minus di awal (jika ada)
                # - sisanya harus berupa digit, dan input tidak boleh hanya berupa "-" saja
                is_valid = kunci_input.lstrip("-").isdigit() and kunci_input not in ("", "-")

                if is_valid:
                    kunci = int(kunci_input)

                    if aksi == "1":
                        # menampilkan tahapan proses terlebih dahulu sebelum hasil akhir
                        proses_caesar_enkripsi(teks, kunci)
                        hasil = caesarChiper_enkripsi(teks, kunci)
                        print(f"✅ Hasil Enkripsi: {hasil}")
                    else:
                        proses_caesar_dekripsi(teks, kunci)
                        hasil = caesarChiper_dekripsi(teks, kunci)
                        print(f"✅ Hasil Dekripsi: {hasil}")
                    break  # keluar dari perulangan validasi kunci setelah berhasil diproses
                else:
                    print("Kunci harus berupa angka (dapat berupa nilai negatif, misalnya -3).")

        else:
            # apabila pengguna memasukkan pilihan aksi selain 1, 2, atau 3
            print("Aksi tidak dikenal. Proses dibatalkan.")

        # menanyakan kepada pengguna apakah ingin mengulang proses atau mengakhiri program
        # inilah yang membuat menu benar-benar berjalan secara berulang (looping)
        ulang = input("\nApakah ingin mencoba kembali? (y/n): ").strip().lower()
        if ulang != "y":
            break  # keluar dari perulangan utama apabila pengguna tidak menjawab "y"

    print("\nKembali ke Menu Utama...")
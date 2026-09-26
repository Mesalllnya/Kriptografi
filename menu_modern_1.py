# ================================================
# RSA CIPHER - Algoritma Modern Kriptografi (Kunci Asimetris)
# ================================================
# Konsep dasar: RSA menggunakan sepasang kunci yang berbeda, yaitu kunci publik (e, n)
# untuk enkripsi dan kunci privat (d, n) untuk dekripsi. Berbeda dengan Caesar/Vigenere
# yang bersifat simetris (kunci enkripsi = kunci dekripsi), pada RSA kedua kunci tersebut
# berbeda namun saling berpasangan secara matematis.
#
# Rumus utama:
#   Enkripsi : C = M^e mod n
#   Dekripsi : M = C^d mod n
# dengan M adalah nilai byte dari karakter plaintext, dan C adalah ciphertext berupa angka.

def enkripsiRSA(plainText: str) -> str:
    """
    Melakukan enkripsi plaintext menggunakan algoritma RSA.

    Args:
        plainText (str): Teks yang akan dienkripsi.

    Returns:
        str: Ciphertext hasil enkripsi RSA.
    """
    cipherText = ""

    print("\nProses RSA Enkripsi\n")
    print("[1]. Plaintext : ", plainText)

    # setiap karakter perlu diubah menjadi representasi angka (byte) terlebih dahulu,
    # karena operasi pangkat dan modulo pada RSA hanya dapat dilakukan terhadap bilangan
    plaintext_bytes = plainText.encode("utf-8")

    print("[2]. Konversi ke nilai byte: ", list(plaintext_bytes))
    print("[3]. Rumus RSA: C = M^e mod n")

    hasil = []

    # setiap byte (mewakili satu karakter) dienkripsi secara terpisah, bukan sekaligus,
    # karena nilai M harus lebih kecil daripada n agar hasil dekripsi dapat kembali dengan benar
    for i, byte in enumerate(plaintext_bytes):
        # pow(byte, e, n) menghitung (byte pangkat e) mod n secara efisien
        # penggunaan pow() dengan tiga argumen jauh lebih cepat dibandingkan (byte ** e) % n
        # karena Python melakukan perhitungan modulo di setiap tahap perpangkatan (modular exponentiation),
        # bukan menghitung byte^e sebagai bilangan raksasa terlebih dahulu baru dimodulo di akhir
        cipher = pow(byte, e, n)
        hasil.append(str(cipher))

        print(f"  Karakter ke-{i + 1}: M = {byte} -> C = {cipher}")

    # hasil akhir digabungkan dengan spasi sebagai pemisah antar-blok angka,
    # karena setiap angka dapat memiliki jumlah digit yang berbeda-beda
    cipherText = " ".join(hasil)

    print("[4] Ciphertext : ", cipherText)

    return cipherText


def dekripsiRSA(cipherText: str) -> str:
    """
    Melakukan dekripsi ciphertext menggunakan algoritma RSA.

    Args:
        cipherText (str): Ciphertext berupa angka yang dipisahkan spasi.

    Returns:
        str: Plaintext hasil dekripsi RSA.
    """
    print("\n Proses RSA Dekripsi")
    print("[1] Ciphertext : ", cipherText)

    try:
        # ciphertext dipecah berdasarkan spasi, lalu setiap bagian dikonversi menjadi int
        # blok try/except diperlukan karena input dari pengguna bisa saja bukan berupa angka
        cipher_blocks = [int(x) for x in cipherText.split()]
    except ValueError:
        print("[ERROR] Ciphertext harus berupa angka!")
        return ""

    print("[2] Rumus RSA: M = C^d mod n")

    hasil = []

    for i, cipher in enumerate(cipher_blocks):
        # proses dekripsi menggunakan kunci privat (d, n), kebalikan dari proses enkripsi
        plain = pow(cipher, d, n)
        hasil.append(plain)

        print(f"    Blok ke-{i + 1}: C = {cipher} -> M = {plain}")

    # setelah didapat kembali nilai byte aslinya, byte tersebut dirangkai menjadi
    # objek bytes lalu didekode menggunakan UTF-8 untuk dikembalikan menjadi teks
    plaintext = bytes(hasil).decode("utf-8")

    print("[3] Konversi byte :", hasil)
    print("[4] Plaintext :", plaintext)

    return plaintext


# ================================================
# PEMBANGKITAN KUNCI RSA
# ================================================
# Bilangan prima p dan q dipilih terlebih dahulu (dalam praktik nyata, keduanya
# berukuran sangat besar dan dirahasiakan; di sini digunakan nilai kecil agar
# perhitungan mudah ditelusuri untuk keperluan pembelajaran)
p = 61
q = 53

# n = p x q, dipakai bersama pada kunci publik maupun kunci privat, dan nilainya
# menentukan batas maksimum nilai byte yang dapat dienkripsi dengan aman (M harus < n)
n = p * q

# phi(n) = (p - 1)(q - 1), disebut fungsi Euler, digunakan untuk menghitung kunci privat
phi = (p - 1) * (q - 1)

# e adalah bagian dari kunci publik, dipilih sedemikian rupa sehingga nilainya
# relatif prima terhadap phi (tidak memiliki faktor persekutuan selain 1)
e = 17

# d adalah bagian dari kunci privat, merupakan invers modular dari e terhadap phi,
# yaitu bilangan yang memenuhi (e * d) mod phi = 1
# pow(e, -1, phi) menghitung invers modular tersebut secara langsung (fitur Python 3.8 ke atas)
d = pow(e, -1, phi)


def jalankan():
    """
    Fungsi utama yang menjalankan program dari sisi pengguna (menu interaktif pada terminal)
    Alur program: menampilkan info kunci -> input teks -> pemilihan aksi -> proses -> hasil ->
    menawarkan pengulangan, sehingga program tidak perlu dijalankan kembali dari luar
    """
    print("\n--- Algoritma MODERN 1 (RSA) ---")

    # menampilkan informasi kunci publik dan privat sekali di awal,
    # sebagai referensi bagi pengguna untuk memahami parameter yang sedang digunakan
    print("\n[INFO RSA]")
    print(f"Public Key  : (e={e}, n={n})")
    print(f"Private Key : (d={d}, n={n})")

    # perulangan utama, agar program dapat mengulang proses tanpa harus dijalankan kembali dari luar
    while True:
        teks = input("\nMasukkan teks (Plaintext/Ciphertext): ")

        # validasi agar teks kosong (atau hanya berisi spasi) tidak diproses lebih lanjut
        if teks.strip() == "":
            print("Teks tidak boleh kosong. Silakan coba kembali.")
            continue

        print("\nPilih Aksi:")
        print("1. Enkripsi")
        print("2. Dekripsi")
        aksi = input("Pilihan (1/2): ")

        if aksi == "1":
            cipherText = enkripsiRSA(teks)
            print(f"\n✅ Hasil Enkripsi: {cipherText}")

        elif aksi == "2":
            plainText = dekripsiRSA(teks)

            # hasil dekripsi hanya ditampilkan apabila proses konversi berhasil (bukan string kosong)
            if plainText != "":
                print(f"\n✅ Hasil Dekripsi: {plainText}")

        else:
            print("Aksi tidak dikenal. Proses dibatalkan.")

        # menanyakan kepada pengguna apakah ingin mengulang proses atau mengakhiri program
        ulang = input("\nApakah ingin mencoba kembali? (y/n): ").strip().lower()
        if ulang != "y":
            break

    print("\nKembali ke Menu Utama...")


if __name__ == "__main__":
    jalankan()
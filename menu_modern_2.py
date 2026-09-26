from Crypto.Cipher import AES

# ================================================
# AES-128 CIPHER - Algoritma Modern Kriptografi (Kunci Simetris, Block Cipher)
# ================================================
# Konsep dasar: berbeda dengan Caesar/Vigenere yang memproses karakter satu per satu,
# AES memproses data dalam bentuk blok berukuran tetap, yaitu 16 byte (128 bit) per blok.
# AES-128 berarti panjang kunci yang digunakan adalah 128 bit, atau setara 16 byte.
# Mode ECB (Electronic Codebook) yang dipakai di sini mengenkripsi setiap blok 16 byte
# secara independen menggunakan kunci yang sama.

# AES-128 mensyaratkan panjang key harus tepat 16 bytes (128 bit)
# apabila panjangnya tidak sesuai, library PyCryptodome akan menampilkan error saat AES.new() dipanggil
key = b"1234567890abcdef"


def enkripsiAES(plainText: str) -> str:
    """
    Melakukan enkripsi plaintext menggunakan AES-128.

    Args:
        plainText (str): Teks yang akan dienkripsi.

    Returns:
        str: Ciphertext hasil enkripsi dalam format hexadecimal.
    """
    print("\nProses AES Enkripsi")
    print("[1] Plaintext :", plainText)

    # teks perlu diubah menjadi bytes terlebih dahulu, karena AES bekerja pada level byte, bukan karakter
    data = plainText.encode("utf-8")
    print("[2] Plaintext Bytes :", list(data))

    # AES mengharuskan panjang data merupakan kelipatan 16 byte
    # apabila panjang data belum kelipatan 16, perlu ditambahkan byte tambahan (padding) di akhir
    # skema padding yang digunakan di sini adalah PKCS#7: nilai byte padding yang ditambahkan
    # sama dengan jumlah byte padding itu sendiri, sehingga proses penghapusannya mudah dilakukan
    # kembali saat dekripsi (cukup dibaca dari byte terakhir)
    padding = 16 - (len(data) % 16)
    data = data + bytes([padding] * padding)

    print("[3] Setelah Padding :", list(data))
    print("[4] AES-128 Key :", key.decode())

    # membuat objek cipher AES dengan mode ECB (Electronic Codebook)
    # pada mode ini, setiap blok 16 byte dienkripsi secara terpisah dan independen
    cipher = AES.new(key, AES.MODE_ECB)

    # melakukan enkripsi terhadap seluruh data (yang sudah dalam kelipatan 16 byte) sekaligus
    encrypted = cipher.encrypt(data)

    # hasil enkripsi berupa bytes acak, sehingga diubah ke format heksadesimal
    # agar dapat ditampilkan dan disalin sebagai teks biasa (tanpa karakter yang tidak dapat dicetak)
    cipherText = encrypted.hex().upper()
    print("[5] Ciphertext Hex :", cipherText)

    return cipherText


def dekripsiAES(cipherText: str) -> str:
    """
    Melakukan dekripsi ciphertext menggunakan AES-128.

    Args:
        cipherText (str): Ciphertext hexadecimal.

    Returns:
        str: Plaintext hasil dekripsi.
    """
    print("\n Proses AES Dekripsi")
    print("[1] Ciphertext Hex :", cipherText)

    try:
        # ciphertext dalam format heksadesimal dikembalikan menjadi bytes asli
        # blok try/except diperlukan karena input dari pengguna belum tentu berupa heksadesimal yang valid
        encrypted = bytes.fromhex(cipherText)
    except ValueError:
        print("[ERROR] Ciphertext harus berupa heksadesimal!")
        return ""

    print("[2] Ciphertext Bytes :", list(encrypted))
    print("[3] AES-128 Key : ", key.decode())

    # dekripsi memerlukan key yang sama persis dengan yang dipakai saat enkripsi
    cipher = AES.new(key, AES.MODE_ECB)

    # mendekripsi seluruh blok ciphertext, hasilnya masih termasuk byte padding di bagian akhir
    decrypted = cipher.decrypt(encrypted)

    print("[4] Hasil Dekripsi dengan Padding :", list(decrypted))

    try:
        # byte terakhir dari hasil dekripsi menunjukkan jumlah byte padding yang ditambahkan
        # sesuai skema PKCS#7 yang digunakan pada saat proses enkripsi
        padding = decrypted[-1]

        # byte padding dihapus dengan mengambil data mulai dari awal hingga sebelum bagian padding
        plaintext_bytes = decrypted[:-padding]

        # bytes hasil dekripsi dikonversi kembali menjadi teks menggunakan UTF-8
        plaintext = plaintext_bytes.decode("utf-8")

    except (ValueError, UnicodeDecodeError):
        # kegagalan pada tahap ini biasanya menandakan ciphertext atau key yang digunakan tidak sesuai,
        # sehingga hasil dekripsi berupa data acak yang tidak dapat dibaca sebagai teks maupun padding yang valid
        print("[ERROR] Gagal melakukan dekripsi!")
        return ""

    print("[5] Plaintext:", plaintext)
    return plaintext


def jalankan():
    """
    Fungsi utama yang menjalankan program dari sisi pengguna (menu interaktif pada terminal)
    Alur program: menampilkan info kunci -> input teks -> pemilihan aksi -> proses -> hasil ->
    menawarkan pengulangan, sehingga program tidak perlu dijalankan kembali dari luar
    """
    print("\n--- Algoritma Modern 2 (AES-128) ---")
    print("\n[INFO AES]")
    print("Jenis      : AES-128")
    print("Key        :", key.decode())
    print("Key Length : 128-bit")
    print("Block Size : 128-bit")

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
            cipherText = enkripsiAES(teks)
            print(f"\n✅ Hasil Enkripsi: {cipherText}")

        elif aksi == "2":
            plainText = dekripsiAES(teks)

            # hasil dekripsi hanya ditampilkan apabila proses berhasil (bukan string kosong)
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
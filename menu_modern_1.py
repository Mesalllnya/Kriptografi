# Semua Algoritma Kudu punya ini
def enkripsiRSA(plainText: str) -> str:
    # Kalau udah dibikin fungsinya terus ketik " 3 kali biar bikin autodocstringnya kayak dibawah
    """
    Melakukan enkripsi plaintext menggunakan algoritma RSA.

    Args:
        plainText (str): Teks yang akan dienkripsi.

    Returns:
        str: Ciphertext hasil enkripsi RSA.
    """

    # RSA Enkripsi
    cipherText = ""

    print("\nProses RSA Enkripsi\n")
    print("[1]. Plaintext : ", plainText)

    # konversi plaintext menjadi byte
    plaintext_bytes = plainText.encode("utf-8")

    print("[2]. Konversi ke nilai byte: ", list(plaintext_bytes))
    print("[3]. Rumus RSA: C = M^e mod n")

    hasil = []

    for i, byte in enumerate(plaintext_bytes):
        # RSA Enkripsi
        cipher = pow(byte, e, n)
        hasil.append(str(cipher))

        print(f"  Karakter ke-{ i + 1}: " f"M = {byte} -> C = {cipher}")

    # Ciphertextt berupa angka yang dipisahkan spasi
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
        cipher_blocks = [int(x) for x in cipherText.split()]
    except ValueError:
        print("[ERROR] Ciphertext harus berupa angka!")
        return ""

    print("[2] Rumus RSA: M = C^d mod n")

    hasil = []

    for i, cipher in enumerate(cipher_blocks):

        plain = pow(cipher, d, n)
        hasil.append(plain)

        print(f"    Blok ke-{i + 1}: " f"C = {cipher} → M = {plain}")

    # Konversi kembali angka menjadi karakter
    plaintext = bytes(hasil).decode("utf-8")

    print("[3] Konversi byte :", hasil)
    print("[4] Plaintext :", plaintext)

    return plaintext


# Kunci RSA

# Bil Prima
p = 61
q = 53

# n = p × q
n = p * q

# phi (n) = (p - 1)(q - 1)
phi = (p - 1) * (q - 1)

# Public exponent
e = 17

# Private exponent
d = pow(e, -1, phi)


def jalankan():
    # Judul Program Nanti Diganti
    print("\n--- Algoritma MODERN 1 (RSA) ---")

    # Menampilkan informasi key
    print("\n[INFO RSA]")
    print(f"Public Key  : (e={e}, n={n})")
    print(f"Private Key : (d={d}, n={n})")

    teks = input("Masukkan teks (Plaintext/Ciphertext): ")

    print("\nPilih Aksi:")
    print("1. Enkripsi")
    print("2. Dekripsi")
    aksi = input("Pilihan (1/2): ")

    if aksi == "1":
        # RSA Engine Enkripsi + Proses

        cipherText = enkripsiRSA(teks)
        print(f"\n✅ Hasil Enkripsi: {cipherText}")

    elif aksi == "2":
        # RSA Engine Dekripsi + Proses

        plainText = dekripsiRSA(teks)

        if plainText != "":
            print(f"\n✅ Hasil Dekripsi: {teks}_DECRYPTED_KLASIK1")

    else:
        print("Aksi tidak dikenal. Batal.")

    input("\nTekan Enter untuk kembali ke Menu Utama...")


if __name__ == "__main__":
    jalankan()

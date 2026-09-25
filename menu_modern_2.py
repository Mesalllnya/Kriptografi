from Crypto.Cipher import AES

# AES 128 menggunakan key 16 bytes
key = b"1234567890abcdef"


# Semua Algoritma Kudu punya ini
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

    # Konversi plaintext menjadi bytes
    data = plainText.encode("utf-8")
    print("[2] Plaintext Bytes :", list(data))

    # Padding agar panjang data kelipatan 16 byte
    padding = 16 - (len(data) % 16)
    data = data + bytes([padding] * padding)

    print("[3] Setelah Padding :", list(data))
    print("[4] AES-128 Key :", key.decode())

    # Membuat AES dengan mode ECB
    cipher = AES.new(key, AES.MODE_ECB)

    # Enkripsi
    encrypted = cipher.encrypt(data)

    # Ubah ke heksadesimal agar mudah disimpan
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
        # Konversi heksadesimal menjadi bytes
        encrypted = bytes.fromhex(cipherText)
    except ValueError:
        print("[ERROR] Ciphertext harus berupa heksadesimal!")
        return ""

    print("[2] Ciphertext Bytes :", list(encrypted))
    print("[3] AES-128 Key : ", key.decode())

    # Membuat AES dengan key yang sama
    cipher = AES.new(key, AES.MODE_ECB)

    # Dekripsi
    decrypted = cipher.decrypt(encrypted)

    print("[4] Hasil Dekripsi dengan Padding :", list(decrypted))

    try:
        # Ambil jumlah padding dari byte terakhit
        padding = decrypted[-1]

        # Hapus padding
        plaintext_bytes = decrypted[:-padding]

        # Konversi kembali ke teks
        plaintext = plaintext_bytes.decode("utf-8")

    except (ValueError, UnicodeDecodeError):
        print("[ERROR] Gagal melakukan dekripsi!")
        return ""

    print("[5] Plaintext:", plaintext)
    return plaintext


def jalankan():
    # Judul Program Nanti Diganti
    print("\n--- Algoritma Modern 2 (AES-128) ---")
    print("\n[INFO AES]")
    print("Jenis      : AES-128")
    print("Key        :", key.decode())
    print("Key Length : 128-bit")
    print("Block Size : 128-bit")

    teks = input("Masukkan teks (Plaintext/Ciphertext): ")

    print("\nPilih Aksi:")
    print("1. Enkripsi")
    print("2. Dekripsi")
    aksi = input("Pilihan (1/2): ")

    if aksi == "1":
        # AES ENGINE ENKRIPSI + TAMPILAN PROSES
        cipherText = enkripsiAES(teks)
        print(f"\n✅ Hasil Enkripsi: {cipherText}")

    elif aksi == "2":
        # AES ENGINE DEKRIPSI + TAMPILAN PROSES
        plainText = dekripsiAES(teks)

        if plainText != "":
            print(f"\n✅ Hasil Dekripsi: {plainText}")

    else:
        print("Aksi tidak dikenal. Batal.")

    input("\nTekan Enter untuk kembali ke Menu Utama...")


if __name__ == "__main__":
    jalankan()

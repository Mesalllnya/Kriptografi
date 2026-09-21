# Semua Algoritma Kudu punya ini
def algoritmaKu(plainText: str) -> str:
    # Kalau udah dibikin fungsinya terus ketik " 3 kali biar bikin autodocstringnya kayak dibawah
    cipherText = ""
    return cipherText


def jalankan():
    # Judul Program Nanti Diganti
    print("\n--- Algoritma KLASIK 1 ---")
    teks = input("Masukkan teks (Plaintext/Ciphertext): ")

    print("\nPilih Aksi:")
    print("1. Enkripsi")
    print("2. Dekripsi")
    aksi = input("Pilihan (1/2): ")

    if aksi == "1":
        # Nanti Ini Yang diganti
        # DUMMY ENGINE ENKRIPSI + TAMPILAN PROSES
        print("\n[PROSES] Menggeser karakter sebanyak 3 langkah ke kanan...")
        print("[PROSES] A -> D, B -> E...")
        print(f"\n✅ Hasil Enkripsi: {teks}_ENCRYPTED_KLASIK1")

    elif aksi == "2":
        # Nanti Ini Yang diganti
        # DUMMY ENGINE DEKRIPSI + TAMPILAN PROSES
        print("\n[PROSES] Menggeser karakter sebanyak 3 langkah ke kiri...")
        print("[PROSES] D -> A, E -> B...")
        print(f"\n✅ Hasil Dekripsi: {teks}_DECRYPTED_KLASIK1")

    else:
        print("Aksi tidak dikenal. Batal.")

    input("\nTekan Enter untuk kembali ke Menu Utama...")

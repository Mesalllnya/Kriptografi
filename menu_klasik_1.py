# Semua Algoritma Kudu punya ini nama fungsinya diganti aja
# terus semua engine ada didalam ini untuk yang langsung jadi bukan yang per step
# yang per step mungkin bisa bikin fungsi baru

def caesarChiper_enkripsi(plaintext: str, shift: int) -> str:
    # Kalau udah dibikin fungsinya terus ketik " 3 kali biar bikin autodocstringnya kayak dibawah
    """
    Algoritma Caesar Cipher: menggeser posisi abjad ke kanan sebanyak shift/kunci

    Args:
        plainText (str) : Plain Text Yang mau di enkripsi
        shift (int) : jumlah pergeseran karakter

    Returns:
        str: Ciphertext Yang telah dienkripsi
    """

    cipherText = ""
    shift = int(shift)
    for karakter in plaintext:
        # huruf atau abjad
        # rumus enkripsi caesar chiper: (P + K) % 26 menyesuaikan dengan urutan ASCII
        if(karakter.isalpha()):
            # ini yang huruf kapital
            if(karakter.isupper()):
                chiper = ((ord(karakter) - ord('A') + shift) % 26) + ord('A')
                cipherText += chr(chiper)
            # ini yang huruf kecil
            else:
                chiper = ((ord(karakter) - ord('a') + shift) % 26) + ord('a')
                cipherText += chr(chiper)
        # angka
        elif(karakter.isdigit()):
            chiper = ((int(karakter) + shift) % 10)
            cipherText += str(chiper)
        # karakter lain dibiarkan
        else:
            cipherText += karakter


    return cipherText

def caesarChiper_dekripsi(chipertext: str, shift: int) -> str:
    # Kalau udah dibikin fungsinya terus ketik " 3 kali biar bikin autodocstringnya kayak dibawah
    """
    Algoritma Caesar Cipher: menggeser posisi abjad ke kiri sebanyak shift/kunci

    Args:
        chipertext (str) : chiper Text Yang mau di dekripsi
        shift (int) : jumlah pergeseran karakter

    Returns:
        str: Plaintext Yang telah didekripsi
    """

    plainText = ""
    shift = int(shift)
    for karakter in plainText:
        # huruf
        # rumus enkripsi caesar chiper: (P + K) % 26 karena menggunakan ascii jadi
        if(karakter.isalpha()):
            # ini yang huruf kapital
            if(karakter.isupper()):
                plain = ((ord(karakter) - ord('A') - shift) % 26) + ord('A')
                plainText += chr(plain)
            # ini yang huruf kecil
            else:
                plain = ((ord(karakter) - ord('a') - shift) % 26) + ord('a')
                plainText += chr(plain)
        # angka
        elif(karakter.isdigit()):
            plain = ((int(karakter) - shift) % 10)
            plainText += str(plain)
        # karakter lain dibiarkan
        else:
            plainText += karakter


    return plainText
    

def jalankan():
    # Judul Program Nanti Diganti
    print("\n--- Algoritma KLASIK Caesar Chiper ---")
    teks = input("Masukkan teks (Plaintext/Ciphertext): ")
    kunci = int(input("Masukkan kunci (geser berapa): "))

    print("\nPilih Aksi:")
    print("1. Enkripsi")
    print("2. Dekripsi")
    aksi = input("Pilihan (1/2): ")

    if aksi == "1":
        hasil = caesarChiper_enkripsi(teks,kunci)
        print(f"\n[PROSES] Menggeser karakter sebanyak {kunci} langkah ke kanan...")
        # print("[PROSES] A -> D, B -> E...")
        print(f"\n✅ Hasil Enkripsi: {hasil}")

    elif aksi == "2":
        hasil = caesarChiper_dekripsi(teks,kunci)
        print(f"\n[PROSES] Menggeser karakter sebanyak {kunci} langkah ke kiri...")
        # print("[PROSES] D -> A, E -> B...")
        print(f"\n✅ Hasil Dekripsi: {hasil}")

    else:
        print("Aksi tidak dikenal. Batal.")

    input("\nTekan Enter untuk kembali ke Menu Utama...")

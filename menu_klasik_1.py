# Semua Algoritma Kudu punya ini nama fungsinya diganti aja
# terus semua engine ada didalam ini untuk yang langsung jadi bukan yang per step
# yang per step mungkin bisa bikin fungsi baru


def caesarChiper_enkripsi(plaintext: str, kunci: int) -> str:
    """
    Algoritma Caesar Cipher: menggeser posisi abjad ke kanan sebanyak kunci

    Args:
        plaintext (str) : Plain Text Yang mau di enkripsi
        kunci (int) : jumlah pergeseran karakter

    Returns:
        str: Ciphertext Yang telah dienkripsi (Hanya hasil string murni)
    """
    cipherText = ""
    kunci = int(kunci)
    
    for karakter in plaintext:
        if(karakter.isalpha()):
            if(karakter.isupper()):
                chiper = ((ord(karakter) - ord('A') + kunci) % 26) + ord('A')
            else:
                chiper = ((ord(karakter) - ord('a') + kunci) % 26) + ord('a')
            cipherText += chr(chiper)
            
        elif(karakter.isdigit()):
            chiper = ((int(karakter) + kunci) % 10)
            cipherText += str(chiper)
            
        else:
            cipherText += karakter

    return cipherText

def caesarChiper_dekripsi(chipertext: str, kunci: int) -> str:
    """
    Algoritma Caesar Cipher: menggeser posisi abjad ke kiri sebanyak kunci/kunci

    Args:
        chipertext (str) : chiper Text Yang mau di dekripsi
        kunci (int) : jumlah pergeseran karakter

    Returns:
        str: Plaintext Yang telah didekripsi (Hanya hasil string murni)
    """
    plainText = ""
    kunci = int(kunci)
    
    for karakter in chipertext:
        if(karakter.isalpha()):
            if(karakter.isupper()):
                plain = ((ord(karakter) - ord('A') - kunci) % 26) + ord('A')
            else:
                plain = ((ord(karakter) - ord('a') - kunci) % 26) + ord('a')
            plainText += chr(plain)
            
        elif(karakter.isdigit()):
            plain = ((int(karakter) - kunci) % 10)
            plainText += str(plain)
            
        else:
            plainText += karakter

    return plainText

def proses_caesar_enkripsi(plaintext: str, kunci: int):
    """ Menampilkan log proses pergeseran karakter saat enkripsi
    
        Args:
            chipertext (str) : chiper Text Yang mau di dekripsi
            kunci (int) : jumlah pergeseran karakter
    """
    kunci = int(kunci)
    print(f"\n[PROSES] Menggeser karakter sebanyak {kunci} langkah ke kanan...")
    
    for karakter in plaintext:
        if(karakter.isalpha()):
            if(karakter.isupper()):
                chiper = ((ord(karakter) - ord('A') + kunci) % 26) + ord('A')
            else:
                chiper = ((ord(karakter) - ord('a') + kunci) % 26) + ord('a')
            print(f"{karakter} -> {chr(chiper)}")
            
        elif(karakter.isdigit()):
            chiper = ((int(karakter) + kunci) % 10)
            print(f"{karakter} -> {str(chiper)} (Angka)")
            
        else:
            print(f"{karakter} -> {karakter} (Dibiarkan)")
    print("-" * 30)

def proses_caesar_dekripsi(chipertext: str, kunci: int):
    """ Menampilkan log proses pergeseran karakter saat dekripsi
    
        Args:
            chipertext (str) : chiper Text Yang mau di dekripsi
            kunci (int) : jumlah pergeseran karakter
    """
    kunci = int(kunci)
    print(f"\n[PROSES] Menggeser karakter sebanyak {kunci} langkah ke kiri...")
    
    for karakter in chipertext:
        if(karakter.isalpha()):
            if(karakter.isupper()):
                plain = ((ord(karakter) - ord('A') - kunci) % 26) + ord('A')
            else:
                plain = ((ord(karakter) - ord('a') - kunci) % 26) + ord('a')
            print(f"{karakter} -> {chr(plain)}")
            
        elif(karakter.isdigit()):
            plain = ((int(karakter) - kunci) % 10)
            print(f"{karakter} -> {str(plain)} (Angka)")
            
        else:
            print(f"{karakter} -> {karakter} (Dibiarkan)")
    print("-" * 30)

def jalankan():
    print("\n--- Algoritma KLASIK Caesar Chiper ---")
    teks = input("Masukkan teks (Plaintext/Ciphertext): ")

    while True:
        kunci = input("Masukkan kunci (geser): ")

        if kunci.isdigit():
            kunci = int(kunci)
            print("\nPilih Aksi:")
            print("1. Enkripsi")
            print("2. Dekripsi")
            aksi = input("Pilihan (1/2): ")

            if aksi == "1" :
                # Tampilkan langkah-langkahnya dulu
                proses_caesar_enkripsi(teks, kunci)
                
                hasil = caesarChiper_enkripsi(teks, kunci)        
                print(f"✅ Hasil Enkripsi: {hasil}")

            elif aksi == "2" :
                # Tampilkan langkah-langkahnya dulu
                proses_caesar_dekripsi(teks, kunci)
                
                hasil = caesarChiper_dekripsi(teks, kunci)        
                print(f"✅ Hasil Dekripsi: {hasil}")

            else:
                print("Aksi tidak dikenal. Batal.")
        
            break
        else:
            print("\nKunci harus berupa angka")

    input("\nTekan Enter untuk kembali ke Menu Utama...")
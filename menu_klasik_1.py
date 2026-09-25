# Nilai ASCII
# 'A' = 65, 'a' = 97
# Kapital dari 65 sampai 90
# kecil dari 97 sampai 122

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
    # mengubah nilai kunci menjadi int dengan cara di casting
    kunci = int(kunci)
    
    for karakter in plaintext:
        # mengecek apakah karakter (yang didapat dari loop ini) merupakan huruf
        if(karakter.isalpha()):
            # cek apakah hurufnya besar atau kecil
            # Jika huruf besar
            if(karakter.isupper()):
                # rumus enkripsi C=(p+k) % 26 karena mengikuti ASCII jadi perlu penyesuaian dengan 
                # ord('A) = menghasilkan bilangan dari si A di ASCII / si 'A' ini bilangan ke sekian di ASCII
                chiper = ((ord(karakter) - ord('A') + kunci) % 26) + ord('A')
            # jika huruf kecil
            else:
                # sama kayak yang huruf kapital/besar cuman ini dari 'a'
                chiper = ((ord(karakter) - ord('a') + kunci) % 26) + ord('a')

            # chiper nanti menghasilkan bilangan/int dengan casting chr() diubah menjadi char yang sesuai sama nilai/urutannya di ASCII
            # hasil casting langsung dimasukkin ke variabel cipherText
            cipherText += chr(chiper)

        # mengecek apakah karakter (yang didapat dari loop ini) merupakan angka  
        elif(karakter.isdigit()):
            # kurang lebih sama tapi karena ini digit yang ada cuman 0-9 berarti 10 digit saja
            chiper = ((int(karakter) + kunci) % 10)
            # karena ga bisa nambahin int langsung jadi di casting dulu dan langsung ditambahkan ke variabel cipherText
            cipherText += str(chiper)

        # mengecek apakah karakter (yang didapat dari loop ini) bukan angka ataupun huruf
        else:
            # selain karater huruf dan angka diabaikan / tidak diubah
            cipherText += karakter

    # mengembalikkan nilai yang ada di variabel cipherText
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
    # prosesnya kurang lebih sama kayak yang enkripsi bedanya cuman di rumusnya
    # karena geser ke kiri rumusnya jadi di kurang
    plainText = ""
    kunci = int(kunci)
    
    for karakter in chipertext:
        if(karakter.isalpha()):
            if(karakter.isupper()):
                # rumus dekripsi P=(C-K) modulo 26 
                plain = ((ord(karakter) - ord('A') - kunci) % 26) + ord('A')
            else:
                # rumus dekripsi P=(C-K) modulo 26
                plain = ((ord(karakter) - ord('a') - kunci) % 26) + ord('a')
            plainText += chr(plain)
            
        elif(karakter.isdigit()):
            # rumus dekripsi P=(C-K) modulo 10
            plain = ((int(karakter) - kunci) % 10)
            plainText += str(plain)
            
        else:
            # langsung di masukkin ke variabel bos
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
                # rumus dekripsi C=(P-K) modulo 26
                chiper = ((ord(karakter) - ord('A') + kunci) % 26) + ord('A')
            else:
                # rumus dekripsi C=(P-K) modulo 26
                chiper = ((ord(karakter) - ord('a') + kunci) % 26) + ord('a')
            print(f"{karakter} -> {chr(chiper)}")
            
        elif(karakter.isdigit()):
            # rumus dekripsi C=(P-K) modulo 10
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
    # casting kunci ke int
    kunci = int(kunci)
    print(f"\n[PROSES] Menggeser karakter sebanyak {kunci} langkah ke kiri...")
    
    for karakter in chipertext:
        if(karakter.isalpha()):
            if(karakter.isupper()):
                # rumus dekripsi P=(C-K) modulo 26
                plain = ((ord(karakter) - ord('A') - kunci) % 26) + ord('A')
            else:
                # rumus dekripsi P=(C-K) modulo 26
                plain = ((ord(karakter) - ord('a') - kunci) % 26) + ord('a')
            print(f"{karakter} -> {chr(plain)}")
            
        elif(karakter.isdigit()):
            # rumus dekripsi P=(C-K) modulo 10
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

def vegenere_enkripsi(plainText: str, kunci: str) -> str:
    """
    Algoritma Vigenere: Proses Enkripsi
    
    Args:
        plainText (str) : Teks asli yang mau dienkripsi
        kunci (str) : Kata kunci pergeseran karakter (alfabet)
    
    Returns:
        str: Ciphertext hasil enkripsi
    """
    chiperText = ""
    kunci = kunci.upper()
    key_idx = 0
    
    for char in plainText:
        if char.isalpha():
            shift = ord(kunci[key_idx % len(kunci)]) - ord('A')
            base = ord('A') if char.isupper() else ord('a')
            
            c = chr((ord(char) - base + shift) % 26 + base)
            chiperText += c
            key_idx += 1
        else:
            chiperText += char
            
    return chiperText


def vegenere_dekripsi(chipertext: str, kunci: str) -> str:
    """
    Algoritma Vigenere: Proses Dekripsi

    Args:
        chipertext (str) : Ciphertext yang mau didekripsi
        kunci (str) : Kata kunci pergeseran karakter (alfabet)

    Returns:
        str: Plaintext hasil dekripsi
    """
    plainText = ""
    kunci = kunci.upper()
    key_idx = 0
    
    for char in chipertext:
        if char.isalpha():
            shift = ord(kunci[key_idx % len(kunci)]) - ord('A')
            base = ord('A') if char.isupper() else ord('a')
            
            p = chr((ord(char) - base - shift + 26) % 26 + base)
            plainText += p
            key_idx += 1
        else:
            plainText += char
            
    return plainText


def proses_vegenere_enkripsi(plainText: str, kunci: str):
    """Menampilkan langkah-langkah detail proses enkripsi.
        Args:
            chipertext (str) : Ciphertext yang mau didekripsi
            kunci (str) : Kata kunci pergeseran karakter (alfabet)
    """

    print("\n--- DETAIL PROSES ENKRIPSI ---")
    kunci = kunci.upper()
    key_idx = 0
    
    for char in plainText:
        if char.isalpha():
            k_char = kunci[key_idx % len(kunci)]
            shift = ord(k_char) - ord('A')
            base = ord('A') if char.isupper() else ord('a')
            
            p_val = ord(char) - base
            c_val = (p_val + shift) % 26
            c_char = chr(c_val + base)
            
            print(f"P: '{char}' ({p_val:2}) + K: '{k_char}' ({shift:2}) -> ({p_val:2} + {shift:2}) mod 26 = {c_val:2} -> C: '{c_char}'")
            key_idx += 1
        else:
            print(f"'{char}' bukan alfabet, karakter tidak dienkripsi.")
    print("-" * 30)


def proses_vegenere_dekripsi(chipertext: str, kunci: str):
    """Menampilkan langkah-langkah detail proses enkripsi.
        Args:
            chipertext (str) : Ciphertext yang mau didekripsi
            kunci (str) : Kata kunci pergeseran karakter (alfabet)
    """

    print("\n--- DETAIL PROSES DEKRIPSI ---")
    kunci = kunci.upper()
    key_idx = 0
    
    for char in chipertext:
        if char.isalpha():
            k_char = kunci[key_idx % len(kunci)]
            shift = ord(k_char) - ord('A')
            base = ord('A') if char.isupper() else ord('a')
            
            c_val = ord(char) - base
            p_val = (c_val - shift + 26) % 26
            p_char = chr(p_val + base)
            
            print(f"C: '{char}' ({c_val:2}) - K: '{k_char}' ({shift:2}) -> ({c_val:2} - {shift:2} + 26) mod 26 = {p_val:2} -> P: '{p_char}'")
            key_idx += 1
        else:
            print(f"'{char}' bukan alfabet, karakter tetap.")
    print("-" * 30)


def jalankan():
    print("\n--- Algoritma KLASIK Vigenere Cipher ---")
    teks = input("Masukkan teks (Plaintext/Ciphertext): ")

    while True:
        kunci = input("Masukkan kunci (berupa kata/huruf): ")

        if kunci.isalpha():
            print("\nPilih Aksi:")
            print("1. Enkripsi")
            print("2. Dekripsi")
            aksi = input("Pilihan (1/2): ")

            if aksi == "1":
                # Panggil fungsi cetak proses step-by-step
                proses_vegenere_enkripsi(teks, kunci)
                
                hasil = vegenere_enkripsi(teks, kunci)        
                print(f"\n✅ Hasil Enkripsi: {hasil}")

            elif aksi == "2":
                # Panggil fungsi cetak proses step-by-step
                proses_vegenere_dekripsi(teks, kunci)
                
                hasil = vegenere_dekripsi(teks, kunci)        
                print(f"\n✅ Hasil Dekripsi: {hasil}")

            else:
                print("Aksi tidak dikenal. Batal.")
        
            break
        else:
            print("\nError: Kunci untuk Vigenere harus berupa alfabet/huruf, tidak boleh angka atau spasi!")

    input("\nTekan Enter untuk kembali ke Menu Utama...")
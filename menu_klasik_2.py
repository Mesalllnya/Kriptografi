# Nilai ASCII
# 'A' = 65, 'a' = 97
# Kapital dari 65 sampai 90
# kecil dari 97 sampai 122

def vigenere_enkripsi(plainText: str, kunci: str) -> str:
    """
    Algoritma Vigenere: Proses Enkripsi
    
    Args:
        plainText (str) : Teks asli yang mau dienkripsi
        kunci (str) : Kata kunci pergeseran karakter (alfabet dan/atau angka)
    
    Returns:
        str: Ciphertext hasil enkripsi
    """
    chiperText = ""
    # Menyamakan format kunci menjadi huruf kapital semua
    kunci = kunci.upper()
    key_idx = 0
    
    for char in plainText:
        # cek char it huruf/angka/karakter lain
        if char.isalpha() or char.isdigit():
            # Menentukan karakter kunci saat ini
            # kalau urutan kunci sudah habis akan mulai dari yang awal lagi
            k_char = kunci[key_idx % len(kunci)]
            
            # Hitung nilai pergeseran (shift)
            if k_char.isalpha():
                # menentukan key nya
                # menghitung nilai aslinya 
                shift = ord(k_char) - ord('A')
            else: # jika k_char adalah angka
                shift = int(k_char)
                
            # JIKA KARAKTER ADALAH HURUF
            if char.isalpha():
                # jika char berupa huruf kapital akan menggunakan niali dari kapital di ASCII
                base = ord('A') if char.isupper() else ord('a')
                # rumusnya C=(P+K) mod 26 jadi (P+K-base(dari ASCII huruf kapital/kecil)) mod 26 + base
                c = chr((ord(char) - base + shift) % 26 + base)
                chiperText += c
                
            # JIKA KARAKTER ADALAH ANGKA
            elif char.isdigit():
                # C=(P+K) mod 10
                c = str((int(char) + shift) % 10)
                chiperText += c
                
            key_idx += 1 # Lanjut ke karakter key berikutnya
        else:
            chiperText += char
            
    return chiperText


def vigenere_dekripsi(chipertext: str, kunci: str) -> str:
    """
    Algoritma Vigenere: Proses Dekripsi

    Args:
        chipertext (str) : Ciphertext yang mau didekripsi
        kunci (str) : Kata kunci pergeseran karakter (alfabet dan/atau angka)

    Returns:
        str: Plaintext hasil dekripsi
    """
    plainText = ""
    kunci = kunci.upper()
    key_idx = 0
    
    for char in chipertext:
        if char.isalpha() or char.isdigit():
            # Tentukan nilai karakter dari kunci saat ini
            k_char = kunci[key_idx % len(kunci)]
            
            # Menentukan shift
            if k_char.isalpha():
                # menentukan key nya
                shift = ord(k_char) - ord('A')
            else:
                shift = int(k_char)
                
            # DEKRIPSI HURUF
            if char.isalpha():
                # jika char berupa huruf kapital akan menggunakan niali dari kapital di ASCII
                base = ord('A') if char.isupper() else ord('a')
                # rumusnya P=(C-K) mod 26 jadi (P-K-base(dari ASCII huruf kapital/kecil)+26) mod 26 + base
                # +26 untuk mencari selisihnya / pokoknya biar ga negatif 
                p = chr((ord(char) - base - shift + 26) % 26 + base)
                plainText += p
                
            # DEKRIPSI ANGKA
            elif char.isdigit():
                # rumusnya C=(P+K) mod 26 jadi (P+K) mod 10                
                p = str((int(char) - shift) % 10)
                plainText += p
                
            key_idx += 1
        else:
            plainText += char
            
    return plainText


def proses_vigenere_enkripsi(plainText: str, kunci: str):
    """Menampilkan langkah-langkah detail proses enkripsi."""
    print("\n--- DETAIL PROSES ENKRIPSI ---")
    kunci = kunci.upper()
    
    # === PEMETAAN KUNCI ===
    kunci_sejajar = "" 
    temp_idx = 0 #urutannya
    for char in plainText:
        if char.isalpha() or char.isdigit():
            # menginputkan kunci yang sudah di urutkan
            kunci_sejajar += kunci[temp_idx % len(kunci)]
            temp_idx += 1 #melanjutkan urutan
        else:
            kunci_sejajar += char  # Spasi/simbol disamakan agar layout rapi
            
    print("Pemetaan Kunci terhadap Teks:")
    print(f"Plaintext : {plainText}")
    print(f"Key       : {kunci_sejajar}\n")
    # ============================================

    key_idx = 0
    for char in plainText:
        if char.isalpha() or char.isdigit():
            # Tentukan nilai karakter dari kunci saat ini
            k_char = kunci[key_idx % len(kunci)]

            # Menentukan shift
            if k_char.isalpha():
                shift = ord(k_char) - ord('A')
            else:
                shift = int(k_char)
                
            if char.isalpha():
                # base: karakter nya kapital atau bukan
                base = ord('A') if char.isupper() else ord('a')
                # p_val = nilai dari variabel plaintext 
                p_val = ord(char) - base
                # c_val = rumus perhitungannya C=(P+K) mod 26
                c_val = (p_val + shift) % 26
                # c_char = nilai yang disubstitusikan dengan urutan ASCII
                c_char = chr(c_val + base)
                # print p: karakter Plaintext apa + k: keynya -> (penjumlahan plainText + key) mod 26 = hasil -> C: chipertext nya
                print(f"[HURUF] P: '{char}' ({p_val:2}) + K: '{k_char}' ({shift:2}) -> ({p_val:2} + {shift:2}) mod 26 = {c_val:2} -> C: '{c_char}'")
                
            elif char.isdigit():
                p_val = int(char)
                c_val = (p_val + shift) % 10
                # sama kek sebelumnya cuman yang angka
                print(f"[ANGKA] P: '{char}' ({p_val:2}) + K: '{k_char}' ({shift:2}) -> ({p_val:2} + {shift:2}) mod 10 = {c_val:2} -> C: '{c_val}'")
                
            key_idx += 1
        else:
            print(f"[LAIN] '{char}' bukan alfabet/angka, karakter tidak dienkripsi.")
            
    print("-" * 30)


def proses_vigenere_dekripsi(chipertext: str, kunci: str):
    """Menampilkan langkah-langkah detail proses dekripsi."""
    print("\n--- DETAIL PROSES DEKRIPSI ---")
    kunci = kunci.upper()
    
    # === PEMETAAN KUNCI ===
    kunci_sejajar = ""
    temp_idx = 0
    for char in chipertext:
        if char.isalpha() or char.isdigit():
            kunci_sejajar += kunci[temp_idx % len(kunci)]
            temp_idx += 1
        else:
            kunci_sejajar += char  # Spasi/simbol disamakan agar layout rapi
            
    print("Pemetaan Kunci terhadap Teks:")
    print(f"Ciphertext: {chipertext}")
    print(f"Key       : {kunci_sejajar}\n")
    # ============================================

    key_idx = 0
    for char in chipertext:
        if char.isalpha() or char.isdigit():
            k_char = kunci[key_idx % len(kunci)]
            
            if k_char.isalpha():
                shift = ord(k_char) - ord('A')
            else:
                shift = int(k_char)
                
            if char.isalpha():
                base = ord('A') if char.isupper() else ord('a')
                c_val = ord(char) - base
                p_val = (c_val - shift + 26) % 26
                p_char = chr(p_val + base)
                print(f"[HURUF] C: '{char}' ({c_val:2}) - K: '{k_char}' ({shift:2}) -> ({c_val:2} - {shift:2} + 26) mod 26 = {p_val:2} -> P: '{p_char}'")
                
            elif char.isdigit():
                c_val = int(char)
                p_val = (c_val - shift) % 10
                print(f"[ANGKA] C: '{char}' ({c_val:2}) - K: '{k_char}' ({shift:2}) -> ({c_val:2} - {shift:2}) mod 10 = {p_val:2} -> P: '{p_val}'")
                
            key_idx += 1
        else:
            print(f"[LAIN] '{char}' bukan alfabet/angka, karakter tetap.")
            
    print("-" * 30)


def jalankan():
    print("\n--- Algoritma KLASIK Vigenere Cipher ---")
    teks = input("Masukkan teks (Plaintext/Ciphertext): ")

    while True:
        kunci = input("Masukkan kunci (alfabet dan/atau angka): ")

        if kunci.isalnum():
            print("\nPilih Aksi:")
            print("1. Enkripsi")
            print("2. Dekripsi")
            aksi = input("Pilihan (1/2): ")

            if aksi == "1":
                proses_vigenere_enkripsi(teks, kunci)
                hasil = vigenere_enkripsi(teks, kunci)        
                print(f"\n✅ Hasil Enkripsi: {hasil}")

            elif aksi == "2":
                proses_vigenere_dekripsi(teks, kunci)
                hasil = vigenere_dekripsi(teks, kunci)        
                print(f"\n✅ Hasil Dekripsi: {hasil}")

            else:
                print("Aksi tidak dikenal. Batal.")
        
            break
        else:
            print("\nError: Kunci untuk Vigenere harus berupa alfabet/angka, tidak boleh ada spasi atau simbol!")

    input("\nTekan Enter untuk kembali ke Menu Utama...")


# if __name__ == "__main__":
#     jalankan()
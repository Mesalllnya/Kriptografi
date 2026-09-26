# ================================================
# VIGENERE CIPHER - Algoritma Klasik Kriptografi
# ================================================
# Konsep dasar: mirip Caesar Cipher, tetapi nilai pergeseran (shift) tidak tetap,
# melainkan mengikuti setiap huruf pada kata kunci yang diulang sepanjang teks.
# Nilai ASCII acuan:
#   'A' = 65, 'Z' = 90   -> huruf kapital
#   'a' = 97, 'z' = 122  -> huruf kecil
#   '0' = 48, '9' = 57   -> angka (dihitung menggunakan int(), bukan ord())

def vigenere_enkripsi(plainText: str, kunci: str) -> str:
    """
    Algoritma Vigenere: Proses Enkripsi

    Args:
        plainText (str) : Teks asli yang akan dienkripsi
        kunci (str) : Kata kunci pergeseran karakter (alfabet dan/atau angka)

    Returns:
        str: Ciphertext hasil enkripsi
    """
    chiperText = ""
    # kunci disamakan menjadi huruf kapital seluruhnya agar perhitungan ord('A') konsisten
    kunci = kunci.upper()
    # key_idx menandai posisi karakter kunci yang sedang digunakan, terpisah dari posisi karakter teks
    # karena karakter non-alfanumerik pada teks tidak ikut menggeser posisi kunci
    key_idx = 0

    for char in plainText:
        # hanya huruf dan angka yang diproses; karakter lain akan ditangani pada blok else di bawah
        if char.isalpha() or char.isdigit():
            # menentukan karakter kunci yang berlaku untuk posisi ini
            # operator modulo (%) membuat kunci "berulang" begitu panjangnya sudah terlampaui
            # contoh: kunci "ABC" pada karakter ke-4 akan kembali memakai kunci[0], yaitu 'A'
            k_char = kunci[key_idx % len(kunci)]

            # menghitung nilai pergeseran (shift) berdasarkan karakter kunci saat ini
            if k_char.isalpha():
                # apabila karakter kunci berupa huruf, nilai pergeseran diambil dari posisi hurufnya (A=0, B=1, dst)
                shift = ord(k_char) - ord('A')
            else:
                # apabila karakter kunci berupa angka, nilai pergeseran adalah angka itu sendiri
                shift = int(k_char)

            # PROSES UNTUK KARAKTER HURUF
            if char.isalpha():
                # base menentukan titik acuan ASCII, tergantung huruf kapital atau huruf kecil
                base = ord('A') if char.isupper() else ord('a')
                # Rumus: C = (P + K) mod 26
                # (ord(char) - base) mengubah huruf menjadi posisi 0-25 terlebih dahulu,
                # baru kemudian ditambah shift, dimodulo 26, dan dikembalikan ke kode ASCII aslinya
                c = chr((ord(char) - base + shift) % 26 + base)
                chiperText += c

            # PROSES UNTUK KARAKTER ANGKA
            elif char.isdigit():
                # Rumus: C = (P + K) mod 10, karena rentang angka hanya 0-9 (10 kemungkinan)
                c = str((int(char) + shift) % 10)
                chiperText += c

            # posisi kunci hanya dimajukan apabila karakter yang diproses adalah huruf/angka
            key_idx += 1
        else:
            # spasi, tanda baca, dan simbol lain tidak dienkripsi dan tidak menggeser posisi kunci
            chiperText += char

    return chiperText


def vigenere_dekripsi(chipertext: str, kunci: str) -> str:
    """
    Algoritma Vigenere: Proses Dekripsi

    Args:
        chipertext (str) : Ciphertext yang akan didekripsi
        kunci (str) : Kata kunci pergeseran karakter (alfabet dan/atau angka)

    Returns:
        str: Plaintext hasil dekripsi
    """
    plainText = ""
    kunci = kunci.upper()
    key_idx = 0

    for char in chipertext:
        if char.isalpha() or char.isdigit():
            # logika penentuan kunci identik dengan proses enkripsi
            k_char = kunci[key_idx % len(kunci)]

            if k_char.isalpha():
                shift = ord(k_char) - ord('A')
            else:
                shift = int(k_char)

            # DEKRIPSI UNTUK HURUF
            if char.isalpha():
                base = ord('A') if char.isupper() else ord('a')
                # Rumus: P = (C - K) mod 26
                # ditambahkan +26 sebelum modulo agar hasil pengurangan yang bernilai negatif
                # tetap dikonversi menjadi nilai positif yang benar (Python sebenarnya sudah menangani
                # modulo pada bilangan negatif dengan benar, namun +26 ditambahkan agar lebih eksplisit dan mudah dibaca)
                p = chr((ord(char) - base - shift + 26) % 26 + base)
                plainText += p

            # DEKRIPSI UNTUK ANGKA
            elif char.isdigit():
                # Rumus: P = (C - K) mod 10
                p = str((int(char) - shift) % 10)
                plainText += p

            key_idx += 1
        else:
            plainText += char

    return plainText


def proses_vigenere_enkripsi(plainText: str, kunci: str):
    """ Menampilkan langkah-langkah detail proses enkripsi, termasuk pemetaan kunci terhadap teks. """
    print("\n--- DETAIL PROSES ENKRIPSI ---")
    kunci = kunci.upper()

    # === PEMETAAN KUNCI ===
    # bagian ini bertujuan menampilkan kunci yang sudah "diselaraskan" persis di bawah teks aslinya,
    # sehingga pengguna dapat melihat karakter kunci mana yang digunakan untuk setiap huruf/angka
    kunci_sejajar = ""
    temp_idx = 0  # penghitung posisi kunci, terpisah dari posisi karakter teks
    for char in plainText:
        if char.isalpha() or char.isdigit():
            kunci_sejajar += kunci[temp_idx % len(kunci)]
            temp_idx += 1
        else:
            # spasi/simbol pada teks diberi karakter yang sama pada baris kunci
            # semata-mata agar tampilan sejajar dan mudah dibaca, bukan bagian dari perhitungan
            kunci_sejajar += char

    print("Pemetaan Kunci terhadap Teks:")
    print(f"Plaintext : {plainText}")
    print(f"Key       : {kunci_sejajar}\n")
    # ============================================

    key_idx = 0
    for char in plainText:
        if char.isalpha() or char.isdigit():
            k_char = kunci[key_idx % len(kunci)]

            if k_char.isalpha():
                shift = ord(k_char) - ord('A')
            else:
                shift = int(k_char)

            if char.isalpha():
                base = ord('A') if char.isupper() else ord('a')
                p_val = ord(char) - base       # posisi huruf asli dalam rentang 0-25
                c_val = (p_val + shift) % 26   # hasil perhitungan Vigenere
                c_char = chr(c_val + base)     # dikonversi kembali menjadi huruf
                # baris print berikut menampilkan rincian perhitungan agar mudah ditelusuri/diverifikasi
                print(f"[HURUF] P: '{char}' ({p_val:2}) + K: '{k_char}' ({shift:2}) -> ({p_val:2} + {shift:2}) mod 26 = {c_val:2} -> C: '{c_char}'")

            elif char.isdigit():
                p_val = int(char)
                c_val = (p_val + shift) % 10
                print(f"[ANGKA] P: '{char}' ({p_val:2}) + K: '{k_char}' ({shift:2}) -> ({p_val:2} + {shift:2}) mod 10 = {c_val:2} -> C: '{c_val}'")

            key_idx += 1
        else:
            print(f"[LAIN] '{char}' bukan alfabet/angka, karakter tidak dienkripsi.")

    print("-" * 30)


def proses_vigenere_dekripsi(chipertext: str, kunci: str):
    """ Menampilkan langkah-langkah detail proses dekripsi, termasuk pemetaan kunci terhadap teks. """
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
            kunci_sejajar += char

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
    """
    Fungsi utama yang menjalankan program dari sisi pengguna (menu interaktif pada terminal)
    Alur program: input teks -> input kunci -> pemilihan aksi -> tampilan proses -> hasil ->
    menawarkan pengulangan, sehingga program tidak perlu dijalankan kembali dari luar
    """
    print("\n--- Algoritma KLASIK Vigenere Cipher ---")

    # perulangan utama, memungkinkan proses diulang tanpa keluar dari fungsi
    while True:
        teks = input("\nMasukkan teks (Plaintext/Ciphertext): ")

        # validasi agar teks kosong (atau hanya berisi spasi) tidak diproses lebih lanjut
        if teks.strip() == "":
            print("Teks tidak boleh kosong. Silakan coba kembali.")
            continue

        # perulangan khusus untuk validasi kunci, terpisah dari perulangan utama
        while True:
            kunci = input("Masukkan kunci (alfabet dan/atau angka): ")

            # kunci Vigenere tidak boleh kosong, dan hanya boleh berisi huruf/angka (tanpa spasi atau simbol)
            # karena setiap karakter kunci harus dapat diproses sebagai penentu nilai pergeseran (shift)
            if kunci != "" and kunci.isalnum():
                break
            else:
                print("Error: Kunci untuk Vigenere harus berupa alfabet/angka, tidak boleh kosong, tidak boleh ada spasi atau simbol!")

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
            # apabila pilihan aksi tidak dikenali, proses dibatalkan namun program tidak langsung berhenti
            print("Aksi tidak dikenal. Proses dibatalkan.")

        # menanyakan kepada pengguna apakah ingin mengulang proses atau mengakhiri program
        # bagian inilah yang membuat menu dapat berjalan secara berulang (looping)
        ulang = input("\nApakah ingin mencoba kembali? (y/n): ").strip().lower()
        if ulang != "y":
            break

    print("\nKembali ke Menu Utama...")


# if __name__ == "__main__":
#     jalankan()
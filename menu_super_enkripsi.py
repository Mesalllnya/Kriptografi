import menu_klasik_1 as mk1
import menu_klasik_2 as mk2
import menu_modern_1 as md1
import menu_modern_2 as md2


# Semua Algoritma Kudu punya ini
def algoritmaKu(plainText: str) -> str:
    # Kalau udah dibikin fungsinya terus ketik " 3 kali biar bikin autodocstringnya kayak dibawah
    cipherText = ""
    return cipherText


def jalankan():
    """_summary_
    Menjalankan Algoritma Super yang menggabungkan
    4 Algoritma Kriptografi:

    1. Caesar Cipher
    2. Vigenere
    3. Modern Erlan 1
    4. Modern Erlan 2

    """
    print("\n--- Algoritma Super ---")
    teks = input("Masukkan teks (Plaintext/Ciphertext) \nKHUSUS SUPERENRKRIPSI: ")

    while True:
        print("\nPilih Aksi:")
        print("1. Enkripsi")
        print("2. Dekripsi")
        aksi = input("Pilihan (1/2): ")

        if aksi == "1":
            # 1. Mengenkripsi Menggunakan Caesar Cipher terlebih dahulu
            kunci = input("Masukkan kunci (geser): ")
            while not kunci.isdigit():
                kunci = input("Masukkan kunci (geser): ")
            kunci = int(kunci)
            hasilCaesar = mk1.caesarChiper_enkripsi(teks, kunci)
            mk1.proses_caesar_enkripsi(teks, kunci)

            # 2. Hasil Caesar Cipher digunakan untuk Vignere
            kunci = input("Masukkan kunci (Huruf): ")
            hasilVigenere = mk2.vigenere_enkripsi(hasilCaesar, kunci)
            mk2.proses_vigenere_enkripsi(hasilCaesar, kunci)

            # 3. Hasil Vignere digunakan untuk Modern 1
            hasilRSA = md1.enkripsiRSA(hasilVigenere)

            # 4. Hasil modern 1 digunakan untuk Modern 2
            hasilAES = md2.enkripsiAES(hasilRSA)

            # Print Hasil Enkripsi
            print("Hasil Enkripsi: ", hasilAES)

        elif aksi == "2":
            # 1. Deskripsi dimulai dari modern 2
            dekripsiAES = md2.dekripsiAES(teks)

            # 2. Deskripsi Modern 1
            dekripsiRSA = md1.dekripsiRSA(dekripsiAES)

            # 3. Deskripsi Vigenere
            kunci = input("Masukkan kunci (Huruf): ")
            hasilVigenere = mk2.vigenere_dekripsi(dekripsiRSA, kunci)
            mk2.proses_vigenere_dekripsi(teks, kunci)

            # 4. Deskripsi Caesar (Final)
            kunci = input("Masukkan kunci (geser): ")
            while not kunci.isdigit():
                kunci = input("Masukkan kunci (geser): ")
            kunci = int(kunci)
            hasilCaesar = mk1.caesarChiper_dekripsi(hasilVigenere, kunci)
            mk1.proses_caesar_dekripsi(hasilVigenere, kunci)

            # Print Hasil Deskripsi
            print("Hasil Deskripsi: ", hasilVigenere)

        else:
            print("Aksi tidak dikenal. Batal.")

        break

    input("\nTekan Enter untuk kembali ke Menu Utama...")

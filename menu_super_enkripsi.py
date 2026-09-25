import menu_klasik_1 as mk1
import menu_klasik_2 as mk2


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
            hasilVigenere = mk2.vegenere_enkripsi(hasilCaesar, kunci)
            mk2.proses_vegenere_enkripsi(hasilCaesar, kunci)

            # 3. Hasil Vignere digunakan untuk Modern 1

            # 4. Hasil modern 1 digunakan untuk Modern 2

            # Print Hasil Enkripsi
            print("Hasil Enkripsi: ", hasilVigenere)

        elif aksi == "2":
            # 1. Deskripsi dimulai dari modern 2

            # 2. Deskripsi Modern 1
            hasilModern1 = "apalah"

            # 3. Deskripsi Vigenere
            # FIXME - Sementara kuganti teks biar bisa ngetest
            kunci = input("Masukkan kunci (Huruf): ")
            hasilVigenere = mk2.vegenere_dekripsi(teks, kunci)
            mk2.proses_vegenere_dekripsi(teks, kunci)

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

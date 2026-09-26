import menu_klasik_1 as mk1
import menu_klasik_2 as mk2
import menu_modern_1 as md1
import menu_modern_2 as md2

# ================================================
# ALGORITMA SUPER - Gabungan 4 Lapis Kriptografi
# ================================================
# Konsep dasar: teks diproses secara berlapis (multi-layer encryption) melalui 4 algoritma
# berbeda secara berurutan. Semakin banyak lapisan, semakin sulit ciphertext dipecahkan,
# karena penyerang harus mematahkan seluruh lapisan, bukan hanya satu algoritma saja.
#
# Urutan pada proses ENKRIPSI:
#   Plaintext -> [1] Caesar Cipher -> [2] Vigenere -> [3] RSA -> [4] AES -> Ciphertext akhir
#
# Urutan pada proses DEKRIPSI merupakan kebalikannya (LIFO / last-in-first-out),
# karena lapisan yang terakhir dipasang pada saat enkripsi harus dibuka terlebih dahulu:
#   Ciphertext akhir -> [1] AES -> [2] RSA -> [3] Vigenere -> [4] Caesar Cipher -> Plaintext asli


def jalankan():
    """
    Menjalankan Algoritma Super yang menggabungkan 4 Algoritma Kriptografi:

    1. Caesar Cipher
    2. Vigenere
    3. RSA
    4. AES-128

    Alur program: input teks -> pemilihan aksi (enkripsi/dekripsi) -> proses berlapis
    sesuai urutan di atas -> hasil akhir -> menawarkan pengulangan
    """
    print("\n--- Algoritma Super ---")

    # perulangan utama, agar program dapat mengulang proses tanpa harus dijalankan kembali dari luar
    while True:
        teks = input("\nMasukkan teks (Plaintext/Ciphertext)\nKHUSUS SUPERENKRIPSI: ")

        # validasi agar teks kosong (atau hanya berisi spasi) tidak diproses lebih lanjut,
        # karena teks kosong yang diproses hingga lapisan RSA/AES dapat menimbulkan error
        if teks.strip() == "":
            print("Teks tidak boleh kosong. Silakan coba kembali.")
            continue

        print("\nPilih Aksi:")
        print("1. Enkripsi")
        print("2. Dekripsi")
        aksi = input("Pilihan (1/2): ")

        if aksi == "1":
            # ==========================================================
            # PROSES ENKRIPSI (Caesar -> Vigenere -> RSA -> AES)
            # ==========================================================

            # 1. Mengenkripsi menggunakan Caesar Cipher terlebih dahulu
            kunci_caesar = input("Masukkan kunci Caesar (geser): ")
            # perulangan validasi hingga kunci yang dimasukkan benar-benar berupa angka
            while not kunci_caesar.isdigit():
                print("Kunci harus berupa angka.")
                kunci_caesar = input("Masukkan kunci Caesar (geser): ")
            kunci_caesar = int(kunci_caesar)

            hasilCaesar = mk1.caesarChiper_enkripsi(teks, kunci_caesar)
            mk1.proses_caesar_enkripsi(teks, kunci_caesar)

            # 2. Hasil Caesar Cipher digunakan sebagai input untuk Vigenere
            kunci_vigenere = input("Masukkan kunci Vigenere (Huruf/Angka): ")
            # validasi agar kunci Vigenere tidak kosong dan hanya berisi huruf/angka,
            # sesuai syarat pada modul vigenere (tidak boleh spasi atau simbol)
            while kunci_vigenere == "" or not kunci_vigenere.isalnum():
                print("Kunci Vigenere tidak boleh kosong dan harus berupa huruf/angka tanpa spasi atau simbol.")
                kunci_vigenere = input("Masukkan kunci Vigenere (Huruf/Angka): ")

            hasilVigenere = mk2.vigenere_enkripsi(hasilCaesar, kunci_vigenere)
            mk2.proses_vigenere_enkripsi(hasilCaesar, kunci_vigenere)

            # 3. Hasil Vigenere digunakan sebagai input untuk RSA
            # RSA di sini tidak memerlukan input kunci tambahan dari pengguna,
            # karena kunci publik (e, n) sudah didefinisikan secara tetap di dalam modul md1
            hasilRSA = md1.enkripsiRSA(hasilVigenere)

            # 4. Hasil RSA digunakan sebagai input untuk AES (lapisan terakhir)
            # sama seperti RSA, AES di sini menggunakan key tetap yang sudah didefinisikan di modul md2
            hasilAES = md2.enkripsiAES(hasilRSA)

            # menampilkan hasil akhir setelah melalui keempat lapisan enkripsi
            print("\n✅ Hasil Enkripsi: ", hasilAES)

        elif aksi == "2":
            # ==========================================================
            # PROSES DEKRIPSI (AES -> RSA -> Vigenere -> Caesar)
            # ==========================================================
            # urutan pembukaan lapisan harus terbalik dari urutan enkripsi,
            # sebab lapisan AES adalah lapisan terluar (dipasang terakhir saat enkripsi),
            # sehingga harus dibuka terlebih dahulu, dan seterusnya hingga lapisan Caesar

            # 1. Dekripsi dimulai dari lapisan AES (lapisan paling luar)
            dekripsiAES = md2.dekripsiAES(teks)

            # apabila dekripsi AES gagal (mengembalikan string kosong), proses dihentikan
            # agar tidak melanjutkan dekripsi dengan data yang sudah tidak valid ke lapisan berikutnya
            if dekripsiAES == "":
                print("Proses dekripsi dihentikan karena lapisan AES gagal diproses.")
            else:
                # 2. Dekripsi lapisan RSA, menggunakan hasil dekripsi AES sebagai input
                dekripsiRSA = md1.dekripsiRSA(dekripsiAES)

                if dekripsiRSA == "":
                    print("Proses dekripsi dihentikan karena lapisan RSA gagal diproses.")
                else:
                    # 3. Dekripsi lapisan Vigenere
                    kunci_vigenere = input("Masukkan kunci Vigenere (Huruf/Angka): ")
                    while kunci_vigenere == "" or not kunci_vigenere.isalnum():
                        print("Kunci Vigenere tidak boleh kosong dan harus berupa huruf/angka tanpa spasi atau simbol.")
                        kunci_vigenere = input("Masukkan kunci Vigenere (Huruf/Angka): ")

                    hasilVigenere = mk2.vigenere_dekripsi(dekripsiRSA, kunci_vigenere)
                    mk2.proses_vigenere_dekripsi(dekripsiRSA, kunci_vigenere)

                    # 4. Dekripsi lapisan Caesar (lapisan terdalam / paling awal dipasang saat enkripsi)
                    kunci_caesar = input("Masukkan kunci Caesar (geser): ")
                    while not kunci_caesar.isdigit():
                        print("Kunci harus berupa angka.")
                        kunci_caesar = input("Masukkan kunci Caesar (geser): ")
                    kunci_caesar = int(kunci_caesar)

                    hasilCaesar = mk1.caesarChiper_dekripsi(hasilVigenere, kunci_caesar)
                    mk1.proses_caesar_dekripsi(hasilVigenere, kunci_caesar)

                    # menampilkan hasil akhir setelah keempat lapisan berhasil dibuka,
                    # yang seharusnya berupa plaintext asli sebelum proses superenkripsi
                    print("\n✅ Hasil Dekripsi: ", hasilCaesar)

        else:
            print("Aksi tidak dikenal. Proses dibatalkan.")

        # menanyakan kepada pengguna apakah ingin mengulang proses atau mengakhiri program
        # bagian inilah yang membuat menu dapat berjalan secara berulang (looping)
        ulang = input("\nApakah ingin mencoba kembali? (y/n): ").strip().lower()
        if ulang != "y":
            break

    input("\nTekan Enter untuk kembali ke Menu Utama...")
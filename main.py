import sys
import menu_klasik_1
import menu_klasik_2
import menu_modern_1
import menu_modern_2
import menu_super_enkripsi


def main():
    while True:
        print("\n" + "=" * 40)
        print(
            "\033[1;31mAPLIKASI KRIPTOGRAFI KELOMPOK SANGAR YK \n\tIfsalll, Erlan, Roi, Nahdi \033[0m"
        )
        print("=" * 40)
        print("1. Klasik 1 (Contoh: Caesar Cipher)\033[0m")
        print("2. Klasik 2 (Contoh: Vigenere Cipher)")
        print("3. Modern 1 (Contoh: AES)")
        print("4. Modern 2 (Contoh: DES)")
        print("5. Super Enkripsi (Gabungan 4 Algoritma)")
        print("\033[5;91m0. Keluar\033[0m")
        print("=" * 40)

        pilihan = input("Pilih menu (0-5): ")

        if pilihan == "1":
            menu_klasik_1.jalankan()
        elif pilihan == "2":
            menu_klasik_2.jalankan()
        elif pilihan == "3":
            menu_modern_1.jalankan()
        elif pilihan == "4":
            menu_modern_2.jalankan()
        elif pilihan == "5":
            menu_super_enkripsi.jalankan()
        elif pilihan == "0":
            print("Keluar dari aplikasi!!")
            sys.exit()
        else:
            print("Pilihan tidak valid. Baca menu lagi, ya.")


if __name__ == "__main__":
    main()

import time
import matplotlib.pyplot as plt

def hitung_zakat_rekursif(gaji):
    if gaji <= 0:
        return 0
    return 0.025 * gaji

def hitung_zakat_iteratif(gaji):
    zakat = 0
    if gaji > 0:
        zakat = 0.025 * gaji
    return zakat

def tampilkan_hasil(gaji, zakat_rekursif, waktu_rekursif, zakat_iteratif, waktu_iteratif):
    print("\nHasil Perhitungan Zakat:\n")
    print("+------------------+------------------------+---------------------+------------------------+---------------------+")
    print("| Gaji (IDR)       | Zakat Rekursif (IDR)  | Waktu Rekursif (s)  | Zakat Iteratif (IDR)  | Waktu Iteratif (s)    |")
    print("+------------------+------------------------+---------------------+------------------------+---------------------+")
    for i in range(len(gaji)):
        print(f"| {gaji[i]:<16,} | {zakat_rekursif[i]:<22,.2f} | {waktu_rekursif[i]:<19.6f} | {zakat_iteratif[i]:<22,.2f} | {waktu_iteratif[i]:<19.6f} |")
    print("+------------------+------------------------+---------------------+------------------------+---------------------+")

def plot_grafik(gaji, waktu_rekursif, waktu_iteratif):
    plt.figure(figsize=(10, 6))
    plt.plot(gaji, waktu_rekursif, marker='o', label='Rekursif', color='blue')
    plt.plot(gaji, waktu_iteratif, marker='x', label='Iteratif', color='red')
    plt.title("Perbandingan Waktu Eksekusi Rekursif vs Iteratif Program zakat")
    plt.xlabel("Gaji (IDR)")
    plt.ylabel("Waktu Eksekusi (s)")
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.legend()
    plt.tight_layout()
    plt.show()

def main():
    gaji = []
    zakat_rekursif = []
    waktu_rekursif = []
    zakat_iteratif = []
    waktu_iteratif = []

    while True:
        print("\n====== Menu Program Zakat ====== :")
        print("1. Masukkan Data Gaji")
        print("2. Tampilkan Hasil dan Grafik")
        print("3. Keluar")
        print("===================================")

        pilihan = input("Pilih opsi (1/2/3): ")

        if pilihan == "1":
            try:
                jumlah_data = int(input("Masukkan jumlah data gaji yang akan dihitung: "))

                for _ in range(jumlah_data):
                    nilai_gaji = float(input("Masukkan jumlah gaji penghasilan Anda (dalam IDR): "))

                    if nilai_gaji < 0:
                        print("Gaji tidak boleh negatif. Silakan coba lagi.")
                        continue

                    # Rekursif
                    start = time.time()
                    zakat_r = hitung_zakat_rekursif(nilai_gaji)
                    end = time.time()
                    waktu_r = end - start

                    # Iteratif
                    start = time.time()
                    zakat_i = hitung_zakat_iteratif(nilai_gaji)
                    end = time.time()
                    waktu_i = end - start

                    gaji.append(nilai_gaji)
                    zakat_rekursif.append(zakat_r)
                    waktu_rekursif.append(waktu_r)
                    zakat_iteratif.append(zakat_i)
                    waktu_iteratif.append(waktu_i)

            except ValueError:
                print("Input tidak valid. Harap masukkan angka yang benar untuk gaji.")

        elif pilihan == "2":
            if not gaji:
                print("Belum ada data gaji yang dimasukkan. Silakan pilih opsi 1 terlebih dahulu.")
                continue

            tampilkan_hasil(gaji, zakat_rekursif, waktu_rekursif, zakat_iteratif, waktu_iteratif)
            plot_grafik(gaji, waktu_rekursif, waktu_iteratif)

        elif pilihan == "3":
            print("Terima kasih telah menggunakan program ini. Program selesai.")
            break

        else:
            print("Pilihan tidak valid. Silakan pilih menu yang tersedia.")

if __name__ == "__main__":
    main()

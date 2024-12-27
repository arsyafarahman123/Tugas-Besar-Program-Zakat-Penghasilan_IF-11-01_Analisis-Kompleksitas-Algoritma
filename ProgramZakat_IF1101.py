import time
import matplotlib.pyplot as plt

# Fungsi menghitung zakat penghasilan dari gaji
def hitung_zakat(gaji):
    return gaji * 0.025

# Fungsi rekursif untuk menghitung zakat
def total_zakat_recursive(n, gaji_list):
    if n == 0:
        return 0
    return hitung_zakat(gaji_list[n-1]) + total_zakat_recursive(n-1, gaji_list)

# Fungsi iteratif untuk menghitung zakat
def total_zakat_iterative(gaji_list):
    total_zakat = 0
    for gaji in gaji_list:
        total_zakat += hitung_zakat(gaji)
    return total_zakat

# Data dummy untuk 25 orang dengan gaji tertentu
gaji_list = [
    1500000, 2000000, 2500000, 3000000, 3500000, 
    4000000, 4500000, 5000000, 5500000, 6000000, 
    6500000, 7000000, 7500000, 8000000, 8500000, 
    9000000, 9500000, 10000000, 10500000, 11000000,
    11500000, 12000000, 12500000, 13000000, 13500000
]

# Menampilkan data dummy awal
print("\nDaftar Gaji yang Tersedia:")
for idx, gaji in enumerate(gaji_list, 1):
    print(f"{idx}. Gaji: Rp {gaji}")

# Input jumlah data yang ingin dihitung
print("\nMasukkan jumlah data yang ingin dihitung dan diurutkan pencarian (1-25):")
while True:
    try:
        jumlah_data = int(input("Masukkan jumlah data (1-25): "))
        if 1 <= jumlah_data <= 25:
            break
        else:
            print("Jumlah data harus antara 1 dan 25. Coba lagi.")
    except ValueError:
        print("Masukkan angka yang valid.")

# Input beberapa nilai n yang ingin dihitung dari data
n_values_input = []
print(f"\nMasukkan beberapa nilai n yang ingin dihitung (1 sampai {len(gaji_list)}):")
for i in range(jumlah_data):  # Input sesuai jumlah_data yang dipilih
    while True:
        try:
            n = int(input(f"Masukkan n ke-{i + 1} (1-{len(gaji_list)}): "))
            if 1 <= n <= len(gaji_list):
                n_values_input.append(n)
                break
            else:
                print(f"Jumlah n harus antara 1 dan {len(gaji_list)}. Coba lagi.")
        except ValueError:
            print("Masukkan angka yang valid.")

# Menampilkan gaji yang dipilih untuk dihitung zakatnya
print(f"\nGaji yang akan dihitung zakatnya (Jumlah data: {jumlah_data}):")
for i in n_values_input:
    print(f"Nomor {i}. Gaji: Rp {gaji_list[i - 1]}")

# Variabel untuk menyimpan hasil
recursive_times = []
iterative_times = []

# Loop untuk menghitung waktu eksekusi untuk setiap nilai n yang dimasukkan
print("\nMemproses data...")
for n in n_values_input:  # Untuk setiap nilai n yang dimasukkan
    # Hitung waktu rekursif
    start_recursive = time.time()
    total_zakat_recursive(n, gaji_list[:n])
    recursive_time = time.time() - start_recursive

    # Hitung waktu iteratif
    start_iterative = time.time()
    total_zakat_iterative(gaji_list[:n])
    iterative_time = time.time() - start_iterative

    # Simpan hasil
    recursive_times.append(recursive_time)
    iterative_times.append(iterative_time)

# Cetak hasil
print("\n+-----+---------------------------+---------------------------+")
print("|  n  |   Recursive Time (s)      |   Iterative Time (s)      |")
print("+-----+---------------------------+---------------------------+")
for i in range(len(n_values_input)):
    print(f"| {n_values_input[i]:<4} | {recursive_times[i]:<24.10f} | {iterative_times[i]:<24.10f}  |")
print("+-----+---------------------------+---------------------------+")

# Tampilkan grafik hasil
plt.figure(figsize=(8, 6))
plt.plot(n_values_input, recursive_times, label='Recursive Time', marker='o', linestyle='-')
plt.plot(n_values_input, iterative_times, label='Iterative Time', marker='o', linestyle='--')
plt.title('Perbandingan Waktu Eksekusi (Rekursif vs Iteratif) pada Bubble Sort Program Menghitung Zakat Penghasilan (2,5%)')
plt.xlabel('Jumlah Orang (n)')
plt.ylabel('Execution Time (seconds)')

# Menambahkan label untuk nilai-nilai waktu pada grafik
for i in range(len(n_values_input)):
    # Menampilkan waktu di sebelah kiri titik data
    plt.text(n_values_input[i], recursive_times[i] + 0.00000001, f'{recursive_times[i]:.10f}', ha='center', va='bottom', fontsize=9)
    plt.text(n_values_input[i], iterative_times[i] + 0.00000001, f'{iterative_times[i]:.10f}', ha='center', va='bottom', fontsize=9)



# Menyesuaikan skala sumbu Y untuk rentang waktu kecil
plt.yscale('log')

# Menambahkan nilai pada sumbu Y untuk rentang yang lebih tepat
plt.yticks([0.000005, 0.00001, 0.00002, 0.00005, 0.0001], ["0.000005", "0.00001", "0.00002", "0.00005", "0.0001"])

plt.legend()
plt.grid(True)
plt.show()

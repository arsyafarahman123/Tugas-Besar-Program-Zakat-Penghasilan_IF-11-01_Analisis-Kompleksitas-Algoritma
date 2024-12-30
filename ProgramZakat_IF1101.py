import time
import matplotlib.pyplot as plt


# Fungsi Bubble Sort Iteratif
def bubble_sort_iterative(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


# Fungsi Bubble Sort Rekursif
def bubble_sort_recursive(arr, n=None):
    if n is None:
        n = len(arr)
    if n == 1:
        return
    for i in range(n - 1):
        if arr[i] > arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
    bubble_sort_recursive(arr, n - 1)


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

# Input nilai-nilai n yang ingin dihitung
n_values_input = []
print(f"\nMasukkan beberapa nilai n yang ingin dihitung (1 sampai {len(gaji_list)}):")
for i in range(jumlah_data):
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

# Variabel untuk menyimpan hasil waktu eksekusi
recursive_times = []
iterative_times = []

# Loop untuk menghitung waktu eksekusi untuk setiap nilai n yang dimasukkan
print("\nMemproses data...")
for n in n_values_input:
    # Salin data untuk memastikan konsistensi
    data_iterative = gaji_list[:n]
    data_recursive = gaji_list[:n]

    # Hitung waktu Bubble Sort Iteratif
    start_iterative = time.time()
    bubble_sort_iterative(data_iterative)
    iterative_time = time.time() - start_iterative

    # Hitung waktu Bubble Sort Rekursif
    start_recursive = time.time()
    bubble_sort_recursive(data_recursive)
    recursive_time = time.time() - start_recursive

    # Simpan hasil
    iterative_times.append(iterative_time)
    recursive_times.append(recursive_time)

# Cetak hasil
print("\n+-----+---------------------------+---------------------------+")
print("|  n  |   Recursive Time (s)      |   Iterative Time (s)      |")
print("+-----+---------------------------+---------------------------+")
for i in range(len(n_values_input)):
    print(f"| {n_values_input[i]:<4} | {recursive_times[i]:<24.10f} | {iterative_times[i]:<24.10f}  |")
print("+-----+---------------------------+---------------------------+")

# Tampilkan grafik hasil
plt.figure(figsize=(10, 6))
plt.plot(n_values_input, iterative_times, label='Iterative Bubble Sort', marker='o', linestyle='-')
plt.plot(n_values_input, recursive_times, label='Recursive Bubble Sort', marker='o', linestyle='--')
plt.title('Perbandingan Waktu Eksekusi Bubble Sort (Iteratif vs Rekursif)')
plt.xlabel('Jumlah Data (n)')
plt.ylabel('Execution Time (seconds)')

# Menambahkan label untuk nilai-nilai waktu pada grafik
for i in range(len(n_values_input)):
    plt.text(n_values_input[i], recursive_times[i] + 0.00000001, f'{recursive_times[i]:.10f}', ha='center', va='bottom', fontsize=9)
    plt.text(n_values_input[i], iterative_times[i] + 0.00000001, f'{iterative_times[i]:.10f}', ha='center', va='bottom', fontsize=9)

# Menambahkan legenda dan grid
plt.legend()
plt.grid(True)
plt.show()

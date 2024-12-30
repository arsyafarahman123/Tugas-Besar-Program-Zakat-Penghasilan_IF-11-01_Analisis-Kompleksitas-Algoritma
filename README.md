
# Tugas Akhir: Analisis Kompleksitas Algoritma

## Kelas: IF-11-01

## Anggota Kelompok:
- **Arsya Fathiha Rahman** (2311102152)
- **Grashela Ayudia Prameswari** (2311102318)

---

## Studi Kasus
Studi Kasus Dalam kasus ini, Bubble Sort digunakan untuk mengurutkan data gaji sebelum menghitung zakat. Algoritma ini membandingkan elemen berdekatan dan menukarnya jika diperlukan. Proses ini berlanjut hingga seluruh data terurut. Setelah pengurutan, zakat dihitung menggunakan dua metode: rekursif dan iteratif. Pada metode rekursif, fungsi memanggil dirinya sendiri untuk menghitung zakat, sedangkan metode iteratif menggunakan perulangan untuk menghitung zakat. Kedua metode ini dibandingkan untuk melihat mana yang lebih efisien setelah data diurutkan dengan Bubble Sort.



## Perbandingan 

Program ini membandingkan Waktu Eksekusi **Metode rekursif** dan **iteratif** setelah data diurutkan dengan **Bubble Sort**. Rekursif lebih lambat karena pemanggilan fungsi berulang, sementara iteratif lebih efisien dan lebih cepat. 
Analisis Kinerja: 
1. Bubble Sort: Mengurutkan data gaji, meski sederhana, mempengaruhi waktu eksekusi. 
2. Rekursif: Lebih lambat karena overhead pemanggilan fungsi. 
3. Iteratif: Lebih efisien dan cepat tanpa overhead pemanggilan fungsi.

Perbandingan Performa Dari hasil perbandingan waktu eksekusi, dapat dilihat bahwa metode iteratif cenderung lebih efisien dibandingkan dengan metode rekursif, terutama untuk jumlah data yang lebih besar. Waktu eksekusi iteratif lebih cepat karena tidak melibatkan overhead pemanggilan fungsi berulang yang terjadi pada metode rekursif.

## Fitur Utama
- Implementasi algoritma **Sequential Search** menggunakan **iteratif** dan **rekursif**.
- Pengguna diminta untuk memasukkan jumlah pasien (n) dan kelas BPJS yang ingin dicari (kelas 1, 2, atau 3).
- Kemudian, program akan menampilkan data perbandingannya ke dalam tabel.
- Setelah, ditambilkan tabelnya program akan membentuknya ke dalam grafik perbanfingan iteratif vs rekursif.

```python
# Fungsi Bubble Sort Iteratif
def bubble_sort_iterative(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

#  Fungsi Bubble Sort Rekursif
def bubble_sort_recursive(arr, n=None):
    if n is None:
        n = len(arr)
    if n == 1:
        return
    for i in range(n - 1):
        if arr[i] > arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
    bubble_sort_recursive(arr, n - 1)
```

## Output Terminal

```plaintext
Daftar Gaji yang Tersedia:
1. Gaji: Rp 1500000
2. Gaji: Rp 2000000
3. Gaji: Rp 2500000
4. Gaji: Rp 3000000
5. Gaji: Rp 3500000
6. Gaji: Rp 4000000
7. Gaji: Rp 4500000
8. Gaji: Rp 5000000
9. Gaji: Rp 5500000
10. Gaji: Rp 6000000
11. Gaji: Rp 6500000
12. Gaji: Rp 7000000
13. Gaji: Rp 7500000
14. Gaji: Rp 8000000
15. Gaji: Rp 8500000
16. Gaji: Rp 9000000
17. Gaji: Rp 9500000
18. Gaji: Rp 10000000
19. Gaji: Rp 10500000
20. Gaji: Rp 11000000
21. Gaji: Rp 11500000
22. Gaji: Rp 12000000
23. Gaji: Rp 12500000
24. Gaji: Rp 13000000
25. Gaji: Rp 13500000

Masukkan jumlah data yang ingin dihitung dan diurutkan pencarian (1-25):
Masukkan jumlah data (1-25): 1

Masukkan beberapa nilai n yang ingin dihitung (1 sampai 25):
Masukkan n ke-1 (1-25): 5

Gaji yang akan dihitung zakatnya (Jumlah data: 1):
Nomor 5. Gaji: Rp 3500000

Memproses data...

+-----+---------------------------+---------------------------+
|  n  |   Recursive Time (s)      |   Iterative Time (s)      |
+-----+---------------------------+---------------------------+
| 5    | 0.0000171661             | 0.0000052452              |
+-----+---------------------------+---------------------------+

```
## Output Grafik
![Output Grafik1](https://github.com/arsyafarahman123/Tugas-Besar-Program-Zakat-Penghasilan_IF-11-01_Analisis-Kompleksitas-Algoritma/blob/main/grafik1.png)

```plaintext
Masukkan jumlah data yang ingin dihitung dan diurutkan pencarian (1-25):
Masukkan jumlah data (1-25): 2

Masukkan beberapa nilai n yang ingin dihitung (1 sampai 25):
Masukkan n ke-1 (1-25): 5
Masukkan n ke-2 (1-25): 10

Gaji yang akan dihitung zakatnya (Jumlah data: 2):
Nomor 5. Gaji: Rp 3500000
Nomor 10. Gaji: Rp 6000000

Memproses data...

+-----+---------------------------+---------------------------+
|  n  |   Recursive Time (s)      |   Iterative Time (s)      |
+-----+---------------------------+---------------------------+
| 5    | 0.0000112057             | 0.0000030994              |
| 10   | 0.0000071526             | 0.0000016689              |
+-----+---------------------------+---------------------------+

```
## Output Grafik
![Output Grafik2](https://github.com/arsyafarahman123/Tugas-Besar-Program-Zakat-Penghasilan_IF-11-01_Analisis-Kompleksitas-Algoritma/blob/main/grafik2.png)

```plaintext

Masukkan jumlah data yang ingin dihitung dan diurutkan pencarian (1-25):
Masukkan jumlah data (1-25): 3

Masukkan beberapa nilai n yang ingin dihitung (1 sampai 25):
Masukkan n ke-1 (1-25): 5
Masukkan n ke-2 (1-25): 10
Masukkan n ke-3 (1-25): 15

Gaji yang akan dihitung zakatnya (Jumlah data: 3):
Nomor 5. Gaji: Rp 3500000
Nomor 10. Gaji: Rp 6000000
Nomor 15. Gaji: Rp 8500000

Memproses data...

+-----+---------------------------+---------------------------+
|  n  |   Recursive Time (s)      |   Iterative Time (s)      |
+-----+---------------------------+---------------------------+
| 5    | 0.0000076294             | 0.0000019073              |
| 10   | 0.0000021458             | 0.0000014305              |
| 15   | 0.0000016689             | 0.0000009537              |
+-----+---------------------------+---------------------------+
```
## Output Grafik
![Output Grafik3](https://github.com/arsyafarahman123/Tugas-Besar-Program-Zakat-Penghasilan_IF-11-01_Analisis-Kompleksitas-Algoritma/blob/main/grafik3.png)

```plaintext
Masukkan jumlah data yang ingin dihitung dan diurutkan pencarian (1-25):
Masukkan jumlah data (1-25): 4

Masukkan beberapa nilai n yang ingin dihitung (1 sampai 25):
Masukkan n ke-1 (1-25): 5
Masukkan n ke-2 (1-25): 10
Masukkan n ke-3 (1-25): 15
Masukkan n ke-4 (1-25): 20

Gaji yang akan dihitung zakatnya (Jumlah data: 4):
Nomor 5. Gaji: Rp 3500000
Nomor 10. Gaji: Rp 6000000
Nomor 15. Gaji: Rp 8500000
Nomor 20. Gaji: Rp 11000000

Memproses data...

+-----+---------------------------+---------------------------+
|  n  |   Recursive Time (s)      |   Iterative Time (s)      |
+-----+---------------------------+---------------------------+
| 5    | 0.0000209808             | 0.0000061989              |
| 10   | 0.0000069141             | 0.0000042915              |
| 15   | 0.0000071526             | 0.0000045300              |
| 20   | 0.0000088215             | 0.0000052452              |
+-----+---------------------------+---------------------------+
```
## Output Grafik
![output Grafik4](https://github.com/arsyafarahman123/Tugas-Besar-Program-Zakat-Penghasilan_IF-11-01_Analisis-Kompleksitas-Algoritma/blob/main/grafik4.png)



```plaintext
Program selesai dan terimakasih!
```



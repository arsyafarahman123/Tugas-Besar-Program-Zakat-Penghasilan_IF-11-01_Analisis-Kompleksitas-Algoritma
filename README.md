Kelas: IF-11-01
Nama Anggota Kelompok:

1. Arsya Fathiha Rahman (2311102152)
2. Grashela Ayudia Prameswari (2311102318)

 Penjelasan Program:

- Studi Kasus
Dalam kasus ini, Bubble Sort digunakan untuk mengurutkan data gaji sebelum menghitung zakat. Algoritma ini membandingkan elemen berdekatan dan menukarnya jika diperlukan. Proses ini berlanjut hingga seluruh data terurut. Setelah pengurutan, zakat dihitung menggunakan dua metode: rekursif dan iteratif. Pada metode rekursif, fungsi memanggil dirinya sendiri untuk menghitung zakat, sedangkan metode iteratif menggunakan perulangan untuk menghitung zakat. Kedua metode ini dibandingkan untuk melihat mana yang lebih efisien setelah data diurutkan dengan Bubble Sort.

- Result:
Perbandingan Waktu Eksekusi:
Metode rekursif dan iteratif digunakan setelah data diurutkan dengan Bubble Sort. Rekursif lebih lambat karena pemanggilan fungsi berulang, sementara iteratif lebih efisien dan lebih cepat.
Analisis Kinerja:
        1. Bubble Sort: Mengurutkan data gaji, meski sederhana, mempengaruhi waktu eksekusi.
        2. Rekursif: Lebih lambat karena overhead pemanggilan fungsi.
        3. Iteratif: Lebih efisien dan cepat tanpa overhead pemanggilan fungsi.


- Perbandingan Performa
Dari hasil perbandingan waktu eksekusi, dapat dilihat bahwa metode iteratif cenderung lebih efisien dibandingkan dengan metode rekursif, terutama untuk jumlah data yang lebih besar. Waktu eksekusi iteratif lebih cepat karena tidak melibatkan overhead pemanggilan fungsi berulang yang terjadi pada metode rekursif.

- Grafik Perbandingan
Iterative vs Recursive Graph
Grafik berikut ini menunjukkan perbandingan antara waktu eksekusi rekursif dan iteratif. Sumbu X menunjukkan jumlah orang yang dihitung, sedangkan sumbu Y menunjukkan waktu eksekusi (dalam detik). Waktu eksekusi untuk kedua metode dipetakan dan dibandingkan.
Metode iteratif lebih efisien pada data besar karena menggunakan loop langsung tanpa pemanggilan fungsi berulang, sehingga waktu eksekusinya lebih cepat dan meningkat linier sesuai jumlah data. 
Metode rekursif kurang efisien karena banyaknya pemanggilan fungsi yang menambah overhead, menyebabkan waktu eksekusi meningkat drastis dan berisiko stack overflow pada data besar.

- Conclusion
Pada grafik ini, terlihat bahwa garis waktu eksekusi untuk metode iteratif lebih mendatar dan lebih rendah dibandingkan dengan metode rekursif, yang menunjukkan bahwa metode iteratif lebih efisien dalam hal waktu eksekusi.

- Kesimpulan
Berdasarkan hasil yang diperoleh, dapat disimpulkan bahwa:
1. Metode Iteratif lebih efisien dan cocok digunakan untuk aplikasi yang membutuhkan waktu eksekusi cepat, seperti perhitungan zakat penghasilan.
2. Metode Rekursif memiliki kelebihan dalam hal konsep yang lebih sederhana dan mudah dipahami, namun tidak cocok untuk aplikasi yang memerlukan performa tinggi, terutama dengan data besar.


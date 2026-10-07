# Studi_Kasus6_MuhammadFikri_095

**NAMA : MUHAMMAD FIKRI**

**NIM : 2609116095**

**KELAS C**

## Sistem Pencatatan Nilai Mahasiswa


Program ini berbasis Python. Program dapat membaca riwayat nilai dari file, menampilkannya, dan menambahkan nilai baru secara permanen. Data disimpan dalam file *JSON* sehingga tetap ada walaupun program ditutup.


---

## berikut penjelasan program

### 1. Import dan path
 
<img width="675" height="131" alt="Cuplikan layar 2026-10-07 072358" src="https://github.com/user-attachments/assets/fa2b1f8e-de06-43e7-9787-47a0e8289d86" />

Import JSON digunakan untuk memanggil modul python untuk membaca dan menulis file JSON, path digunakan untuk menyimpan file menyimpan data, agar file dapat diakses.
 
### 2. `baca_data()`: membaca file
 
<img width="556" height="190" alt="Cuplikan layar 2026-10-07 075102" src="https://github.com/user-attachments/assets/040e2314-7767-47aa-a29a-5e53fc9c3769" />

- def digunakan untuk membuat fungsi yang bisa dipanggil berulang kali.
- open (path, "r") membuka file dalam mode baca, dan with menutup file otomatis setelah selesai dipakai.
- json.load(f) digunakan untuk mengubah isi file JSON menjadi list berisi dictionary di Python.
- try-except FileNotFoundError mencegah error jika file belum ada. Fungsi akan mengembalikan list kosong.

---

### 3. Fungsi tampilkan_data()

<img width="634" height="296" alt="Cuplikan layar 2026-10-07 075223" src="https://github.com/user-attachments/assets/f5c8739c-2609-487b-81d1-cee28d7584f9" />

- baca_data() digunakan untuk mengambil seluruh data dari file.
- len(data) == 0 mengecek apakah data masih kosong, lalu menampilkan pesan jika benar.
- for mahasiswa in data mengulang setiap data mahasiswa di dalam list.
- mahasiswa['nama'], mahasiswa['nim'], dan seterusnya mengambil nilai berdasarkan key pada dictionary.
- Garis ----- dipakai sebagai pemisah antar data agar tampilan mudah dibaca

---

### 4. `tambah_data()`: menyimpan data

<img width="512" height="311" alt="Cuplikan layar 2026-10-07 075524" src="https://github.com/user-attachments/assets/4a46ba76-5e54-4ce6-8d65-03551c2dd132" />

- baca_data() dipanggil lebih dulu agar data lama tidak tertimpa.
- data_baru ialah dictionary yang berisi nama, NIM, mata kuliah, dan nilai dari input user.
- data.append(data_baru) digunakan untuk menambahkan data baru ke akhir list.
- open(path, "w") untuk membuka file dalam mode tulis.
- json.dump(data, file, indent=4) untul menulis seluruh list ke file JSON. Parameter indent=4 membuat isi file rapi dan mudah dibaca.

---

### 5. Perulangan Menu Utama
 
<img width="565" height="380" alt="Cuplikan layar 2026-10-07 080047" src="https://github.com/user-attachments/assets/c7dd34a7-6006-431a-b443-c3a4bbe84e1f" />

- while True membuat program berjalan terus-menerus sampai user memilih keluar.
- input() untuk menerima pilihan menu dari user dan disimpan di variabel pilihan.
- if-elif-else memanggil fungsi sesuai pilihan: menu 1 memanggil tampilkan_data(), menu 2 memanggil tambah_data().
- Menu 3 menjalankan break untuk menghentikan perulangan, sehingga program selesai.
- else menangani input di luar pilihan menu dan menampilkan pesan kesalahan.

---

berikut adalah hasil dari program 

<img width="684" height="487" alt="Cuplikan layar 2026-10-07 080918" src="https://github.com/user-attachments/assets/44fd00de-ba20-4c7a-bc14-518d5a4bf9f0" />

gambar diatas merupakan menu 1 yaitu menampilkan semua data nilai  yg tersimpan di JSON

---

<img width="499" height="643" alt="Cuplikan layar 2026-10-07 081015" src="https://github.com/user-attachments/assets/ba0b5f45-141c-4bfe-96e3-e4489549fc91" />


gambar tersebut ialah menu 2 yaitu menambah data nilai seperti nama, nim, kelas, nilai yg dihasilkan. yg akan otomatis tersimpan di file JSON. dan jika ingin melihat apakah data yg di tambahkan tadi tersimpan, dengan memilih menu 1 yaitu tampilkan nilai. dan di menu 3 digunakan untuk keluar menu

---

<img width="574" height="405" alt="Cuplikan layar 2026-10-07 081038" src="https://github.com/user-attachments/assets/a4374ad7-71ba-467e-b043-6a989962b6ab" />

berikut isi dari file JSON yg akan terisi otomatis saat menambahkan data nilai baru.

---

sekian terimakasihh


import  json

path = r"C:\Users\longorr\Documents\Sistem Informasi\Fikri_file.json"

def baca_data():
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []
 
def tampilkan_data():
    data = baca_data()
    print("\n==== DATA NILAI MAHASISWA ====")
    if len(data) == 0:
        print("Belum ada data nilai.")
    else:
        for mahasiswa in data:
            print(f"Nama        : {mahasiswa['nama']}")
            print(f"NIM         : {mahasiswa['nim']}")
            print(f"Mata Kuliah : {mahasiswa['mata_kuliah']}")
            print(f"Nilai       : {mahasiswa['nilai']}")
            print("-----------------------------")

def tambah_data():
    data = baca_data()
    data_baru = {
        "nama": input("Nama        : "),
        "nim": input("NIM         : "),
        "mata_kuliah": input("Mata Kuliah : "),
        "nilai": input("Nilai       : ")
    }
    data.append(data_baru)
 
    with open(path, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)
    print("Data nilai berhasil disimpan!")

while True:
    print("\n==== SISTEM PENCATATAN NILAI MAHASISWA ====")
    print("1. Tampilkan nilai\n2. Tambah nilai\n3. Keluar")
    pilihan = input("Pilih menu: ")
 
    if pilihan == "1":
        tampilkan_data()
    elif pilihan == "2":
        tambah_data()
    elif pilihan == "3":
        print("Program selesai.")
        break
    else:
        print("Pilihan tidak valid!")
 
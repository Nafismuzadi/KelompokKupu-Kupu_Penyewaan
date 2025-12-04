data = {}
rental_history = []

def tambah():
    nama = input("Masukkan barang yang mau disewakan : ")
    try:
        harga = float(input("Masukkan harga barang sewaan perjam : "))
        stok = int(input("Masukkan stok barang sewaan : "))
    except:
        print("Input harga/stok tidak valid. Data batal ditambahkan.\n")
        return

    data[nama] = {
        "Nama barang": nama,
        "Harga sewa perjam": harga,
        "Stok barang": stok
    }
    print("\nData berhasil ditambahkan\n")

def lihat():
    if len(data) == 0:
        print("\nBelum ada data\n")
    else:
        print("\nList barang sewaan saat ini\n")
        for nama, info in data.items():
            print(f"nama barang : {info['Nama barang']}")
            print(f"harga barang : {info['Harga sewa perjam']}")
            print(f"Stok barang: {info['Stok barang']}\n")

def update():
    if len(data) == 0:
        print("belum ada data")
        return

    lihat()
    while True:
        nama = input("Masukkan nama barang yang ingin di ubah : ")
        if nama in data:
            print("\nData ditemukan\n")
            break
        else:
            print("\nData tidak ditemukan\n")

    
    while True:
        try:
            harga_baru = float(input("Masukkan harga baru : "))
            if harga_baru < 0:
                print("Harga sewa tidak boleh NEGATIF")
            else:
                data[nama]["Harga sewa perjam"] = harga_baru
                print("Harga berhasil diperbarui\n")
                break
        except:
            print("Input tidak valid!!, silahkan masukkan lagi")

    
    while True:
        try:
            stok_baru = int(input("Masukkan stok baru : "))
            if stok_baru < 0:
                print("\nStok baru tidak boleh minus")
            else:
                data[nama]["Stok barang"] = stok_baru
                print("Stok berhasil diperbarui\n")
                break
        except:
            print("Input tidak valid!!, silahkan masukkan lagi")

def hapus():
    if len(data) == 0:
        print("belum ada data")
        return

    lihat()
    while True:
        nama_barang = input("masukkan nama barang: ")
        if nama_barang in data:
            print("\nData ditemukan\n")
            break
        else:
            print("barang tidak ditemukan, silahkan masukkan lagi")

    while True:
        dihapus = input(f"apakah anda yakin ingin menghapus {nama_barang}?  (y/n) ").lower()
        if dihapus in ["y", "n"]:
            break
        print("Input tidak valid!!, silahkan masukkan lagi")

    if dihapus == "y":
        del data[nama_barang]
        print(f"barang {nama_barang} berhasil dihapus\n")
    else:
        print("penghapusan dibatalkan\n")

def sewa():
    if len(data) == 0:
        print("Belum ada barang yang bisa di sewa")
        return

    lihat()
    while True:
        barang_sewa = input("Inputkan barang yang ingin di sewa : ")
        if barang_sewa in data:
            stok_tersedia = data[barang_sewa]["Stok barang"]
            if stok_tersedia == 0:
                print("Stok barang habis! Silahkan pilih barang lain.")
                return
            print("\nBarang ditemukan\n")
            print(f"\nStok barang : {stok_tersedia}")
            break
        else:
            print("Barang tidak tersedia, masukkan lagi.")

    nama_penyewa = input("Masukkan nama penyewa : ")

    while True:
        try:
            sewapiro = int(input("Anda ingin menyewa berapa banyak? : "))
            stok_tersedia = data[barang_sewa]["Stok barang"]
            if sewapiro <= 0:
                print("Jumlah sewa harus lebih dari 0!")
            elif sewapiro > stok_tersedia:
                print(f"Stok tidak mencukupi. Stok tersedia : {stok_tersedia}")
            else:
                break
        except:
            print("Input tidak valid!!, silahkan masukkan lagi")

    while True:
        try:
            print("Jika sewa lebih dari 3 jam maka akan mendapat diskon 10%, jika sewa lebih dari 5 jam maka akan mendapat diskon 20%")
            durasi = int(input("Berapa jam anda ingin sewa barang tersebut? : "))
            if durasi <= 0:
                print("Durasi sewa harus lebih dari 0 jam")
            else:
                break
        except:
            print("Input tidak valid!!, silahkan masukkan lagi")

    harga = data[barang_sewa]["Harga sewa perjam"]
    total_sementara = harga * durasi * sewapiro

    diskon = 0
    if durasi >= 5:
        diskon = total_sementara * 0.20
    elif durasi >= 3:
        diskon = total_sementara * 0.10

    total_bayar = total_sementara - diskon

    data[barang_sewa]["Stok barang"] -= sewapiro

    transaksi = {
        "nama_penyewa": nama_penyewa,
        "barang": barang_sewa,
        "jumlah": sewapiro,
        "durasi_jam": durasi,
        "harga_perjam": harga,
        "total_before_discount": total_sementara,
        "diskon": diskon,
        "total_bayar": total_bayar
    }
    rental_history.append(transaksi)

    print("\n===== STRUK SEWA =====")
    print(f"Nama penyewa        : {nama_penyewa}") 
    print(f"Nama barang         : {barang_sewa}")
    print(f"Jumlah              : {sewapiro}")
    print(f"Durasi sewa         : {durasi} jam")
    print(f"Harga per jam       : {harga}")
    print(f"Total sebelum diskon: {total_sementara}")
    print(f"Diskon              : {diskon}")
    print(f"Total bayar         : {total_bayar}")
    print("=======================\n")
    print("Barang berhasil disewa!\n")


def sedang_di_sewa():
    if len(rental_history) == 0:
        print("Belum ada barang yang di sewa\n")
        return

    print("\nList barang yang sedang di sewa")
    print("================================")

    for catatan_sewa in rental_history:
        print(f"Penyewa : {catatan_sewa['nama_penyewa']}")
        print(f"Barang  : {catatan_sewa['barang']}")
        print(f"Jumlah  : {catatan_sewa['jumlah']}")
        print("--------------------------------")
    
    print()



def pengembalian():
    if not rental_history:
        print("Belum ada transaksi sewa.\n")
        return

    sedang_di_sewa()

    nama_penyewa = input("Nama penyewa: ")
    if not any(t["nama_penyewa"] == nama_penyewa for t in rental_history):
        print(f"Nama penyewa '{nama_penyewa}' tidak ditemukan.\n")
        return


    while True:
        nama_barang = input("Nama barang yang dikembalikan: ")

        transaksi = None
        for t in rental_history:
            if t["nama_penyewa"] == nama_penyewa and t["barang"] == nama_barang:
                transaksi = t
                break

        if transaksi:
            data[nama_barang]["Stok barang"] += transaksi["jumlah"]
            rental_history.remove(transaksi)
            print(f"{nama_barang} berhasil dikembalikan oleh {nama_penyewa}\n")
            break
        else:
            print(f"Barang '{nama_barang}' tidak ditemukan untuk penyewa '{nama_penyewa}'. Silakan masukkan lagi.\n")

    while True:
        try:
            lama_pengembalian = int(input("Masukkan total lama penyewaannya (jam): "))
            if lama_pengembalian <= 0:
                print("Input tidak boleh minus atau 0! Silakan masukkan lagi.")
            else:
                break
        except:
            print("Input tidak valid! Masukkan angka.")


    durasi_awal = transaksi["durasi_jam"]        
    harga_perjam = transaksi["harga_perjam"]      
    telat = lama_pengembalian - durasi_awal

    denda = 0
    if telat > 0:
        denda = telat * (harga_perjam * 0.5)   
        print(f"Anda telat {telat} jam.")
        print(f"Denda keterlambatan : Rp {denda:,.0f}")
    else:
        print("Pengembalian tepat waktu, tidak ada denda.\n")


    print("\n===== STRUK PENGEMBALIAN =====")
    print(f"Nama Penyewa   : {nama_penyewa}")
    print(f"Barang         : {nama_barang}")
    print(f"Lama sewa      : {durasi_awal} jam")
    print(f"Lama kembali   : {lama_pengembalian} jam")
    print(f"Telat          : {telat if telat > 0 else 0} jam")
    print(f"Denda          : Rp {denda:,.0f}")
    print("===============================\n")



pw = "admin123"

while True:
    print("Selamat datang di rental serba ada")
    print("Menu \n1.Pemilik\n2.Penyewa\n3.Keluar")
    pilih = input("Pilih Menu (1-3) : ")
    print()

    if pilih == "1":
        while True :
            try:
                sandi = input("Masukkan password anda : " )
                if sandi == pw :
                    while True:
                        print("\n1.Tambah barang\n2.Lihat barang\n3.Edit barang\n4.Hapus barang\n5.Barang yang sedang di sewa\n6.Kembali")
                        pilih_owner = input("Pilih menu (1-6) : ")
                        print()

                        if pilih_owner == "1":
                            tambah()
                        elif pilih_owner == "2":
                            lihat()
                        elif pilih_owner == "3":
                            update()
                        elif pilih_owner == "4":
                            hapus()
                        elif pilih_owner == "5":
                            sedang_di_sewa()
                        elif pilih_owner == "6":
                            print("GoodByeeee")
                            print()
                            break
                        else:
                            print("Input tidak valid!!, silahkan masukkan lagi")
                            print()
                    break
                else :
                    print("Password salah")
            except :
                print("Password anda salah")
            
            
    elif pilih == "2":
        while True:
            print("1.Lihat barang tersedia\n2.Sewa barang\n3.Pengembalian barang\n4.Kembali")
            pilih_penyewa = input("Pilih menu (1-4) : ")
            print()

            if pilih_penyewa == "1":
                lihat()
            elif pilih_penyewa == "2":
                sewa()
            elif pilih_penyewa == "3":
                pengembalian()
            elif pilih_penyewa == "4":
                print()
                break
            else:
                print("Input tidak valid!!, silahkan masukkan lagi")
    elif pilih == "3":
        print("GoodByeee")
        print()
        break
    else:
        print("Input tidak valid!!!, silahkan masukkan lagi")
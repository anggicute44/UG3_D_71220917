huhhhah = (input("Masukkan Plat Nomor: ")).split(" ")
try :
    makanikan_3 = int(huhhhah[1])
    if makanikan_3 < 3001:
        print ("Plat nomor tersebut diperuntukan untuk mobil")
    elif makanikan_3 < 4001:
        print ("Plat nomorr tersebut diperuntukan motor")
    elif makanikan_3 < 5001:
        print ("Plat nomor tersebut diperuntukan untuk angkutan umum")
    else:
        print ("Plat nomor tidak terindikasi ketiga angkutan tersebut")


except:
    print ("Plat Nomor Tidak Terindikasi, setelah kode daerah harus berupa nomor kendaraan")
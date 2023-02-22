jomblah = float(input("Masukkan nilai curah hujan : "))
mamat_1 = (print ("Cuaca terang berawan") if jomblah == 0 else (print ("Curah hujan ringan") if jomblah <= 20 else (print("Cuaca hujan sedang") if jomblah <=50 else (print("Curah hujan lebat") if jomblah <= 100 else (print("Curah hujan ekstrem") if jomblah > 100 else () )))))

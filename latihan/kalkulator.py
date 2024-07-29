while True:
    choise = int(input("kalkulator sederhana\n1. tambah\n2. kurang\n3. kali\n4. bagi\npilihan: ".title()))
    if choise >= 1 and choise <=4:
        nilai1 = int(input("Nilai pertama: "))
        nilai2 = int(input("Nilai kedua: "))
        if choise == 1:
            hasil = nilai1 + nilai2
            print(f"{nilai1} + {nilai2} = {hasil}")
        elif choise == 2:
            hasil = nilai1 - nilai2
            print(f"{nilai1} - {nilai2} = {hasil}")
        elif choise == 3:
            hasil = nilai1 * nilai2
            print(f"{nilai1} x {nilai2} = {hasil}")
        elif choise == 4:
            hasil = nilai1 / nilai2
            print(f"{nilai1} ÷ {nilai2} = {hasil}")
        else:
            print("error: unknown")
    else:
        print("error: unknown")
        break
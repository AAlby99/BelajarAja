def main():
    while True:
        try:
            pilihan = int(input('Pilih salah satu:\n1. IDR ke USD.\n2. USD ke IDR.\nKlik 0 Untuk Mengakhiri Sistem\nPilih: '))
            if pilihan == 1:
                print('Selamat datang di Konversi mata uang indonesia ke dolar amerika'.title())
                uang = int(input("Masukan nominal: "))
                hasil = uang / 16000
                print(f"Nominal IDR: {uang:,.2f} jika di konversi ke USD adalah: {hasil:,.2f}".title())
            elif pilihan == 2:
                print('Selamat datang di Konversi mata uang amerika ke rupiah indoesia'.title())
                uang = int(input("Masukan nominal: "))
                hasil = uang * 16000
                print(f"Nominal USD: {uang:,.2f} jika di konversi ke IDR adalah: {hasil:,.2f}".title())
            elif pilihan == 0:
                break
                
        except:
            print("masukan data yang valid")
            
if __name__ == "__main__":
    main()
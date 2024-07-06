import main
def start():
    while True:
        print("Pilih operasi:")
        print("1. Tambah")
        print("2. Kurang")
        print("3. Kali")
        print("4. Bagi")
        print("5. Menu Utama")
        
        pilihan = input("Masukkan pilihan (1/2/3/4/5): ")
        
        if pilihan == '5':
            print("Terima kasih telah menggunakan kalkulator!")
            main.menu()
            break
            

        if pilihan in ['1', '2', '3', '4']:
            num1 = float(input("Masukkan angka pertama: "))
            num2 = float(input("Masukkan angka kedua: "))
            
            if pilihan == '1':
                hasil = num1 + num2
                operasi = '+'
            elif pilihan == '2':
                hasil = num1 - num2
                operasi = '-'
            elif pilihan == '3':
                hasil = num1 * num2
                operasi = '*'
            elif pilihan == '4':
                if num2 == 0:
                    hasil = "Error: Tidak bisa dibagi dengan nol!"
                    operasi = '/'
                else:
                    hasil = num1 / num2
                    operasi = '/'
            
            print(f"Hasil: {num1} {operasi} {num2} = {hasil}")
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    start()
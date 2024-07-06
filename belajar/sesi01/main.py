from libr import welcome, keluar
from opsi import kaptencurut, kalkulator, warung

def menu():
    pilihan_user = int(input(f'pilih menu: \n1. game mencari kapten curut\n2. kalkulator\n3. warung\n4. keluar \n\nsilahkan pilih: '))
    # return pilihan_user # biar bisa di pake di retrun fungsinya untu mengembalikan pilihan ke user (misal digunakan saat dipisah dari fungsion nya jika dalam satu fungsion tidak usah di kasih retrun)
    
    if pilihan_user == 1:
        kaptencurut.start()
    elif pilihan_user == 2:
        kalkulator.start()
    elif pilihan_user == 3:
        warung.start()
    elif pilihan_user == 4:
        keluar()
    else:
        print("maaf pilihan tidak tersedia \n -----------")


def main():
    welcome()
    menu()
if __name__ == "__main__":  #intinya ini untuk validasi saya pun belom begitu paham
    main()
# program menghitung luas dan kelilng segitiga dan persegi
import os
import math


# header program
def header():
    os.system('cls')

    print(f'{"Welcome to Sistim menghitung luas dan kelilng segitiga dan persegi":^80}\n')
    print('sebelum itu pilih dulu ya')

# brain program

def luas_segitiga(alas = 1, tinggi=1):
    proses = 1/2 * alas * tinggi
    return proses

def keliling_segitiga(a, b, c):
    proses = a + b + c
    return proses

def luas_persegi(sisi):
    proses = sisi ** 2
    return proses

def keliling_persegi(sisi):
    proses = sisi * 4
    return proses

def luas_lingkaran():
    jari_jari = int(input('masukan jari jari: ')) 
    luas = math.pi * (jari_jari ** 2)
    return luas



# body program
def body():
    while True:
        try:
            choices = int(input('\nMenu \n1. segitiga \n2. persegi\n3. lingkaran\n0 Untuk berhenti\nPilih: '))
            
            if choices == 1:
                pilihan_segitiga = int(input('\nMenu \n1. luas \n2 keliling\nPilih: '))
                if pilihan_segitiga == 1:
                    alas_input = input('\nmasukan alasnya: ')
                    tinggi_input = input('masukan tingginya: ')
                    
                    # pengecekan
                    alas = float(alas_input) if alas_input else 1
                    tinggi = float(tinggi_input) if tinggi_input else 1
                    
                    print(f'Hasilnya adlah {luas_segitiga(alas=alas,tinggi=tinggi)}')
                elif pilihan_segitiga == 2:
                    a_input = input('masukan sisi a: ')
                    b_input = input('masukan sisi b: ')
                    c_input = input('masukan sisi c: ')
                    
                    # pengecekan
                    a = int(a_input) if a_input else 0
                    b = int(b_input) if b_input else 0
                    c = int(c_input) if c_input else 0
                    
                    print(f'Hasilnya adalah {keliling_segitiga(a=a, b=b, c=c)}')
                else:
                    print('masukan tidak valid')
            elif choices == 2:
                pilihan_persegi = int(input('\nMenu \n1. luas \n2. keliling\nPilih: '))
                
                if pilihan_persegi == 1:
                    sisi_input = input('Masukan sisinya: ')
                    
                    # pengecekan
                    lsisi = int(sisi_input) if sisi_input else 0
                    
                    print(f'Hasinya adalah {luas_persegi(lsisi)}')
                
                elif pilihan_persegi == 2:
                    s1 = input('masukan sisinya: ')
                    
                    ksisi = int(s1) if s1 else 0
                    
                    print(f'Hasilnya adalah {keliling_persegi(ksisi)}')
                else:
                    print('masukan tidak valid')
            elif choices == 3:
                print('Luas lingkaran adalah', luas_lingkaran())
            elif choices == 0:
                break
            else:
                print('masukan tidak valid')
        except Exception as err:
            print(f'Kesalahan pengetikan: {err}')
            

def main():
    header()
    body()
    
if __name__ == "__main__":
    main()


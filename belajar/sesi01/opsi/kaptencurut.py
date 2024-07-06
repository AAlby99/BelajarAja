import random    #libary ada 2 hal baru
import main

def start():
    while True:
        posisi_kapten_curt = random.randint(1, 4) # ini di ambil dari libary python untuk selengkapnya bisa cari di google
        bentuk_goa = "|_|"
        jumlah_goa = [bentuk_goa] * 4
        goa_kosong = " ".join(jumlah_goa)
        isi_goa = jumlah_goa.copy()
        isi_goa[posisi_kapten_curt - 1] = "|🐭|"
        isi_goa = " ".join(isi_goa)

        print(f'''
                AYO CEPAT SELAMATKAN KAPTEN CURUT
            MENURUT KAMU KAPTEN CURUT ADA DI GOA MANA??
                        [1 / 2 / 3 / 4]
                            
                        {goa_kosong}
                ''')
        pilihan = int(input(f'Cari di goa [1 / 2 / 3 / 4]: '))
        if pilihan > 0 and pilihan < 5 :
                print(f'KAMU MULAI CARI DI GOA: {pilihan}')
                if int(pilihan) == posisi_kapten_curt:   #int() bisa juga di tulis di dalam inputnya contoh pilihan = int(input('Cari di goa [1/2/3/4]:'))
                    print(f'''Selamat kamu berhasil menyelamatkan kapten curut di goa {pilihan} dari malabahaya
                                                {isi_goa}
                        ''')
                else:
                    print(f'''NOOOOOOO KAPTEN CURUUTTTT T-T kamu gagal menyelamatkan kapten curut kamu harus tanggung jawab
                ---------------------------------------------------------------------------------------------------------------         
                            KAMU SEHARUSNYA MENCARI DI GOA {posisi_kapten_curt} KARNA KAPTEN CURUT ADA DI SITU
                                                {isi_goa}
                            ''')
        else:
            print(f"TIDAK ADA GOA {pilihan}")
            exit()
        main_lagi = input("\nMau main lagi? [y/n]: ")
        if main_lagi == "n":
            main.menu()
            break


if __name__ == "__main__":
    start()




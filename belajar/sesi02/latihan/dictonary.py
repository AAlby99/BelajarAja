import datetime as dt
import os # ini library python buat ngejalanin printah ke terminal saat ini saya mengunakan clear
import random
import string

buah_tempate = {
    'Nama':'buah',
    'Jumlah': 0,
    'Warna': 'kuning',
    'Manis': True,
    'Kadaluarsa': dt.date(2024,8,17)
}

keranjang_buah = {}
while True:
    try:
        os.system('cls')
        print(f'\n{"welcome to fruit store":^80}'.title())
        print(90*'-')

        buah = dict.fromkeys(buah_tempate.keys()) # membuat deictionary baru mengunakan key dari buah_tempalte 
        buah['Nama']= input('Masukkan nama buah: ')
        buah['Jumlah'] = input('Masukkan banyak buah: ')
        buah['Warna'] = input('Masukkan warna buah: ')
        rasa = input('Apakah manis (y/n): ')
        if rasa == 'y':
            buah['Manis'] = True
        else:
            buah['Manis'] = False
        print('Masukan Tanggal kadaluarsanya: ')
        tanggal = int(input('tanggal: '))
        bulan = int(input('bulan: '))
        taun = int(input('tahun: '))
        kdl = dt.date(taun, bulan, tanggal)
        buah['Kadaluarsa'] = kdl

        KEY = ''.join((random.choice(string.ascii_uppercase) for i in range(4)))
        # artinya saya membuat key dengan mengunakakn random number dan memilih string dengan kode asci upper case di dalam range 6
        keranjang_buah.update({KEY: buah})
        print(f'|{'ID':<5} | {'Nama':<15}| {'Jumlah':<4}| {'Warna':<4}| {'Manis':<6}| {'Kadaluarss':<9}|')
        print(60*'-')

        for buah in keranjang_buah.keys():
            KEY = buah
            NAMA = keranjang_buah[KEY]['Nama']
            NIS = keranjang_buah[KEY]['Jumlah']
            NILAI = keranjang_buah[KEY]['Warna']
            BEASISWA = 'Yes' if keranjang_buah[KEY]['Manis'] else 'No'
            LAHIR = keranjang_buah[KEY]['Kadaluarsa'].strftime("%x")
            print(f'|{KEY:<5} | {NAMA:<15}| {NIS:<5} | {NILAI:^5}| {BEASISWA:<6}| {LAHIR:<10}|')
        klik = int(input('sini: '))
        if klik == 1:
            break
        else:
            True
    except Exception as err:
        print(f'Ups keknya kamu salah ketik: {err}')
        break
# nesting dictonary 
import datetime

siswa = {
    'nama' : 'alby',
    'nis' : '3478',
    'nilai' : 800,
    'beasiswa' : True,
    'lahir' : datetime.datetime(2006, 2, 10)
}
siswa2 = {
    'nama' : 'avil',
    'nis' : '3479',
    'nilai' : 860,
    'beasiswa' : False,
    'lahir' : datetime.datetime(2008, 4, 10)
}
siswa3 = {
    'nama' : 'tiago',
    'nis' : '3477',
    'nilai' : 400,
    'beasiswa' : False,
    'lahir' : datetime.datetime(2002, 9, 19)
}
# nesting 
data_siswa = {
    'id001' : siswa,
    'id002' : siswa2,
    'id003' : siswa3
}
print(f'{'ID':<5} {'Nama':<15} {'NIS':<4} {'Nilai':<4} {'Beasiswa':<6} {'lahir':<9}')
print(50*'-')
for sis in data_siswa.keys():
    KEY = sis
    NAMA = data_siswa[KEY]['nama']
    NIS = data_siswa[KEY]['nis']
    NILAI = data_siswa[KEY]['nilai']
    BEASISWA = 'Yes' if data_siswa[KEY]['beasiswa'] else 'No'
    LAHIR = data_siswa[KEY]['lahir'].strftime("%x")
    
    print(f'|{KEY:<5} | {NAMA:<15}| {NIS:<4} | {NILAI:^5}| {BEASISWA:<8}| {LAHIR:<9}|')
    

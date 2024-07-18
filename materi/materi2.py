print("=====Logika Dari Pelajaran Kemarin=====\n\n")
#kasus gabungan
#(+++++5------10+++++)
print("Logika OR\n")
inputangka = int(input("Masukan angka kurang dari 5 atau lebih dari 10: "))

Kurangdari = (inputangka < 5)
print(f'ini kurang dari 5: {Kurangdari}')
lebihdari = (inputangka > 10)
print(f"ini lebih dari 10: {lebihdari}")

keputusan = Kurangdari or lebihdari #logika mengunakan OR
if keputusan == True:
    print(f"\nNilai yang anda masukan: benar")
else:
    print(f"\nNilai yang anda masukan: salah karna {inputangka} nilainya kurang dari 10 atau lebih dari 5")
    
#kasus irisan
#(-----5++++++10------)
print("\nLogika AND\n")
inputangka2 = int(input("Masukan angka Lebih dari 5 dan kurang dari 10: "))

Lebihdari5 = (inputangka2 > 5)
Kurangdari10 = (inputangka2 < 10)
print(f"kurang dari: {Kurangdari10}")
print(f"Lebih dari: {Lebihdari5}")
keputusan2 = Lebihdari5 and Kurangdari10
if keputusan2 == True:
    print(f"\nNilai yang anda masukan: benar")
else:
    print(f"\nNilai yang anda masukan: salah karna {inputangka2} nilainya kurang dari 5 / lebih dari 10")

#Gabungan dari kedua materi AND dan OR

inputangka3 = int(input("\nMasukan angka diantara 0-5 atau diantara 8-11: "))

lebihdari0 = (inputangka3 >= 0)
kurangdari5 = (inputangka3 <= 5)
keputusan3 = lebihdari0 and kurangdari5

lebihdari8 = (inputangka3 >= 8)
kurangdari11 = (inputangka3 <= 11)
keputusan4 = lebihdari8 and kurangdari11

final = keputusan3 or keputusan4

if final == True:
    print("\nNilai yang anda masukan: benar")
else:
    print(f"\nNilai yang anda masukan: salah karna {inputangka3} nilainya bukan diantara 0-5 / diantara 8-11")

inputangka5 = int(input("\nMasukan nilai kurang dari 0 atau diantara 5-8 atau lebih dari 11:"))

kurang0 = (inputangka5 <= 0)
lebih11 = (inputangka5 >= 11)

lebih5 = (inputangka5 >= 5)
kurang8 = (inputangka5 <= 8)
hitungan = lebih5 and kurang8

keputusan_final = (kurang0 or lebih11) or hitungan

if keputusan_final == True:
    print("\nNilai yang anda masukan: benar")
else:
    print("\nNilai yang anda masukan: salah")
    print(f"Karena {inputangka5} nilainya TIDAK diantara 5-8 / lebih dari 0 dan kurang dari 11")

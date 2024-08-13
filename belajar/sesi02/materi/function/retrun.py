import os
# Fungsi kuadrat

def kuadrat(angka):
    hasil = angka**2
    return hasil
os.system("cls")

print(kuadrat(2))

kl = 90
i = kuadrat(kl)
print(i)

# fungsi deengan return banyak

def banyak(x, y):
    kali = x * y
    bagi = x / y
    tambah = x + y
    kurang = x - y
    return kali, bagi, tambah, kurang

print(banyak(1,1))
# jika ingin memisah

o, p, q, r = banyak(9, 9)
print(o)
print(p)
print(q)
print(r)



# JADI return itu akan langsung mengeluarkan dan menghitung dalam 1 variable 
# kasarnya menganti kan print di dalam def
# INTINYA JIKA DI DEPANYA ADA VARIABLE PAKE RETURN KALO NGGA GA USAH GPP    
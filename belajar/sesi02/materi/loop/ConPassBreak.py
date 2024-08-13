#pass
print(10*'-'+"pass"+10*'-')

n = 0
while n < 2:
    n += 1
    if n == 1:
        pass #pass adalah untuk meng skip atau agar tidak di eksekusi dalam contoh ini adlah si if

#continue
print(10*'-'+"continue"+10*'-')

i = 0
while i < 5:
    i += 1
    print(i)
    if i == 2:
        print("waloo")
        continue # jadi continue itu untuk meng skip kode di bawahnya si loop akan kembali ke loop awal (apa pun yang ketemu continue akan terskip)
    print(f"ini angka {i}") # saat di angka 2 sintaks ini ter skip
print(40*"-")

#break
print(10*'-'+"break"+10*'-') #langsung nge end

o = 0
while o < 5:
    o += 1
    print(f"hihi{o}")    
    if o == 3:
        print("berhenti")
        break
    print("yo")
print(40*"-")

o = 0
while True:
    o += 1
    print(f"hihi {o}")    
    if o == 3:
        print("berhenti")
        break
    print("yo")
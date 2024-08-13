sisi = 5

#mengunbakan for
tambahan = 1
for i in range(sisi):
    print("*"*tambahan)
    tambahan += 1

print(40*"-")

# mengunakan while
t1 = 1
while t1 <= sisi:
    print("*"*t1)
    t1 += 1
# cara 2
t2 = 1
while True:
    print("-"*t2)
    t2 += 1
    if t2 > 5:
        break
# mengunakan continue
# ini cara yang di  youtube 
t3 = 1
while True:
    if t3%2:
        print("_"*t3)
        t3 += 1
    else:
        t3 += 1
        continue
    if t3 > 5:
        break
# ini cara dari aku sendiri
t4 = 1
while True:
    if t4%2 == 0:
        print("*"*t4)
        t4 += 1
    else:
        t4 += 1
        continue
    if t4 > 5:
        break

const = 1
panjang = int(input("masukan panjang itunya: "))
spasi = int(panjang // 2)
while True:
    if const%2:
        print(" "*spasi+"+"*const)
        const += 1
        spasi -= 1
    else:
        const += 1
        continue
    if const > panjang:
        break
print(40*"-")
while True:
    if const%2:
        spasi += 1
        print(" "*spasi+"+"*const)
        const -= 1
    else:
        const -= 1
        continue
    if const == 0:
        break
    
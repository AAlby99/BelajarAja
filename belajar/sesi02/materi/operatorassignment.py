print('----operator assignment----')
# operasi yang dilakukan dengan penyingkatan
# operasi di tambah dengan assigment

a = 5 #adalah assignment

a += 1 #artinya sama dengan a = a + 1
print(f'nilai a: {a}')

a -= 2 #artinya sama dengan a = a - 2
print(f'nilai a: {a}')

a *= 2 #artinya sama dengan a = a * 2
print(f'nilai a: {a}')

a /= 2 #artinya sama dengan a = a / 2
print(f'nilai a: {a}')

#itu nilai a nya nyambung dari yang terbaru bukan variable yang pertama

b = 10 
b %= 3 #sisa saat di bagi
print(f'\nnilai b: {b}')  

b = 10
b //= 3
print(f'\nnilai b: {b}')

c = 10
c **= 2 #ini pangkat
print(f'\nnilai c: {c}')
print('----operator assignment----')
# Operasi yang dilakukan dengan penyingkatan
# Operasi ditambahkan dengan assignment

a = 5  # Adalah assignment

a += 1  # Artinya sama dengan a = a + 1
print(f'nilai a: {a}')

a -= 2  # Artinya sama dengan a = a - 2
print(f'nilai a: {a}')

a *= 2  # Artinya sama dengan a = a * 2
print(f'nilai a: {a}')

a /= 2  # Artinya sama dengan a = a / 2
print(f'nilai a: {a}')

# Nilai a nya nyambung dari yang terbaru bukan variable yang pertama

b = 10
b %= 3  # Sisa saat di bagi
print(f'\nnilai b: {b}')

b = 10
b //= 3 # pembagian Bulat kke bawah
print(f'\nnilai b: {b}')

c = 10
c **= 2  # Ini pangkat
print(f'\nnilai c: {c}')

print('operasi bitwise')
ob = True
print(f'\nNilai ob = {ob}')
c |= False
print(f'\nNilai ob |= False menjadi: {ob}')
# AND bitwise
c &= True
print(f'\nNilai ob &= True menjadi: {ob}')

# XOR bitwise
c ^= False
print(f'\nNilai ob ^= False menjadi: {ob}')

# NOT bitwise
c = not ob
print(f'\nNilai not ob menjadi: {c}')
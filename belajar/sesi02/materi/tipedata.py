print("----is dan is not----")
a = 4
b = 4
c = 5
print(hex(id(a)))
print(hex(id(b)))#karna nilai a dan b sama maka id hex nya sama 
print(hex(id(c)))
print(a is b)  # True, karena a dan b adalah objek yang sama
print(a is not c)  # True, karena a dan c adalah objek yang berbeda
print(a is c) # False, karena a dan c adalah objek yang berbeda

print("----not, or, and, xor----")
#not 
a = False
b = True
c = not a
d = not b
print(c) # mwmbalikan fakta
print(d)
print("--OR--")
# or (Jika salah satu nilai ada yang true maka nilai yang lain ikut true jika tidak maka akan tetap false )
a = False
b = False
c = a or b
print(f'{a} or {b} = {c}')
a = False
b = True
c = a or b
print(f'{a} or {b} = {c}')
a = True
b = False
c = a or b
print(f'{a} or {b} = {c}')
a = True
b = True
c = a or b
print(f'{a} or {b} = {c}')
print("--AND--")
# AND (and adalah kebalikan dari or)
a = False
b = False
c = a and b
print(f'{a} and {b} = {c}')
a = False
b = True
c = a and b
print(f'{a} and {b} = {c}')
a = True
b = False
c = a and b
print(f'{a} and {b} = {c}')
a = True
b = True
c = a and b
print(f'{a} and {b} = {c}')
print("--XOR--")
# XOR (xor jika nilai salah satu nya adalah nilai true sisanya False)
a = False
b = False
c = a ^ b
print(f'{a} xor {b} = {c}')
a = False
b = True
c = a ^ b
print(f'{a} xor {b} = {c}')
a = True
b = False
c = a ^ b
print(f'{a} xor {b} = {c}')
a = True
b = True
c = a ^ b
print(f'{a} xor {b} = {c}')

print("\nbitwise")
a = 5
b = 9
print(f"nilai: {a}, binary: {format(a,'08b')}")
print(f"nilai: {b}, binary: {format(b,'08b')}")
# or
c = a | b
print(f"nilai: {c}, binary: {format(c,'08b')}")
# and
c = a & b
print(f"nilai: {c}, binary: {format(c,'08b')}")
# xor
c = a ^ b
print(f"nilai: {c}, binary: {format(c,'08b')}")
# not
c = ~ a
print(f"nilai: {c}, binary: {format(c,'08b')}")
# shifting menggeser nilai biner
print('\nnilai asli')
print(f"nilai: {b}, binary: {format(b,'08b')}")
print('ke kanan')
c = b >> 2
print(f"nilai: {c}, binary: {format(c,'08b')}")
print('ke kiri')
c = b << 2
print(f"nilai: {c}, binary: {format(c,'08b')}")
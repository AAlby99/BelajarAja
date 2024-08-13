buah = ["jeruk", "semangka", "kiwi", "apel"]
a = buah
b = a
print(a)
print(b)

a[1] ="limau"
b.sort() 
# ini akan merubah ke 2 list yang seharusnya tidak  
print(a)
print(b)    

#adress dari ke 2 list 
print(f"adress dari a: {hex(id(a))}")   
print(f"adress dari b: {hex(id(b))}")
# tuh id hex nya sama persistent    
# output dari a dan b sama persis pada baris ke 2 ini 
print(40*"-")

## Jadi solusinya meb=ngunakan copy
buahh = ["jeruk", "semangka", "kiwi", "apel"]
a = buahh
b = a.copy() # mengunkan ini agar si b membuat list baru
print(a)
print(b)

a[1] ="limau"
b.sort() 
print(a)
print(b)    

#adress dari ke 2 list 
print(f"adress dari a: {hex(id(a))}")   
print(f"adress dari b: {hex(id(b))}")
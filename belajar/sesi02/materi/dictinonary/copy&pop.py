# COPY 
# mirip mirip lah sama yang list

unsur = {
    'li' : 'lithium',
    'o' : 'oksigen',
    'he' : 'helium',
    'ni' : 'nikel',
    'e' : 'energi'
}
print(40*'-')

element = unsur.copy()

# POP dictionary

e = element.pop('li') # pop berdasarkan key
print(f'value {e} di ambil dari element atas nama key "li"')
print(f'jadi data li menghilang dari Element \n{element}')

# KESIMPULAN jadi si pop ini mengtranfer dari data "element" ke data "e" jadinya di data "element" key dan value dari li menghilang karna 
# sudah di pindah ke "e"
print(40*'-')

# popitem() 
lastpage = element.popitem() # mengambil data terakhir
print(lastpage)
print(element)




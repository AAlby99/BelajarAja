# list

#data numbers
numbers = [1, 2, 3, 4, 5]
print(numbers)

#data string
names = ['Alby', 'Havi', 'Alvi', 'Krupuk']
print(names)

# data bolean

mood = [True, False, True, True]
print(mood)

#data campuran/mix

mixed_data = [1, 2, 'Alby', True, [2, 3, 4]]
print(mixed_data)

print(40*"-")
# alternatif membuat data list ( with range)
data_range = range(0,5)
data_list = list(data_range)
print(data_list)
#mengunakan inkremen 
data_range = range(0,10,2) # keliapatan 2 (koma ke 3 itu ingkremen (start, stop, step))
data_list = list(data_range)
print(data_list)
print(40*"-")

# list dengan for loop, list comprehension
list_for = [i for i in range(0,10)]
print(list_for)
# pake kuadrat ato penjumlahan lainya
list_for = [i**2 for i in range(0,10)]
print(list_for)
print(40*"-")

# list dengan for dan if

list_for_if = [i for i in range(0,10) if i != 3] # jadi 3 nya hilang
print(list_for_if)
#membuat bilangan hanya bilangan genap
list_for_if = [i for i in range(0,10) if i%2 ==0] # jadi jika hasilnya di bagi lalu sama dengan 0 maka hasil tersebut tidak akan muncul
print(list_for_if)
#memebuat bilangan ganjil
list_for_if = [i for i in range(0,10) if i%2 ==1] # jadi jika hasilnya di bagi lalu sama dengan 0 maka hasil tersebut tidak akan muncul
print(list_for_if)

#jadi logika nya adalah saat data itu memenuhi syarat di if maka data tersebut akan di munculkan yang tidak memenuhi syarat maka akan di hilangkan dari list
print(40*"-")


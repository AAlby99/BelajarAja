# type hints


def fungsi_dengan_hints(argumen:int):
    output = 10**argumen
    return output

print(fungsi_dengan_hints(3))  

# JADI jika mouse kita di taro ke nama fungsinya maka sugestinya akan memberitau kalo tipe data yang sesuai apa

def tanpa_return(init:str):
    print(init)

tanpa_return("Hello, World!") # jika tanpa return makan -> nya akan menjadi none


def panah(i:int) -> int:
    return i * 2

print(panah(5)) # jika mengunakan -> pada def maka jika sedang di anu akan memberitau type outputnya 


# INI OPSIONAL TIDAK WAJIB CUMA BUAT HINTS
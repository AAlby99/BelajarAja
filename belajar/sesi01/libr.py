import socket
from time import sleep

nama_pc = socket.gethostname()
def welcome():
    samadengan = "=" * (len(nama_pc) + 11)
    # tambahan = len(sambutan) + 11
    # tbh = samadengan * tambahan 
    print(samadengan)
    print(f"====={nama_pc}======")
    print(samadengan)
    print('''
    Hay siap untuk bermain game??  PERHATIKAN GOA DI BAWAH 
    sebelum itu isi dulu ya..''')

def keluar():
    print("Program akan di hentikan dalam ")
    print('3...')
    sleep(1)
    print('2...')
    sleep(1)
    print('1...')
    sleep(1)
    print('program dihentikan')
    exit()
if __name__ == '__main__':
    welcome()
    keluar()
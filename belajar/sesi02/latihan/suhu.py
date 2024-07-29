def start():   
    while True:
        print("\nKONFRENSI TEMPERATUR\n")
        
        choice = int(input('Pilih Pengkonffrensian\n1. Celcius\n2. Fahrenheit\n3. Kelvin\n4. Reamur\nMasukan Pilihan: '))
        if choice == 1:
            suhu = input('Masukkan TEMPERATUR (tekan q untuk berhenti): ')
            if suhu == 'q':
                print('Program Dihentikan')
                break
            else:
                cel = float(suhu)
                far = (cel * 9/5) + 32 
                kel = cel + 273.15 
                rea = (4/5) * cel
                print(f'suhu adalah {cel} Celcius')
                print(f'suhu adalah {far} Fahrenheit')
                print(f'suhu adalah {kel} Kelvin')
                print(f'suhu adalah {rea} Reamur')
        elif choice == 2:
            suhu = input('Masukkan Temperatur (tekan q untuk berhenti): ')
            if suhu == 'q':
                print('Program Dihentikan')
                break
            else:
                far = float(suhu)
                cel = (far - 32) * 5/9
                kel = (far - 32) * 5/9 + 273,155 
                rea = (4/9) * (far -32)
                print(f'suhu adalah {cel} Celcius')
                print(f'suhu adalah {far} Fahrenheit')
                print(f'suhu adalah {kel} Kelvin')
                print(f'suhu adalah {rea} Reamur')
        elif choice == 3:
            pass
        elif choice == 4:
            pass
        else:
            print("Invalid")
            break

if __name__ == "__main__":
    start()


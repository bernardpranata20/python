import random
print ('Nyok maen suit!')
while True:
    
    Pilihan = ['batu', 'gunting', 'kertas']
    A = input("Pilih salah satu dari batu, gunting, kertas!  ")

    suitan = Pilihan[random.randint(0,2)]
    if A == 'batu' and suitan == 'batu':
        print('seri')
    elif A == 'batu' and suitan == 'kertas':
        print('menang')
    elif A == 'batu' and suitan == 'gunting':
        print('kalah')
    elif A == 'gunting' and suitan == 'gunting':
        print('seri')
    elif A == 'gunting' and suitan == 'kertas':
        print('menang')
    elif A == 'gunting' and suitan == 'batu':
        print('kalah')
    elif A == 'kertas' and suitan == 'kertas':
        print('seri')
    elif A == 'kertas' and suitan == 'batu':
        print('menang')
    elif A == 'kertas' and suitan == 'gunting':
        print('kalah')
        
    
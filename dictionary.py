print('Key and Value Dictionary')
Identitas = {}

tries = 0
while tries !=3:
    print('=============================================')

    a = input('masukkan key yang ingin ditambahkan  : ')
    b = input('masukkan value yang ingin ditambahkan: ')
    tries += 1
    
    Identitas[a] = b

for key, value in Identitas.items():
    print(key, value)
    
    
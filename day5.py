print('Identitas Diri')
datas = []
data = {}

while True:
    data = {}
    a = input('masukkan nama anda: ')
    b = int(input('masukkan umur anda: '))
    c = input('masukkan hobi anda: ')

    data["nama"] = a
    data["umur"] = b
    data["hobi"] = c
    datas.append(data)
    d = input('apakah masih mau mengisi lagi? (yes/no) ')
    if d == "yes":
        continue
    elif d == 'no':
        for data in datas:
            for key, value in data.items():
                print(key, value)
        break       

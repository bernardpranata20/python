username = 'bernard'
password = '12345'
tries = 0
while tries !=3:
    username1 = input('masukkan username anda: ')
    password1 = input('masukkan password anda: ')
    if username1 == username and password1 == password:
        print("berhasil")
    else:
        print("coba lagi")
    tries += 1
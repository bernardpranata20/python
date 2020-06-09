username = 'bernard'
password = '12345'

username1 = input('masukkan username anda: ')
password1 = input('masukkan password anda: ')

while username1 != username and password1 != password:
    print('Ulang')

    username1 = input('masukkan username anda: ')
    password1 = input('masukkan password anda: ')

    print('selamat datang')
    tries += 1
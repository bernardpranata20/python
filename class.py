class Orang:
    def __init__(self, nama, umur, asal, gender):
        self.nama = nama
        self.umur = umur
        self.asal = asal
        self.gender = gender

    def info(self):
        print(f'Namanya adalah {self.nama} ia berusia {self.umur}. Ia berasal dari {self.asal}. Ia adalah seorang {self.gender}')

a = input('Nama anda: ')
b = input('Umur anda: ')
c = input('Asal anda: ')
d = input('Gender anda: ')
Orang1 = Orang(a, b, c, d)


Orang1.info()

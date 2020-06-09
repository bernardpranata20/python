a = input('Nama bunga: ')
b = int(input('Jumlah Kelopak: '))
c = float(input('Harga Bunga: '))

class Bunga:
    def __init__(self, Nama, Kelopak, Harga):
        self.Nama = Nama
        self.Kelopak = Kelopak
        self.Harga = Harga
        print(f'Bunga {self.Nama} memiliki kelopak {self.Kelopak} dan harganya adalah {self.Harga}. ')


    def Editnama(self,a):
        self.Nama = a

    def Editkelopak(self, b):
        self.Kelopak = b

    def Editharga(self, c):
        self.Harga = c

    def nama2(self):
        return(self.Nama)

    def jumlah2(self):
        return(self.Kelopak)

    def harga2(self):
        return(self.Harga)

        
namabaru = input('Nama bunga: ')
kelopakbaru = int(input('Jumlah Kelopak: '))
hargabaru = float(input('Harga Bunga: '))
Bunga = Bunga(a, b, c)
Bunga.Editnama(namabaru)
Bunga.Editkelopak(kelopakbaru)
Bunga.Editharga(hargabaru)
Nama = Bunga.nama2()
Jumlah = Bunga.jumlah2()
Harga = Bunga.harga2()
print(Nama, Jumlah, Harga)



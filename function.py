def luas(x,y):
    return (x*y)

def volume(x,z):
    print("hasilnya", x*z)
panjang = int(input("masukkan panjang persegi panjang "))
lebar = int(input("masukkan lebar persegi panjang "))

hasil = luas(panjang, lebar)
Tinggi = int(input("masukkan tingginya "))

volume(hasil, Tinggi)
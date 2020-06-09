print("PAYMENT COMPUTATION FOR EMPLOYEES")
print("---------------------------------")
def pembayaran(x,y):
    if Jam > 10:
        return (x*y+ 200)
    elif Jam <= 10:
        return (x*y)
Jam = int(input("Hours:  "))
biaya = int(input("Rate:  "))
hasil = pembayaran(Jam, biaya)
print(hasil)
import random
print ('Nyok maen tebak angka!')
angka = random.randint(1,11)
A = int(input("Masukkin aje angka dari 1-10! "))
while True:
    if A < angka :
        print("Kekecilan mas")
        A = int(input("Masukkin aje angka dari 1-10! "))
    if A > angka:
        print("apalagi ini kegedean mas")
        A = int(input("Masukkin aje angka dari 1-10! "))
    if A == angka:
        print("Cakepp bener luu!!!!")
        break

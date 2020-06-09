print("Kalkulator kane")
tries= 0
while tries !=3:
    a = int(input("masukkan angka pertama: "))
    b = int(input("masukkan angka kedua: "))
    c = int(input("pilih salah satu 1{+} 2{-} 3{x} 4({/} ? "))
    hasil1 = a + b
    hasil2 = a - b
    hasil3 = a * b
    hasil4 = a / b

    if c == 1:
        print (f'{hasil1}')
    elif c == 2:
        print (f'{hasil2}')
    elif c == 3:
        print (f'{hasil3}')
    elif c == 4:
        print (f'{hasil4}')
    tries +=1
print("---Selamat Datang di Kalkulator Sederhana---")
def add(a,b):
    add = a+b
    return add
def subtract(a,b):
    subtract = a-b
    return subtract
def multiply(a,b):
    multiply = a*b
    return multiply
def divide(a,b):
    divide = a/b
    return divide
def hasil(pilihan,a,b):
    if pilihan == "+" :
        return add(a,b)
    elif pilihan == "-" :
        return subtract(a,b)
    elif pilihan == "X":
        return multiply(a,b)
    else:
        return divide(a,b)

pilihan = input("Masukan operator matematika yang ingin Anda hitung: ")
a = int(input("masukan angka pertama: "))
b = int(input("masukan angka kedua: "))
print(hasil(pilihan,a,b))


print("SELAMAT DATANG DI PROGRAM PEMBUAT PIRAMIDA BERLUBANG")
angka = int(input("Masukan Angka: "))
x = 10
y = 20
for i in reversed(range(10)):
    for j in range(i+1):
        print(' ', end='')
    for k in range(x+1):
        if k==0:
            print('*', end='')
        else:
            print(' ', end='')
    for l in range(x):
        if l==y:
            print('*', end='')
            x+=1
        else:
            print(' ', end='')
    x+=1
    print()
for i in range(11):
    print('* ', end='')

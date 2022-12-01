y = input("Masukan Kata: ")
palindrome = True
panjang_y = len(y)
for i in range(panjang_y//2):
    if (y[i] != y[panjang_y-i-1]):
        palindrome = False
        break
if palindrome:
    print ("Yes")
    print ("Jika dibalik: ", y)
else :
    print ("No")
    print ("Jika dibalik: ", y)
    

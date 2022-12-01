def add(a,b):
    add = a + b
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
    if pilihan == 1:
        return add(a,b)
    elif pilihan == 2:
        return subtract(a,b)
    elif pilihan == 3:
        return multiply(a,b)
    else :
        return divide(a,b)

print ("Select operation")
print ("1. Add")
print ("2. Subtract")
print ("3. Multiply")
print ("4. Divide")

pilihan = int(input("Enter choice(1/2/3/4): "))
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print (hasil(pilihan,a,b))




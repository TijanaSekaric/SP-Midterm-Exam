suma = 0
n=0

print("Unesite broj ili =")

while True:
    x=input()
    if x=='=':
        print(" Srednja vrijednost brojeva je: " + str(suma/n))
        break
    suma+=int(x)
    n+=1


 #!/usr/bin/env ptyhon3
import time

def separador(exercici):
    print("#" * 25)
    print("#")
    print("# Exercici " + str(exercici))
    print("#")
    print("#" * 25)
    
'''
separador(1)

number = 0
while number != 5:
    number += 1
    print(number,"mississipi")
    time.sleep (1)    
print("Tothom a tingut teeeeemps!!!!")


separador(2)

while True:
    chupa = input("Digues la praula clau per sortir del bucle. Pista (chupa): ")

    if chupa.lower() == "chupacabra":
        print("¡Has escapat del bucle, felicitats chavaaaaaaaal!!!")
        break
    
    
separador(3)

paraula = input("Digues una paraula: ")

paraula = paraula.upper()

llet = ""

for lletra in paraula:
    if lletra in ['A', 'E', 'I', 'O', 'U']:
        continue
    llet += lletra

print("A continuació obtindràs les lletres no vocals de la teva paraula:")
for lletra in llet:
    print(lletra)
    


separador(4) 

paraula = input("Digues una paraula: ")

paraula = paraula.upper()

llet = ""

for lletra in paraula:
    if lletra in ['A', 'E', 'I', 'O', 'U']:
        continue
    llet += lletra

print("La paraula sense vocals:", llet)


separador(5) 

diners = float(input("Quants diners vols invertir? "))
interes = float(input("Quan és l'interes anual?"))
anys = int(input("Durant quants anys? "))

interes = interes / 100.0

print("Aquesta és la quantitat de diners guanyats per cada any")
for any in range(1, anys + 1):
    capital = diners * (1 + interes)**anys
    print(f"La capital aconseguida ha estat de {capital}")

separador(6)

numero = int(input("Digues un numero del 1 al 20: "))

for i in range(1, numero*2,2):
    for j in range(i,0,-2):
        print(j, end=' ')
    print()
    


separador(7)

numero = int(input("Bro, digues un numero sencer: "))

if numero > 1:
    for i in range(2, int(numero**0.5) + 1):
#per fer això d'aqui adalt ho he buscat al chat gpt, les mates como que no
        if (numero % i) == 0:
            print(f"{numero} no es un número primo.")
            break
    else:
        print(f"{numero} es un número primo.")


separador(8)

paraula = input("Digues una paraula: ")

for lletra in reversed(paraula):
    print(lletra)
    

separador(9)

frase = input("Digues la teva frase: ")
lletra = input("Digues la lletra que vols contar: ")
recompte = 0

for lletraa in frase:
    if lletraa == lletra:
        recompte += 1

# Mostrar el resultado
print(f"En la frase que has posat, la lletra {lletra} surt {recompte} cops durant tota la frase.")

'''
separador(10)

blocs_usuari = int(input("Ingresa el número de bloques: "))

altura = 0
blocs= 0

while blocs <= blocs_usuari:
    altura += 1
    blocs += altura

if blocs > blocs_usuari:
    altura -= 1

print("La altura de la pirámide es:", altura)



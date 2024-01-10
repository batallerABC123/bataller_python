opcio = input("tria una opció:")

while opcio != "X":
   
    if opcio == "M":
        print("Moto")
        break
    if opcio == "C":
        print("Cotxe")
        break
    
import time 

for i in range(10):
    print("a")
    print("a", end="") 
    time.sleep(1)   
    
    
numero_secret = 777

while True:
    usuari = int(input("Digues un número: "))

    if usuari == numero_secret:
        print("¡Ben fet, muggle! Ets lliure.")
        break
    else:
        print("¡Ja, ja! ¡Estàs atrapat en el meu bucle tonto!")
        
num = int(input("Digues un numero sencer: "))

if num % 2 == 0:
    print("El número,", num, "es par.")
else:
    print("El número,", num, "es impar.")
    
renta = float(input("Ingres de la renta anual: "))

if renta < 10000:
    percentatge = 5
elif renta <= 20000:
    percentatge = 15
elif renta <= 35000:
    percentatge = 20
elif renta <= 60000:
    percentatge = 30
elif renta > 60000:
    percentatge = 45
    
print(f"El teu impost és de {percentatge}%")



gender = input("What is your gender? (F/M)")
name = input("What is your name?")
name_begins = input("Initial of your name?")

if gender == "F":
    if name_begins < "M":
        group = "A"
    else:
        group = "B"
else:
    if name_begins > "N":
        group = "A"
    else:
        group = "B"
        
print(f"Your group is {group}")




lletra = int(input("Quin número te la el primer byte?"))

if lletra < 127:
    classe = "A"
elif lletra < 192:
    classe = "B"
elif lletra < 224:
    classe = "C"
elif lletra < 240:
    classe = "D"
elif lletra < 256:
    classe = "E"
else:
    classe = 'No pertenece a ninguna clase'


if classe == "A":
    tipus = "privada"
elif classe == "B":
    tipus = "privada"
elif classe == "C":
    tipus = "privada"
else:
    tipus = "pública"
    
print(f"La classe és {classe} i és de tipus {tipus}.")


        
        
        

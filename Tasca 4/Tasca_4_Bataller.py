#!/usr/bin/env ptyhon3

def separador(exercici):
    print("#" * 25)
    print("#")
    print("# Exercici " + str(exercici))
    print("#")
    print("#" * 25)
    
'''
separador(1)

ingres = float(input("Digues el teu ingres anual:"))

exencio_fiscal = 556.02

if ingres <= 85528:
    impost = round(0.18 * ingres - exencio_fiscal)
else:
    impost = round(14839 + 0.32 * (ingres - 85528))

impost = round(impost, 0)

print("El impuesto es:", impost, "pesos")


separador(2)

any = int(input("Introduce un año:"))

if any < 1582:
    print("Has de posar dins del periode del calendari")
else:
    if (any %4 != 0) or (any /100 == 0 and any & 500 != 0):
        print("Any comú")
    else:
        print("Any Bisiesto")
    



separador(3)

numero_secret = 777

print(
"""
+==================================+
| ¡Benvingut al meu joc, muggle!   |
| Introdueix un nombre enter       |
| i endevina quin número he        |
| triat per a tu                   |
| Llavors,                         |
| Quin és el número secret?        |
+==================================+
""")

while True:
    usuari = int(input("Digues un número: "))

    if usuari == numero_secret:
        print("¡Ben fet, muggle! Ets lliure.")
        break
    else:
        print("¡Ja, ja! ¡Estàs atrapat en el meu bucle tonto!")


separador(4)

num = int(input("Digues un numero sencer: "))

if num % 2 == 0:
    print("El número,", num, "es par.")
else:
    print("El número,", num, "es impar.")
    
    
separador(5)

edat = int(input("Digues la teva edat:"))
ingres = float(input("Digues la quantitat de diners que cobres mensualment:"))


if edat > 16 and ingres >=1000:
    print("Has de tributar")
else:
    print("No has de tributar, quina sort!")
    

separador(6)

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



separador(7)

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



separador(8)

evaluacio = float(input("Puntuació del treballador: "))

if evaluacio == 0.0:
    nivell = "Inacceptable"
elif evaluacio == 0.4:
    nivell = "Aceptable"
elif evaluacio >= 0.6:
    nivell = "Impresionant"
else:
    nivell = "Invàlid"
    evaluacio = 0.0
diners = evaluacio * 2400

print(f"El teu nivell és de {nivell}")
print(f"Els quantitat de diners per el teu nivell és de {diners} ")


separador(9)

print("Abans de poder entrar has de dir la teva edat.")
edat = int(input("Quina edat tens?"))

if edat < 4:
    diners = 0
elif edat < 18:
    diners = 5
else:
    diners = 10
    
print(f"ELs diners que has de pagar per la teva edat son {diners}€.")


separador(10)

print("Com a tot restaurant, hauràs de dir la pizza que vols...")
pizza_client = input("La vols de vegetaria o no? (si/no): ")

ingredients_si = ["mozzarella", "tomate"]

if pizza_client.lower() == "si":
    print("Aquests són els ingredients vegetarians disponibles: Pebrot i Tofu.")
    ingredient_opcional = input("Digues un ingredient: ")
    ingredients = ingredients_si + [ingredient_opcional]
    la_pizza = "si que és Vegetariana,"
else:
    print("Aquests són els ingredients no vegetarians disponibles: Pebrot, Pernil i Salmó.")
    ingredient_opcional = input("Digues un ingredient: ")
    ingredients = ingredients_si + [ingredient_opcional]
    la_pizza = "no és Vegetariana,"

print(f"La pizza que has escollit {la_pizza} la qual està feta amb aquests ingredients: {', '.join(ingredients)}")



separador(11)

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


'''
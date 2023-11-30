#!/usr/bin/env ptyhon3

def separador(exercici):
    print("#" * 25)
    print("#")
    print("# Exercici " + str(exercici))
    print("#")
    print("#" * 25)
'''
separador(1)

nom_user = input("Porfa, posa el teu nom guapi:")
print(f"¡Ei \"{nom_user}\"!")

separador(2)

juan = 3
maria = 5
adan = 6

print(juan, maria, adan)

total_pomes = 14

print(f"El total de pomes és de {total_pomes}.")

print("El que no explica l'història és que juan tenia 6 pomes més, però les tenia amagades.")
print("\n")

juan_extra = 6

total_real = total_pomes + juan_extra

print(f"Així que realment la suma total és de, {total_real}.")

separador(3)

kilometers = 12.25
miles = 7.38

miles_to_kilometers = miles * 1.61 
kilometers_to_miles = kilometers / 1.61 

print(miles, "millas son", round(miles_to_kilometers, 2), "kilómetros")
print(kilometers, "kilómetros son", round(kilometers_to_miles, 2), "millas")

separador(4)

x = float(input("Dona-li valor a la x"))
y = 3*x**3 - 2*x**2 + 3*x-1

print("El resultat és" , y)


separador(5)

hores_treballades = float(input("Quantes hores has treballat?"))
euros_x_hora = float(input("Quants diners per hora?"))

sou = hores_treballades * euros_x_hora

print("El resultat del sou és de" , sou) 


separador(6)

n = int(input("Digues un numero sencer POSITIU"))

if n <= 0:
    print("QUE SIGUI POSITIU")
    
else: suma = n * (n + 1) // 2

print("El resultat és" , suma)


separador(7)

pes = float(input("Quan peses?"))
mesura = float(input("Quan medeixes?"))

imc = pes / (mesura**2)
imc = round(imc,2)

print("EL teu imc és de", imc)


separador(8)

invertir = float(input("Quans diners vols invertir?"))
interes = float(input("Quin és l'interés anual?"))
anys = float(input("Durant quants anys?"))

valor_final= invertir + (invertir + interes / 100) * anys

print("Després dels", int(anys), "anys, el valor final serà de", valor_final)


separador(9)

byte1 = input("Digues el primer byte d'una direcció IP")
byte2 = input("el segon byte")
byte3 = input("el tercer byte")
byte4 = input("el quarat byte")

direcció_ip = byte1 + "." + byte2 + "." + byte3 + "." + byte4

print("La direcció Ip és" + direcció_ip)


separador(10)

hora =int(input("Hora d'inici (hores): "))
minuts =int(input("Minut d'inici (minutos): "))
duracio =int(input("Duració del event (minuts): "))

total_minuts = duracio + minuts

hores_finals = hora + total_minuts // 60
minuts_finals = total_minuts % 60

print("L'event començarà a les ", hora, ":", minuts, " i dura ", duracio, " minuts. Així que acabarà a les ",  hores_finals , ":" , minuts_finals, sep="")
'''

separador(10.1)
#segonapart

dia =int(input("Dia (dies): "))
hora =int(input("Hora d'inici (hores): "))
minuts =int(input("Minut d'inici (minutos): "))
duracio =int(input("Duració del event (minuts): "))

total_minuts = duracio + minuts

hores_finals = hora + total_minuts // 60
minuts_finals = total_minuts % 60

if hores_finals > 23:
    dia_final= dia + 1
    hores_finals = hores_finals - 24

print("L'event començarà el dia ", dia , " a les ", hores_finals, ":", minuts, " i dura ", duracio, " minuts. Així que acabarà a les ",  hores_finals , ":" , minuts_finals," el dia ", dia_final,".", sep="")
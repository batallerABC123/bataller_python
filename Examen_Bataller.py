print(
"""
########################
EXERCICI 1
########################
""")

preu_moto = 300
preu_cotxe = 400
preu_final = 0

vehicle = input("Quin tipus de vehicle tens?:")

while vehicle != "X":
 
    if vehicle == "C":
        print(f"Preu Base {preu_cotxe}€")
        preu_final = preu_cotxe
        break
           
    if vehicle == "M":
        print(f"Preu Base {preu_moto}€")
        break
        
    if vehicle == "X":
        print("Adeu, gràcies")
        break
    

print(
"""
########################
EXERCICI 2
########################
""")
penalitzacio = 100

anys = int(input("Quants anys fa que tens carnet de conduir?"))

if anys < 10: 
    total_penalitzacio = preu_final + penalitzacio
    print(f"Penalització de 100€. El preu final és de {total_penalitzacio}") 
else:
    anys > 10
    preu_final = preu_final * (1 - ((anys-10)*0.01))
    print(f"Bonificació per experiència del 1% per cada any. El preu és de {preu_final}")


print(
"""
########################
EXERCICI 3
########################
""")

partes = int(input("Quants partes en contra tens en el darrer any?"))
if partes == 0:
    bonificacio = preu_final * 0.1
    preu_final = preu_final - bonificacio
    asteriscs = 10
    print("Bonificació de 10%")
    print(f"Preu final {preu_final}€")
elif partes <= 5:
    pena = preu_final * 0.2
    preu_final = preu_final + pena
    asteriscs = 20
    print("Penalitzacio de 20%")
    print(f"Preu final {preu_final}€")
else:
    print("No t'hi volem, suicida!")
    
    
print(
"""
########################
EXERCICI 4
########################
""")

for i in range(asteriscs):
    print("*", end=" ")
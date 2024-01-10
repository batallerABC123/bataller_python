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

sombrero = [1, 2, 3, 4, 5]
print(sombrero)
numuser = int(input("Digues el nou número central:"))

sombrero[2] = numuser
print(sombrero)

del sombrero[4]
print(sombrero)



separador(2)

beatles = []

beatles.insert(0,"John Lennon",)
beatles.insert(1,"Paul McCartney",)

for i in range(2):
    membre = input("Nom del mem3
    bre que afegim: ")
    beatles.append(membre)

print(beatles)



separador(3)

seguim = True
llista = []

while seguim:
    valor = input("Digues un número: ")
    if valor == "fi":
        seguim = False
    else:
        llista.append(int(valor))

print(llista)

for i in range(len(llista)-1):
    for j in range(len(llista)-1):
        if llista[j] > llista[j+1]:
            aux = llista[j]
            llista[j]=llista[j+1]
            llista[j+1] = aux
      
print(llista)


separador(3.1)

seguim = True
llista = [5,3,2,4,1]

print(llista)
for i in range(len(llista)-1):
    for j in range(len(llista)-1-i):
        if llista[j] > llista[j+1]:
            aux = llista[j]
            llista[j]=llista[j+1]
            llista[j+1] = aux
    print(llista)
    
   
separador(5)

numeros_usr = input("Digues números diferents dividits: ")

numeros = [int(num) for num in numeros_usr.split()]
numeros.sort()

print("Els números de major a menor")
for num in numeros:
    print(num)
    

separador(5.1)

numeros_usr = input("Digues números diferents dividits: ")

numeros = [int(num) for num in numeros_usr.split()]
numeros.sort()

print("Els números de menor a major:", numeros)


separador(6)
    
llista_assig = ["Matemàtiques", "Física", "Química", "Història", "Llengua"]
notes = 0
a_repetir = []

for assig in llista_assig:
    nota = float(input(f"Digues la teva nota a la assignatura de {assig}: "))
    if nota < 5: 
        a_repetir.append(assig)
        
print(f"Has de recuperar aquestes asssigantures: {a_repetir}")

'''
separador(7)

paraula = input("Digues una paraula: ")

if paraula.lower() == paraula.lower()[::-1]:
    print("És una paraula palíndromo")
else:
    print("És una paraula no palíndromo")

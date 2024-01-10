numero = int(input("Digues un numero del 1 al 20: "))

for i in range(1, numero*2,2):
    for j in range(i,0,-2):
        print(j, end=' ')
    print()
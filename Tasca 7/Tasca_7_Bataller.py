 #!/usr/bin/env ptyhon3


def separador(exercici):
    print("#" * 25)
    print("#")
    print("# Exercici " + str(exercici))
    print("#")
    print("#" * 25)
    
'''
separador(1)


def is_year_leap(year):
    if (year % 4 == 0 and year % 100 != 0 or year % 400 == 0):
       return True

    return False

test_data = [1900, 2000, 2016, 1987]
test_results = [False, True, True, False]
for i in range(len(test_data)):
	yr = test_data[i]
	print(yr,"->",end="")
	result = is_year_leap(yr)
	if result == test_results[i]:
		print("OK")
	else:
		print("Fallido")
  

separador(2)

def is_year_leap(year):
    if (year % 4 == 0 and year % 100 != 0 or year % 400 == 0):
        return True

    return False

def days_in_month(year, month):
    days = [31,28,31,30,31,30,31,31,30,31,30,31]
    if month != 2:
        result = days[month]
    else:
        if is_year_leap(year):
            result = 29
        else:
            result = days[month]
    return result
     
test_years = [1900, 2000, 2016, 1987]
test_months = [2, 2, 1, 11]
test_results = [28, 29, 31, 30]
for i in range(len(test_years)):
	yr = test_years[i]
	mo = test_months[i]
	print(yr, mo, "->", end="")
	result = days_in_month(year = yr, month = mo)
	if result == test_results[i]:
		print("OK")
	else:
		print("Fallido")
          

separador(3)

def is_year_leap(year):
    if (year % 4 == 0 and year % 100 != 0 or year % 400 == 0):
       return True

    return False

def days_in_month(year, month):
    if (year % 4 == 0 and year % 100 != 0 or year % 400 == 0):
        return True

    return False

def days_in_month(year, month):
    days = [31,28,31,30,31,30,31,31,30,31,30,31]
    if month != 2:
        result = days[month]
    else:
        if is_year_leap(year):
            result = 29
        else:
            result = days[month]
    return result

def day_of_year(year, month, day):
    days = [31,28,31,30,31,30,31,31,30,31,30,31]
    if month != 2:
        result = days[month]
    else:
        if is_year_leap(year):
            result = 29
        else:
            result = days[month]
    return result


separador(4)
#fàcil

def quadrat(num):
    resultat = num**2
    return resultat

def arrel_quadrada(num):
     quadrat_resultat = num**0.5
     return quadrat_resultat


def pitagoras(c,a):
    hipotenusa = arrel_quadrada(quadrat(a) + quadrat(c))
    return hipotenusa

print(f"Si els catets són 3 i 4, la hipotenusa és: {pitagoras(3,4)}")


separador(4)
#difícil
#primo: es pot dividir només per ell mateix i per 1.
num = int(input("Digues un numero: "))


def és_primo(num):
    primo = True
    for i in range(2, num):
	    if num % i == 0:
                primo = False
                break
    return primo
        
print(f"És primo: {és_primo(num)}")



separador(5)

def liters_100km_to_miles_gallon(liters):
    gallons = liters / 3.785411784 
    miles = 100 * 1000 / 1609.344
    return miles / gallons

def miles_gallon_to_liters_100km(miles):
    km_100 = miles * 1609.344 * 1000 / 100
    liters = 3.785411784
    return liters / km_100

print(liters_100km_to_miles_gallon(3.9))
print(liters_100km_to_miles_gallon(7.5))
print(liters_100km_to_miles_gallon(10.))
print(miles_gallon_to_liters_100km(60.3))
print(miles_gallon_to_liters_100km(31.4))
print(miles_gallon_to_liters_100km(23.5))


separador(5)

def liters_100km_to_miles_gallon(liters):
    gallons = liters / 3.785411784 
    miles = 100 * 1000 / 1609.344
    return miles / gallons

def miles_gallon_to_liters_100km(miles):
    km_100 = miles * 1609.344 * 1000 / 100
    liters = 3.785411784
    return liters / km_100

print(liters_100km_to_miles_gallon(3.9))
print(liters_100km_to_miles_gallon(7.5))
print(liters_100km_to_miles_gallon(10.))
print(miles_gallon_to_liters_100km(60.3))
print(miles_gallon_to_liters_100km(31.4))
print(miles_gallon_to_liters_100km(23.5))


separador(8)

def decimal_a_binari(decimal):
    binario = ''
    while decimal // 2 != 0:
        binario = str(decimal % 2) + binario
        decimal = decimal // 2
    return str(decimal) + binario


numero = int(input('Introduce el número a convertir a binario: '))
print(decimal_a_binari(numero))

'''
separador(9)

def es_vocal(lletra):
    vocals = "aeiouAEIOU"
    return lletra in vocals

def treu_vocals(paraula):
    return ''.join(letra for letra in paraula if not es_vocal(letra))

def treu_consonants(paraula):
    return ''.join(letra for letra in paraula if es_vocal(letra))

paraula_exemple = "Em pica l'ou esquerra."
sense_vocals = treu_vocals(paraula_exemple)
sense_consonants = treu_consonants(paraula_exemple)

print(f"Paraula original: {paraula_exemple}")
print(f"Sense vocals: {sense_vocals}")
print(f"Sense consonants: {sense_consonants}")

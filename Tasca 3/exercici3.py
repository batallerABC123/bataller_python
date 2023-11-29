print ("Oriol Torra")
print ("======================")
print ("Exercici 3.1:")
print ("Quin és el teu nom?")
a = input ()
print ("¡Hola", a,"!")
print ("======================")
print ("Exercici 3.2:")
#print ("Apartats 1 i 2:")
var_juan = 3
var_maria = 5
var_adan = 6
print ("Apartat 3:")
print (var_juan,",", var_maria,",", var_adan)
#print ("Apartat 4:")
total_manzanas = (var_juan + var_maria + var_adan)
print ("Apartat 5:")
print (total_manzanas)
print ("Apartat 6:")
var_juan_maria = (var_juan + var_maria)
var_adan_negatiu = -6
print (var_juan_maria * var_adan_negatiu)
print ("======================")
print ("Exercici 3.3:")
kilometers = 1.61
miles = 1
miles_to_kilometers = miles * 1.61
kilometers_to_miles = kilometers / 1.61 
print ("Apartat 1:")
print (miles, "millas son", round(miles_to_kilometers, 2), "kilómetros")
print (kilometers, "kilómetros son", round(kilometers_to_miles, 2), "millas")
print ("Apartat 2:")
kilometers = int(input("Kilometros a millas "))
miles = int(input("Millas a kilometros "))
miles_to_kilometers = miles * 1.61
kilometers_to_miles = kilometers / 1.61 
print (miles, "millas son", round(miles_to_kilometers, 2), "kilómetros")
print (kilometers, "kilómetros son", round(kilometers_to_miles, 2), "millas")
print ("======================")
print ("Exercici 3.4:")
x = 5
x = float(x)
y = 3 * x**3 - 2 * x**2 + 3 * x -1
print ("y =", y)
print ("======================")
print ("Exercici 3.5:")
num_horas = int(input("Horas trabajadas "))
precio_hora = int(input("Coste por hora "))
precio_total = num_horas * precio_hora
print ("He trabajado:", num_horas, "El precio por hora és:", precio_hora, "Por tanto la paga és de:", precio_total)
print ("======================")
print ("Exercici 3.6:")
num_usuari = int(input("Tria un número: ")) 
suma = (num_usuari * (num_usuari + 1)) / 2
print ("El resultat de (num_usuari * (num_usuari + 1)) / 2 és: ", suma)
print ("======================")
print ("Exercici 3.7:")
pes = int(input("El teu pes en Kg és: "))
altura = float(input("La teva altura en M és: "))
imc = pes / (altura **2)
print ("Tu índice de masa corporal es {:.2f}".format(imc))
print ("======================")
print ("Exercici 3.8:")
#L'interés d'aquesta inversió és compost
cantitat_invertir = float(input("La quantitat a invertir és de: "))
interes_anual = int(input("L'interés anual en % és de: "))
num_anys = int(input("El número d'anys és de: "))
interes_decimal =interes_anual /100
capital = cantitat_invertir * (1 + interes_decimal)**num_anys
print ("El capital obtingut és {:.2f}".format(capital))
print ("======================")
print ("Exercici 3.9:")
primer_byte = int(input("Primer byte "))
segon_byte = int(input("Segon byte "))
tercer_byte = int(input("Tercer byte "))
quart_byte = int(input("Quart byte "))
print (primer_byte, segon_byte, tercer_byte, quart_byte, sep=".")
print ("======================")
print ("Exercici 3.10:")
print ("Part 1:")
hour =int(input("Hora de inicio (horas): "))
mins =int(input("Minuto de inicio (minutos): "))
dura =int(input("Duración del evento (minutos): "))
hour_dura = dura // 60
mins_dura = dura % 60
final_hour = (hour + hour_dura + (mins + mins_dura) // 60) % 24
final_min = (mins + mins_dura) % 60
print(f"El evento a comenzando a las {hour:02d}:{mins:02d} y a durado {dura} minutos, por tanto terminará a las {final_hour:02d}:{final_min:02d}")
print ("Part 2:")
day =int(input("Día (días): "))
hour =int(input("Hora de inicio (horas): "))
mins =int(input("Minuto de inicio (minutos): "))
dura =int(input("Duración del evento (minutos): "))
hour_dura = dura // 60
mins_dura = dura % 60
final_hour = (hour + hour_dura + (mins + mins_dura) // 60) % 24
final_min = (mins + mins_dura) % 60
final_day = day + (hour + hour_dura) // 24
print(f"El evento a comenzando el dia {day}/{final_day} a las {hour:02d}:{mins:02d} y a durado {dura} minutos, por tanto terminará el dia {final_day} a las {final_hour:02d}:{final_min:02d}")
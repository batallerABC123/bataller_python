number1 = int(input("Ingresa el primera número:"))
number2 = int(input("Ingresa el segon número:"))
number3 = int(input("Ingresa el tercer número:"))


largest_number = number1
if number2 > largest_number:
    largest_number=number2
    
if number3 > largest_number:
    largest_number = number3
    
print("El número más grande es", largest_number)
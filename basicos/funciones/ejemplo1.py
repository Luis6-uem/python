def saludo():
	print(f"hola mundo")

saludo()

def saludar(nombre,edad):
	print(f"hola Mr. {nombre} que tienes {edad} años")

saludar("Marco", 25)

def saludoPideNombre():
	nombre=input("dame un nombre ")
	print(f"Hola {nombre}")

saludoPideNombre()

def suma(num1,num2):
	total = num1+num2
	return total

suma(3,5)
suma(56,34)

def inicio():
	saludo()
	saludar("Luis", 20)
	saludoPideNombre()
	suma(3,5)
	suma(56,34)


def saludo():
	print(f"hola mundo")


def saludar(nombre,edad):
	print(f"hola Mr. {nombre} que tienes {edad} años")


def saludoPideNombre():
	nombre=input("dame un nombre ")
	print(f"Hola {nombre}")

def suma(num1,num2):
	total = num1+num2
	return total



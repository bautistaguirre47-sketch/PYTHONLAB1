class Cliente:
    def __init__(self, nombre, dni, actividad, membresia):
        self.nombre = nombre
        self.dni = dni
        self.actividad = actividad
        self.membresia = membresia

    def mostrar_resumen(self):       
     print("Bienvenido a GymLab")
nombre = input ("¿cual es tu nombre? ")
print(f"¡mucho gusto, {nombre}!")
print("Para comenzar necesito que me dejes tus datos")
dni = input ("DNI: ")
actividad = input ("¿A qué actividad te gustaria anotarte? ")
membresia = input ("¿Cuántos días a la semana te gustaria venir? ")
print("¡Genial, comencemos!")
print(f"Ficha creada: {nombre} - DNI: {dni} - Actividad: {actividad} ({membresia} días).")
nuevo_cliente = Cliente(nombre, dni, actividad, membresia)
nuevo_cliente.mostrar_resumen()
while True:
 print("Bienvenido a GymLab")
 nombre = input("¿cual es tu nombre? ")
 print(f"¡mucho gusto, {nombre}!")
 print("Para comenzar necesito que me dejes tus datos")
 dni = input ("DNI: ")
 actividad = input("¿A qué actividad te gustaria anotarte? ")
 membresia = input("¿Cuántos días a la semana te gustaria venir? ")
 print("¡Genial, comencemos!")
 continuar = input("\n¿Quieres registrar a otro cliente? (si/no): ").lower()
 if continuar == "no":
    break

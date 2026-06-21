class Cliente:
    def __init__(self, nombre, dni, actividad, membresia, cuota):
        self.nombre = nombre
        self.dni = dni
        self.actividad = actividad
        self.membresia = membresia
        self.cuota = cuota

    def mostrar_resumen(self):       
        print("FICHA DE REGISTRO")
        print(f"Nombre: {self.nombre}")
        print(f"DNI: {self.dni}")
        print(f"Actividad: {self.actividad}")
        print(f"Membresía: {self.membresia}")
        print(f"cuota: {self.cuota}")
        

while True:
    print("Bienvenido a GymLab")
    nombre = input("¿Cuál es tu nombre? ")
    print(f"¡Mucho gusto, {nombre}!")
    
    print("Para comenzar necesito que me dejes tus datos")
    dni = input("DNI: ")
    print("En GymLab contamos con 2 actividades diferentes: Muscalcion y Spinning")
    actividad = input("¿A qué actividad te gustaría anotarte? ")
    print("contamos con diferentes membresias:")
    print("ESTANDAR (3-4 dias)")
    print("VIP (6 dias)") 
    membresia = input("¿Que membresia te gustaria escoger? ").lower()
    if membresia == "estandar":
       print("el valor es de 15.000")
       cuota = "15.000"
    if membresia == "vip":
       print("el valor es de 30.000")
       cuota = "30.000"
    else:
        print("no existe esa membresia")
    

    nuevo_cliente = Cliente(nombre, dni, actividad, membresia, cuota)
    
    
    nuevo_cliente.mostrar_resumen()
    
    continuar = input("¿Quieres registrar a otro cliente? (si/no): ").lower()
    if continuar == "si":
        print("preparando siguiente formulario")
    if continuar == "no":
        print("¡Gracias por registrarte en GymLab!")
        break
    else:
        print("opcion no valida")

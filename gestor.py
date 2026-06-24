class Socio:
    def __init__(self, dni, nombre, membresia):
        self.dni = dni
        self.nombre = nombre
        self.membresia = membresia  # Objeto de tipo Membresia
        self.cuota_pagada = False
        self.actividades = []

    def pagar_cuota(self):
        self.cuota_pagada = True

    def inscribirse(self, actividad):
        self.actividades.append(actividad)


class Actividad:
    def __init__(self, nombre):
        self.nombre = nombre
        self.inscriptos = []
        self.asistencias = 0

    def agregar_socio(self, socio):
        self.inscriptos.append(socio)

    def registrar_asistencia(self):
        self.asistencias += 1


class Membresia:
    def __init__(self, tipo, precio):
        self.tipo = tipo
        self.precio = precio


class Gimnasio:
    def __init__(self):
        self.socios = []
        self.actividades = {}

    def agregar_actividad(self, actividad):
        clave = actividad.nombre.lower().replace("ó", "o")
        self.actividades[clave] = actividad

    def registrar_socio(self, socio):
        self.socios.append(socio)

    def buscar_socio(self, dni):
        for socio in self.socios:
            if socio.dni == dni:
                return socio
        return None

    def mostrar_estadisticas(self):
        total_socios = len(self.socios)
        cuotas_pagadas = 0
        for socio in self.socios:
            if socio.cuota_pagada:
                cuotas_pagadas += 1

        print("\n=========================================")
        print("         ESTADÍSTICAS GENERALES          ")
        print("=========================================")
        print(f"Total socios registrados: {total_socios}")
        print(f"Cuotas pagadas:           {cuotas_pagadas}")
        print("-----------------------------------------")
        for act in self.actividades.values():
            print(f"Actividad {act.nombre}: {len(act.inscriptos)} inscriptos | {act.asistencias} asistencias")
        print("=========================================")


# =====================================================================
# FUNCIONES DE VALIDACIÓN Y ENTRADA DE DATOS
# =====================================================================

def solicitar_texto_no_vacio(mensaje_usuario):
    while True:
        texto = input(mensaje_usuario).strip()
        if len(texto) > 0 and texto.replace(" ", "").isalpha():
            return texto.title()
        print("Error: El campo no puede estar vacío y solo debe contener letras.")


def solicitar_dni(gym_sistema, verificar_duplicado=True):
    while True:
        try:
            dni_input = input("DNI (sin puntos ni espacios): ").strip()
            if not dni_input.isdigit():
                raise ValueError("El DNI debe contener solo números.")
            
            if verificar_duplicado and gym_sistema.buscar_socio(dni_input):
                print("Error: Ya existe un socio registrado con ese DNI.")
                continue
                
            return dni_input
        except ValueError as e:
            print(f"Error de ingreso: {e} Intente nuevamente.")


def solicitar_actividad():
    while True:
        print("\nActividades disponibles en GymLab:")
        print("  - Musculacion")
        print("  - Spinning")
        eleccion = input("¿A qué actividad te gustaría anotarte? ").strip().lower()
        eleccion_normalizada = eleccion.replace("ó", "o")
        
        if eleccion_normalizada in ["musculacion", "spinning"]:
            return eleccion_normalizada
        print("Error: Actividad no válida. Elija 'Musculacion' o 'Spinning'.")


def solicitar_membresia():
    while True:
        print("\nMembresías disponibles:")
        print("  - ESTANDAR (3-4 días) -> $15.000")
        print("  - VIP (6 días)       -> $30.000")
        eleccion = input("¿Qué membresía te gustaría escoger? ").strip().lower()
        
        if eleccion == "estandar":
            return Membresia("Estándar", 15000)
        elif eleccion == "vip":
            return Membresia("VIP", 30000)
        print("Error: Opción no válida. Escriba 'estandar' o 'vip'.")


# =====================================================================
# LOGICA INTERACTIVA DEL MENÚ (Modularización)
# =====================================================================

def registrar_socio_interactivo(gym):
    print("\n--- REGISTRO DE NUEVO SOCIO ---")
    nombre = solicitar_texto_no_vacio("¿Cuál es tu nombre? ")
    print(f"¡Mucho gusto, {nombre}!")
    
    dni = solicitar_dni(gym, verificar_duplicado=True)
    actividad_clave = solicitar_actividad()
    membresia_objeto = solicitar_membresia()

    nuevo_socio = Socio(dni, nombre, membresia_objeto)
    
    paga = input("¿Desea abonar la cuota ahora? (si/no): ").strip().lower()
    if paga == "si":
        nuevo_socio.pagar_cuota()

    gym.registrar_socio(nuevo_socio)
    
    obj_actividad = gym.actividades[actividad_clave]
    nuevo_socio.inscribirse(obj_actividad)
    obj_actividad.agregar_socio(nuevo_socio)

    print("\n=========================================")
    print("           SOCIO REGISTRADO              ")
    print("=========================================")
    print(f"Nombre:    {nuevo_socio.nombre}")
    print(f"DNI:       {nuevo_socio.dni}")
    print(f"Actividad: {obj_actividad.nombre}")
    print(f"Membresía: {nuevo_socio.membresia.tipo}")
    print(f"Estado:    {'PAGADO' if nuevo_socio.cuota_pagada else 'DEUDOR'}")
    print("=========================================")


def marcar_asistencia_interactivo(gym):
    print("\n--- REGISTRAR ASISTENCIA ---")
    if not gym.socios:
        print("No hay socios registrados en el sistema todavía.")
        return

    dni = solicitar_dni(gym, verificar_duplicado=False)
    socio = gym.buscar_socio(dni)

    if socio:
        print(f"\nSocio encontrado: {socio.nombre}")
        # Registrar asistencia en todas las actividades en las que está inscripto
        if socio.actividades:
            for actividad in socio.actividades:
                actividad.registrar_asistencia()
                print(f"¡Asistencia registrada con éxito en {actividad.nombre}!")
        else:
            print("Este socio no está inscripto a ninguna actividad.")
    else:
        print("Error: No se encontró ningún socio con ese DNI.")


def pagar_cuota_interactivo(gym):
    print("\n--- REGISTRAR PAGO DE CUOTA ---")
    if not gym.socios:
        print("No hay socios registrados en el sistema todavía.")
        return

    dni = solicitar_dni(gym, verificar_duplicado=False)
    socio = gym.buscar_socio(dni)

    if socio:
        if socio.cuota_pagada:
            print(f"El socio {socio.nombre} ya tiene su cuota al día.")
        else:
            socio.pagar_cuota()
            print(f"¡Pago registrado! El socio {socio.nombre} ahora está al día.")
    else:
        print("Error: No se encontró ningún socio con ese DNI.")


# =====================================================================
# CONTROLADOR PRINCIPAL
# =====================================================================

def ejecutar_sistema():
    gym = Gimnasio()
    gym.agregar_activity = gym.agregar_actividad(Actividad("Musculación"))
    gym.agregar_actividad(Actividad("Spinning"))

    while True:
        print("\n=========================================")
        print("       SISTEMA DE GESTIÓN GYMLAB         ")
        print("=========================================")
        print("1. Registrar nuevo socio")
        print("2. Registrar asistencia")
        print("3. Registrar pago de cuota")
        print("4. Ver estadísticas generales")
        print("5. Salir del sistema")
        print("=========================================")
        
        opcion = input("Seleccione una opción (1-5): ").strip()

        if opcion == "1":
            registrar_socio_interactivo(gym)
        elif opcion == "2":
            marcar_asistencia_interactivo(gym)
        elif opcion == "3":
            pagar_cuota_interactivo(gym)
        elif opcion == "4":
            gym.mostrar_estadisticas()
        elif opcion == "5":
            print("\n¡Gracias por utilizar el sistema de GymLab! Cerrando sesión...")
            break
        else:
            print("Error: Opción no válida. Por favor, ingrese un número del 1 al 5.")


if __name__ == "__main__":
    ejecutar_sistema()

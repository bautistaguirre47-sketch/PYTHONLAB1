# ==========================
# CLASES
# ==========================

class Socio:
    def __init__(self, dni, nombre, membresia):
        self.dni = dni
        self.nombre = nombre
        self.membresia = membresia
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


# ==========================
# SISTEMA GIMNASIO
# ==========================

class Gimnasio:
    def __init__(self):
        self.socios = []
        self.actividades = []

    # Registrar socio
    def registrar_socio(self, socio):
        self.socios.append(socio)

    # Agregar actividad
    def agregar_actividad(self, actividad):
        self.actividades.append(actividad)

    # Buscar socio
    def buscar_socio(self, dni):
        for socio in self.socios:
            if socio.dni == dni:
                return socio
        return None

    # Estadísticas
    def mostrar_estadisticas(self):
        total_socios = len(self.socios)

        cuotas_pagadas = 0
        for socio in self.socios:
            if socio.cuota_pagada:
                cuotas_pagadas += 1

        print("\n===== ESTADÍSTICAS =====")
        print("Total socios:", total_socios)
        print("Cuotas pagadas:", cuotas_pagadas)

        for actividad in self.actividades:
            print(
                f"{actividad.nombre}: "
                f"{len(actividad.inscriptos)} inscriptos - "
                f"{actividad.asistencias} asistencias"
            )


# ==========================
# PROGRAMA PRINCIPAL
# ==========================

premium = Membresia("Premium", 30000)
basica = Membresia("Básica", 20000)

gym = Gimnasio()

# Crear actividades
musculacion = Actividad("Musculación")
spinning = Actividad("Spinning")

gym.agregar_actividad(musculacion)
gym.agregar_actividad(spinning)

# Registrar socios
s1 = Socio("40111222", "Juan Pérez", premium)
s2 = Socio("40555444", "Ana Gómez", basica)

gym.registrar_socio(s1)
gym.registrar_socio(s2)

# Pago de cuotas
s1.pagar_cuota()

# Inscripción a actividades
s1.inscribirse(musculacion)
musculacion.agregar_socio(s1)

s2.inscribirse(spinning)
spinning.agregar_socio(s2)

# Registrar asistencias
musculacion.registrar_asistencia()
musculacion.registrar_asistencia()
spinning.registrar_asistencia()

# Mostrar estadísticas
gym.mostrar_estadisticas()
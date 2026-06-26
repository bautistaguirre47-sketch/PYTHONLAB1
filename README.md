# GymLab — Sistema de Gestión de Gimnasio

> **Laboratorio N°1 — Algoritmos y Estructuras de Datos**  
> Ingeniería en Sistemas de Información · UTN — Facultad Regional

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## Descripción

**GymLab** es un sistema de gestión de gimnasio desarrollado en Python como trabajo práctico de laboratorio para la materia **Algoritmos y Estructuras de Datos** de la carrera **ISI (Ingeniería en Sistemas de Información)** en la **Universidad Tecnológica Nacional (UTN)**.

El proyecto simula el funcionamiento de un sistema de gestión real, permitiendo registrar socios, asignarles membresías y actividades, registrar asistencias, gestionar el pago de cuotas y visualizar estadísticas generales del gimnasio.

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## Objetivo del Laboratorio

Aplicar de forma progresiva los conceptos fundamentales de programación en Python, partiendo de scripts procedurales simples hasta llegar a un sistema estructurado con **Programación Orientada a Objetos (POO)**, validación de datos y modularización del código.

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## Estructura del Proyecto

```
PYTHONLAB1/
│
├── gestor_gimnasio.py    # Versión 1 — Entrada/salida básica (sin clases)
├── hola_mundo.py         # Versión 2 — Introducción a clases (clase Cliente)
├── p.py                  # Versión 3 — Evolución: cuotas, membresías y bucles
├── prueba.py             # Versión 4 — POO completa con datos de prueba
└── gestor.py             # Versión Final — Sistema interactivo completo
```

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## Evolución del Desarrollo

El proyecto documenta el proceso de aprendizaje iterativo a través de 5 versiones sucesivas:

| Archivo | Etapa | Conceptos Aplicados |
|---|---|---|
| `gestor_gimnasio.py` | Versión 1 | `input()`, `print()`, variables, strings |
| `hola_mundo.py` | Versión 2 | Clases, `__init__`, métodos, instancias |
| `p.py` | Versión 3 | Atributos adicionales, lógica condicional, bucle `while` |
| `prueba.py` | Versión 4 | POO completa: 4 clases, listas, relaciones entre objetos |
| `gestor.py` | Versión Final | Menú interactivo, validaciones, modularización, diccionarios |

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## Arquitectura del Sistema (Versión Final)

### Diagrama de Clases 

```
┌───────────────────┐         ┌──────────────────────┐
│      Socio        │◄────────│      Gimnasio         │
│─────────────────── │         │──────────────────────│
│ - dni             │         │ - socios: list        │
│ - nombre          │         │ - actividades: dict   │
│ - membresia       │         │──────────────────────│
│ - cuota_pagada    │         │ + registrar_socio()   │
│ - actividades     │         │ + agregar_actividad() │
│─────────────────── │         │ + buscar_socio()      │
│ + pagar_cuota()   │         │ + mostrar_estadisticas│
│ + inscribirse()   │         └──────────────────────┘
└───────────────────┘
        │                     ┌───────────────────────┐
        │ participa en        │       Actividad        │
        └────────────────────►│───────────────────────│
                              │ - nombre               │
                              │ - inscriptos: list     │
┌───────────────────┐         │ - asistencias: int     │
│    Membresia      │         │───────────────────────│
│─────────────────── │         │ + agregar_socio()     │
│ - tipo            │         │ + registrar_asistencia│
│ - precio          │         └───────────────────────┘
└───────────────────┘
```

### Clases Implementadas

**`Socio`**  
Representa a un miembro del gimnasio. Almacena sus datos personales, la membresía contratada, el estado de pago de la cuota y las actividades en las que está inscripto.

**`Actividad`**  
Modela una actividad ofrecida por el gimnasio (Musculación o Spinning). Lleva registro de los socios inscriptos y el total de asistencias.

**`Membresia`**  
Encapsula el tipo de membresía (Estándar o VIP) y su precio mensual.

**`Gimnasio`**  
Clase principal que actúa como contenedor del sistema. Gestiona la colección de socios y actividades, y expone las operaciones CRUD del negocio.

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## Funcionalidades

- **Registrar socios** — Alta de nuevos miembros con datos personales, membresía y actividad elegida.
- **Validación de datos** — Control de DNI duplicado, campos de texto vacíos, opciones no válidas.
- **Pago de cuota** — Registro del estado de pago mensual por socio.
- **Registro de asistencias** — Incremento del contador de asistencias por actividad.
- **Estadísticas generales** — Resumen de socios totales, cuotas pagadas e inscriptos por actividad.
- **Menú interactivo** — Interfaz de línea de comandos con navegación por opciones numeradas.

### Membresías disponibles

| Tipo | Días por semana | Precio mensual |
|---|---|---|
| Estándar | 3 a 4 días | $15.000 |
| VIP | 6 días | $30.000 |

### Actividades disponibles

| Actividad |
|---|
| Musculación |
| Spinning |

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## Cómo Ejecutar

### Requisitos

- Python 3.x instalado ([descargar](https://www.python.org/downloads/))

### Pasos

```bash
# Clonar el repositorio
git clone https://github.com/bautistaguirre47-sketch/PYTHONLAB1.git
cd PYTHONLAB1

# Ejecutar
python gestor.py
```
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### Ejemplo de uso

```
=========================================
       SISTEMA DE GESTIÓN GYMLAB
=========================================
1. Registrar nuevo socio
2. Registrar asistencia
3. Registrar pago de cuota
4. Ver estadísticas generales
5. Salir del sistema
=========================================
Seleccione una opción (1-5):
```

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## Conceptos de la Materia Aplicados

- Programación Orientada a Objetos (clases, atributos, métodos, instancias)
- Modularización y separación de responsabilidades
- Estructuras de datos: listas y diccionarios
- Validación de entrada con manejo de excepciones (`try/except`)
- Flujo de control: bucles `while`, condicionales `if/elif/else`
- Funciones con parámetros y valores de retorno
- Uso de `f-strings` y formato de salida por consola

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## Autores

| Frettis Irazusta Andres  | 31048
| Mendez Thiago | 
| Noguera Juan Sebastian | 31658
| Aguirre Gonzalez Bautista | 30684

> **Materia:** Algoritmos y Estructuras de Datos  
> **Carrera:** Ingeniería en Sistemas de Información  
> **Institución:** Universidad Tecnológica Nacional (UTN)  
> **Año:** 2026

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## Licencia

Proyecto académico — uso exclusivo para fines educativos en el marco de la UTN ISI.

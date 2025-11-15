# Ejercicio 7 - Gestión de procesos. Herramientas de monitorización

**Autor:** Alejandro Épila  
**Asignatura:** Programación de servicios y procesos  
**Curso:** 2º DAM  
**Fecha:** Noviembre 2025

---

## 1. Introducción breve y contextualización

El ejercicio consiste en modelar mecánicas de un juego, como si el jugador fuera resolviendo problemas relacionados con mecánica de vehículos (cambio de aceite, frenos, diagnósticos, etc.).

Crear una clase específica para este concepto permite:

- Organizar mejor el código.

- Representar cada mecánica del juego con su propia información.

- Preparar la base para futuras ampliaciones: dificultad, recompensas, etc.

---

## 2. Desarrollo detallado y preciso

#### Clase ``Mecanica``

LA clase contiene:

- Un atributo para almacenar el nombre.

- Un método ``describir()`` que muestra la mecánica por pantalla.

---

## 3. Aplicación práctica

En este apartado se crean varias mecánicas y se utiliza el método ``describir()`` para mostrar sus características.

#### Ejemplo de uso

```
La mecanica seleccionada es: Cambio de aceite
La mecanica seleccionada es: Reparacion de discos de freno
La mecanica seleccionada es: Diagnostico del motor
```

#### ``mecanica.py``

```
class Mecanica:
  def __init__(self, nombre):
    self.nombre = nombre

  def describir(self):
    print(f"La mecanica seleccionada es: {self.nombre}")
```

#### ``main.py``

```
from mecanica import Mecanica

m1 = Mecanica("Cambio de aceite")
m2 = Mecanica("Reparacion de discos de freno")
m3 = Mecanica("Diagnostico del motor")

m1.describir()
m2.describir()
m3.describir()
```

---

## 4. Conclusión breve

Esta actividad refuerza la importancia de las clases y objetos dentro de la programación orientada a datos ,ya que sienta las bases del modelo de datos:

- La clase ``Mecanica`` es un modelo que más adelante podría guardarse en una base de datos.

- Estos objetos pueden convertirse en registros persistentes.

- En acceso a datos, normalmente se trabaja con clases que representan datos del mundo real.

Además, este ejercicio ayuda a comprender:

- Cómo estructurar la información en objetos.

- Cómo organizar el código para escalar el proyecto.

---

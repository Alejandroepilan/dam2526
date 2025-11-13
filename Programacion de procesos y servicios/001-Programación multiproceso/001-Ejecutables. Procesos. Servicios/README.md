# Ejercicio 1 – Ejecutables. Procesos. Servicios

**Autor:** Alejandro Épila  
**Asignatura:** Programación de procesos y servicios  
**Curso:** 2º DAM  
**Fecha:** Noviembre 2025

---

## 1. Introducción breve y contextualización

En este ejercicio se parte de un script en Python que contiene la variable ``numero``, la cual almacena un valor decimal.
A través de un bucle ````for``, esta variable se multiplica por una constante un número muy elevado de veces, lo que provoca que el proceso consuma mucho tiempo de ejecución.

El motivo es que el script se ejecuta de forma secuencial, utilizando únicamente un núcleo del procesador, por lo que no se aprovechan los recursos del sistema de forma eficiente.

---

## 2. Desarrollo detallado y preciso

Para cumplir con los requisitos del ejercicio, se realizaron las siguientes modificaciones:

1. Se creó una variable llamada ``multiplicador`` que almacena el valor constante ``1.0000000000654``.

2. Se añadió una condición dentro del bucle para que la multiplicación solo se realice cuando el contador ``i`` sea múltiplo de 10.000 (``if i % 10000 == 0:``).

---

## 3. Aplicación práctica

Para probar el funcionamiento del script, se realizaron distintas ejecuciones variando el rango y el valor del multiplicador:

### 1. Menos iteraciones

  ```
  for i in range(0, 100000):
    if i % 10000 == 0:
      numero *= multiplicador
      print(f"Iteración {i} -> numero = {numero}")
  ```
Se observa que el valor de ``numero`` cambia progresivamente en las iteraciones 0, 10000, 20000, 30000, etc.

### 2. Cambiar el multiplicador

  ```
  multiplicador = 1.0001
  ```
Al aumentar el multiplicador, el crecimiento de ``numero`` se acelera considerablemente. los cálculos repetidos con decimales pequeños pueden generar variaciones grandes tras muchas iteraciones.

#### Errores comunes

- No declarar la variable ``multiplicador`` y usar el número directamente (disminuye la claridad del código).

- Probar con un rango demasiado grande sin reducirlo para testear (puede tardar mucho en ejecutarse).

---

## 4. Conclusión breve

Este ejercicio permite comprender cómo un proceso secuencial puede convertirse en una carga de cálculo importante cuando se realizan operaciones repetitivas sobre una variable.

---

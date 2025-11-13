# Ejercicio 3 – Hilos

**Autor:** Alejandro Épila  
**Asignatura:** Programación de procesos y servicios  
**Curso:** 2º DAM  
**Fecha:** Noviembre 2025

---

## 1. Introducción breve y contextualización

En un taller mecánico es clave registrar de forma fiable los datos del vehículo (marca, modelo, año) y su historial de reparaciones y mantenimientos.
La propuesta es diseñar una clase ``Vehiculo`` que encapsule esa información y exponga métodos claros para:

- Establecer/obtener atributos.

- Añadir entradas al historial (reparaciones/mantenimientos).

- Mostrar los detalles del vehículo.

---

## 2. Desarrollo detallado y preciso

#### Requisitos cubiertos:

- Atributos privados (encapsulación con ``__``).

- Métodos públicos ``set_*/get_*``.

- Métodos para añadir al historial y mostrar detalles.

- Sin listas/diccionarios/recorridos: el historial es un ``str`` con saltos de línea.

---

## 3. Aplicación práctica

#### Ejemplo de uso
```
from vehiculo import Vehiculo

coche = Vehiculo("BMW", "E36 325i", 1992)

coche.add_reparacion("Cambio bomba de agua", fecha="2025-11-10", coste=220.0)
coche.add_mantenimiento("Cambio de aceite 5W40", fecha="2025-11-12", km=245000)

print(coche.mostrar_detalles())
```

#### Que verás en pantalla
```
Marca: BMW
Modelo: E36 325i
Año: 1992
Historial:
[REPARACION] 2025-11-10 – Cambio bomba de agua – coste: 220.00€
[MANTENIMIENTO] 2025-11-12 – Cambio de aceite 5W40 – km: 245000
```

---

## 4. Conclusión breve

La clase ``Vehiculo`` muestra cómo encapsular atributos privados y controlarla mediante métodos públicos.

La decisión de usar un historial como cadena cumple la restricción (sin listas/diccionarios/bucles).

---

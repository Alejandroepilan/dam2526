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

#### ``vehiculo.py``

```
from datetime import date

class Vehiculo:
  def __init__(self, marca: str = "", modelo: str = "", anio_fabricacion: int = 0):
    self.__marca = marca
    self.__modelo = modelo
    self.__anio_fabricacion = anio_fabricacion
    self.__historial = "" # Historial como texto plano

  def set_marca(self, marca: str) -> None:
    self.__marca = marca

  def get_marca(self) -> str:
    return self.__marca

  def set_modelo(self, modelo: str) -> None:
    self.__modelo = modelo

  def get_modelo(self) -> str:
    return self.__modelo

  def set_anio_fabricacion(self, anio: int) -> None:
    self.__anio_fabricacion = anio

  def get_anio_fabricacion(self) -> int:
    return self.__anio_fabricacion

  def get_historial(self) -> str:
    return self.__historial

  def add_reparacion(self, concepto: str, fecha: str = None, coste: float = None) -> None:
    # Añade una reparacion al historial como linea de texto.
    # - fecha: 'YYYY-MM-DD' (opcional). Si no se pasa, usa hoy.
    # - coste: numero opcional.
    f = fecha if fecha else str(date.today())
    linea = f"[REPARACION] {f} – {concepto}"
    if coste is not None:
      linea += f" – coste: {coste:.2f}€"
    self.__historial += linea + "\n"

  def add_mantenimiento(self, concepto: str, fecha: str = None, km: int = None) -> None:
    # Añade un mantenimiento al historial como linea de texto.
    # - fecha: 'YYYY-MM-DD' (opcional). Si no se pasa, usa hoy.
    # - km: kilometraje opcional.
    f = fecha if fecha else str(date.today())
    linea = f"[MANTENIMIENTO] {f} – {concepto}"
    if km is not None:
      linea += f" – km: {km}"
    self.__historial += linea + "\n"

  def mostrar_detalles(self) -> str:
    #Devuelve un texto con todos los detalles.
    detalles = (
      f"Marca: {self.__marca}\n"
      f"Modelo: {self.__modelo}\n"
      f"Año: {self.__anio_fabricacion}\n"
      "Historial:\n"
    )
    # Si no hay historial, lo indicamos.
    if self.__historial == "":
      return detalles + "(sin entradas)\n"
    return detalles + self.__historial

```

---

## 4. Conclusión breve

La clase ``Vehiculo`` muestra cómo encapsular atributos privados y controlarla mediante métodos públicos.

La decisión de usar un historial como cadena cumple la restricción (sin listas/diccionarios/bucles).

---

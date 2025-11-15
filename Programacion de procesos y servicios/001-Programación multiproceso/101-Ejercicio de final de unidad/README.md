# Ejercicio 101 – Ejercicio de final de unidad

**Autor:** Alejandro Épila  
**Asignatura:** Programación de procesos y servicios  
**Curso:** 2º DAM  
**Fecha:** Noviembre 2025

---

## 1. Introducción breve y contextualización

La mayoría de ordenadores actuales tienen varios núcleos, pero muchos programas no los aprovechan. La programación multiproceso permite repartir tareas pesadas entre varios núcleos y reducir el tiempo de cálculo.

En este proyecto desarrollo una aplicación en Python que simula el trabajo de un ingeniero mecánico: calcula en paralelo el esfuerzo computacional de varias piezas con distintas complejidades.

El programa lee una lista de piezas, ejecuta una simulación numérica para cada una, reparte el trabajo entre varios procesos y compara el tiempo secuencial frente al paralelo, mostrando la mejora obtenida.

---

## 2. Desarrollo detallado y preciso

Puntos clave técnicos:

- Uso de ``multiprocessing.Pool`` para repartir las simulaciones entre múltiples procesos.

- Uso de ``cpu_count()`` para detectar automáticamente el número de núcleos disponibles.

- Comparación clara entre ejecución secuencial y ejecución en paralelo.

---

## 3. Aplicación práctica

#### Cómo ejecutar la aplicación

Desde la terminal, situándote en la carpeta del archivo:

```
py .\ejercicio.py
```

#### Ejemplo de salida

```
Simulación de piezas mecánicas con programación multiproceso

=== Ejecución secuencial ===
Pieza: Biela           | Resultado simulación: 1439999839
Pieza: Cigüeñal        | Resultado simulación: 1391999755
Pieza: Pistón          | Resultado simulación: 1296000001
Pieza: Disco de freno  | Resultado simulación: 767999811
Pieza: Válvula         | Resultado simulación: 1439999839

Tiempo total (secuencial): 6.88 segundos

=== Ejecución en paralelo (multiproceso) ===
Usando 12 procesos en paralelo.

Pieza: Biela           | Resultado simulación: 1439999839
Pieza: Cigüeñal        | Resultado simulación: 1391999755
Pieza: Pistón          | Resultado simulación: 1296000001
Pieza: Disco de freno  | Resultado simulación: 767999811
Pieza: Válvula         | Resultado simulación: 1439999839

Tiempo total (paralelo): 2.09 segundos

=== Comparativa final ===
Tiempo secuencial: 6.88 s
Tiempo paralelo:  2.09 s
Factor de mejora aproximado: x3.29
```

#### ``ejercicio.py``

```
import time
from multiprocessing import Pool, cpu_count


def simular_pieza(args):
    """
    Simula el cálculo pesado para una pieza mecánica.
    En un caso real podría ser una simulación física.
    Aquí usamos una operación numérica costosa como ejemplo.
    """
    nombre_pieza, complejidad = args

    acumulador = 0
    # Bucle "pesado" para simular carga de CPU
    for i in range(complejidad):
        acumulador += (i * i) % 97  # operación tonta pero costosa

    # Devolvemos el resultado junto con el nombre de la pieza
    return nombre_pieza, acumulador


def ejecutar_secuencial(piezas):
    print("=== Ejecución secuencial ===")
    inicio = time.time()

    resultados = []
    for pieza in piezas:
        resultado = simular_pieza(pieza)
        resultados.append(resultado)

    fin = time.time()
    tiempo_total = fin - inicio

    for nombre, valor in resultados:
        print(f"Pieza: {nombre:15s} | Resultado simulación: {valor}")

    print(f"\nTiempo total (secuencial): {tiempo_total:.2f} segundos\n")
    return tiempo_total


def ejecutar_en_paralelo(piezas):
    print("=== Ejecución en paralelo (multiproceso) ===")
    inicio = time.time()

    # Número de procesos = núcleos disponibles
    num_procesos = cpu_count()
    print(f"Usando {num_procesos} procesos en paralelo.\n")

    with Pool(processes=num_procesos) as pool:
        resultados = pool.map(simular_pieza, piezas)

    fin = time.time()
    tiempo_total = fin - inicio

    for nombre, valor in resultados:
        print(f"Pieza: {nombre:15s} | Resultado simulación: {valor}")

    print(f"\nTiempo total (paralelo): {tiempo_total:.2f} segundos\n")
    return tiempo_total


def main():
    # Lista de piezas mecánicas (nombre, complejidad)
    # Complejidad controla las iteraciones: cuanto más grande, más tarda
    piezas = [
        ("Biela", 300_000_00),
        ("Cigüeñal", 290_000_00),
        ("Pistón", 270_000_00),
        ("Disco de freno", 160_000_00),
        ("Válvula", 300_000_00),
    ]

    print("Simulación de piezas mecánicas con programación multiproceso\n")

    # 1) Modo secuencial
    tiempo_secuencial = ejecutar_secuencial(piezas)

    # 2) Modo paralelo
    tiempo_paralelo = ejecutar_en_paralelo(piezas)

    # 3) Comparativa
    if tiempo_paralelo > 0:
        mejora = tiempo_secuencial / tiempo_paralelo
    else:
        mejora = 0

    print("=== Comparativa final ===")
    print(f"Tiempo secuencial: {tiempo_secuencial:.2f} s")
    print(f"Tiempo paralelo:  {tiempo_paralelo:.2f} s")
    print(f"Factor de mejora aproximado: x{mejora:.2f}")


if __name__ == "__main__":
    main()
```

---

## 4. Conclusión breve

Con este proyecto he aplicado de forma práctica los conceptos de programación multiproceso:

- He diseñado una aplicación que simula un caso de uso real, un profesional de la mecánica que necesita ejecutar muchos cálculos pesados sobre diferentes piezas.

- He utilizado múltiples núcleos de CPU mediante ``multiprocessing.Pool``, demostrando cómo repartir trabajo en paralelo.

- He comparado tiempos entre ejecución secuencial y en paralelo, viendo una mejora clara de rendimiento.

La idea clave que me llevo de la unidad es que, cuando tengo muchas tareas independientes y pesadas, puedo diseñar una solución que aproveche todos los núcleos del procesador para reducir drásticamente el tiempo de espera.

---

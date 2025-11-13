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


---

## 4. Conclusión breve

Con este proyecto he aplicado de forma práctica los conceptos de programación multiproceso:

- He diseñado una aplicación que simula un caso de uso real, un profesional de la mecánica que necesita ejecutar muchos cálculos pesados sobre diferentes piezas.

- He utilizado múltiples núcleos de CPU mediante ``multiprocessing.Pool``, demostrando cómo repartir trabajo en paralelo.

- He comparado tiempos entre ejecución secuencial y en paralelo, viendo una mejora clara de rendimiento.

La idea clave que me llevo de la unidad es que, cuando tengo muchas tareas independientes y pesadas, puedo diseñar una solución que aproveche todos los núcleos del procesador para reducir drásticamente el tiempo de espera.

---

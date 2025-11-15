# Examen final

**Autor:** Alejandro Épila  
**Asignatura:** Programación de procesos y servicios  
**Curso:** 2º DAM  
**Fecha:** Noviembre 2025

---

## 1. Introducción breve y contextualización

- Actualmente todavía hay muchos programas que se ejecutan de forma secuencial, sobretodo los mas atiguos ya que las CPU antiguamente solo contaban con 2 núcleos. Ahora mismo hasta el portátil mas básico tiene 4 núcleos y esto se puede aprovechar para poder correr partes de un programa en diferentes núcleos y de esta forma poder distribiur la carga del programa y que se ejecute mas rápidamente.

- El objetivo de este ejercicio es realizar una comparación entre el tiempo que tarda en ejecutarse este programa en modo secuencial contra a usar todos los núcleos disponibles del sistema en el que se está ejecutando.

- En este caso es un programa desarrollado en Python que simula el trabajo de un ingeniero mecánico. Simplemente realiza un gran número de operaciones matemáticas para dar carga a la CPU, es un caso real estas podrían ser una simulación física de componentes mecánicos.

---

## 2. Desarrollo detallado y preciso

### Importaciones

- `time`: trae el módulo `time`, que se usa para medir cuánto tiempo tarda en ejecutarse cada función del prigrama.
- `multiprocessing`:
  - `Pool`: sirve para crear un grupo de procesos que trabajan en paralelo en los distintos núcelos.
  - `cpu_count()`: devuelve cuántos núcleos tiene la CPU donde se está ejecutando el programa. Así este puede saber cuantos puede utilizar.

### Funciones principales del programa

#### 1. `simular_pieza(args)`

- Definimos las variables `nombre_pieza` y `complejidad` como argumentos que le pasamos a la función al ejecutarla. También definimos la variable `acumulador` que es igual a `0`.
- Después simplemente añadimos un bucle `for` el cuál realiza el numero de vueltas indicado en cada pieza del array `piezas`. Dentro de este se calcula `i` al cuadrado y luego se saca el resto de dividirlo enrte 97 (`% 97`). Y este valor se va sumando a `acumulador`.
- Esta es una operación muy aleatoria que simple hace que le de carga a la CPU.
- Por último se devuelve el resultado de cada operación junto al nombre de esa pieza.

#### 2. `ejecutar_secuencial(piezas)`

- Al iniciar la función se muestra por consola el título `=== Ejecución secuencial ===` y seguidamente se inicia un contador en la variable `inicio`.
- Ahora declaramos el array `resultados` y empezamos un bucle `for` según el numero de piezas en la variable `piezas`. Dentro de este guardamos en la variable `resultado` lo que nos devuelve la función `simular_pieza` al ejecutarla con una de las piezas y el contenido de `resultado` lo añadimos al array `resultados` con un `append`. Esto básicamente hace que se simule cada pieza una por una y se guarden todos los resultados de estas en el array `resultados`.
- Seguidamente declaramos la funcion `fin` donde guardamos el tiempo actual, para despues declarar la funcion `timpo_total` que es la resta de `inicio` menos `fin` y asi obtener el tiempo total que ha tardado en ejecutarse la función.
- Luego iniciamos otro bucle `for` para mostrar el nombre de cada pieza con una separacion de 15 carácteres para asi que todas las lineas de separación queden a la misma anchura. Después del nombre mostramos el resultado de la simulación.
- Y por último mostramos y devolvemos el tiempo total en segundos.

#### 3. `ejecutar_en_paralelo(piezas)`

- Igual que en la anterior función mostramos por consola el título e iniciamos el contador.
- Ahora guardamos en la variable `num_procesos` el resultado de la función `cpu_count()` que nos devuelve el número de núcleos que hay en la máquina donde se ha ejecutado el programa y los mostramos por consola.
- Despues creamos el `Pool` con el número de núcelos que hay en la variable `num_procesos` y añadimos al array `resultados` la ejecución de la funcion `simular_pieza` de todas las `piezas` que mostrará los resultados de las diferentes simulaciones.
- Seguidamente declaramos `fin` nuevamente para calcular el `tiempo_total` y mostrarlo por consola, justo despues de volver también a mostrar los nombres y resultados de cada pieza.

#### 4. `main()`

- Para empezar declaramos el array `piezas` con los nombres y las complejidades de los cálculos de cada una. Este número simplemente controla las iteraciones del bucle, asi que cuanto mas grande sea el número mas pesada será la carga de trabajo para la CPU.
- Seguidamente mostramos por consola el título principal de la aplicación y ejecutamos el modo secuencial y en paralelo, guardando en `tiempo_secuencial` y `tiempo_paralelo` el tiempo total de ejecución de cada función respectivamente.
- DEspues realizamos una pequeña division `mejora = tiempo_secuencial / tiempo_paralelo` para así poder ver el factor de mejora aproximadamente.
- Por último mostramos la comparativa por consola, con el tiempo secuencial, el tiempo en paralelo y la mejora.

---

## 3. Aplicación práctica

### Bloques del código

#### 1. Importaciones

- Añadimos al programa los módulos necesarios, en este caso `time` y `multiprocessing`.

```
import time
from multiprocessing import Pool, cpu_count
```

#### 2. Función `simular_pieza(args)`

- Función para realizar el cálculo de las piezas, una simple operación matemática para simular carga de trabajo al CPU.

```
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
```

#### 3. Función `ejecutar_secuencial(piezas)`

- Función para ejecutar de forma secuencial el cálculo de las piezas, es decir, uno detrás de otro.

```
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
```

#### 4. Función `ejecutar_en_paralelo(piezas)`

- Función para ejecutar en paralelo el cálculo de las piezas distribuyendolo entre los diferentes núcelos del sistema.

```
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
```

#### 5. Función `main()`

- Función principal de la aplicación, declara las piezas con sus nombres y complejidades. Ejecuta ambos modos (secuencial y en paralelo) y compara la mejora de tiempo entre estos.

```
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
```

### Errores comunes

- Un error bastante común podría ser no calcular bien todos los núcelos disponibles para la ejecución en paralelo utilizando la función `cpu_count()` y simplemente poner un número fijo en `num_procesos`.

---

## 4. Conclusión breve

- La aplicación aunque sea una simulación, puede llegar a ser un caso real de un ingeniero de mecánica que necesite ejecutar muchos cálculos pesados sobre las físicas de diferentes piezas.

- Gracias a este proyecto he podido observar la gran diferencia que existe entre ejecutar un programa de forma secuencial contra a ejecutarlo en paralelo. Sin duda cuando hay una gran carga de trabajo para la CPU, es muchísimo más eficiente distribuir dicha carga entre todos los núcelos disponibles del sistema.

---

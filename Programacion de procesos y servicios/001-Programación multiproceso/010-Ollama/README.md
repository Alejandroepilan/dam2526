# Ejercicio 10 – Ollama

**Autor:** Alejandro Épila  
**Asignatura:** Programación de procesos y servicios  
**Curso:** 2º DAM  
**Fecha:** Noviembre 2025

---

## 1. Introducción breve y contextualización

En este ejercicio se desarrolla un script en Python que permite enviar preguntas en lenguaje natural sobre una base de datos a un modelo de lenguaje ejecutado en local mediante ``curl`` y la API de Ollama.

El script:

- Lee el esquema de la base de datos desde el archivo ``blog.sql``.

- Construye un contexto donde se describe la estructura de las tablas (``entradas`` y ``usuarios``).

- Combina ese contexto con la pregunta del usuario.

- Envía todo a un modelo de lenguaje mediante ``curl`` para que éste genere:

  - Una breve explicación.

  - Una consulta SQL que responda a la pregunta.

---

## 2. Desarrollo detallado y preciso

Este código sigue exactamente la filosofía del archivo de clase ``005-cargo blog.py``, adaptado al enunciado del ejercicio (nombre de la variable ``prompt_usuario``, carga del esquema, construcción del contexto y ejecución de ``curl``).

---

## 3. Aplicación práctica

#### Como ejecutar el script

1. Asegúrate de que en la misma carpeta tengas:

    - El esquema de la base de datos
    - El script Python
  
2. Asegúrate de que:

    - Ollama está arrancado
    - Tienes el modelo ``llama3:latest``

3. Ejecuta en CMD
  ```
  py .\ejercicio.py
  ```

#### Ejemplo de interacción

Entrada por consola:
```
Introduce el prompt: quiero listar las ultimas 10 entradas
```

Salida:
```
Breve explicaciÃ³n: La pregunta es obtener las Ãºltimas 10 entradas de la base de datos.

La consulta SQL es:

sql
SELECT *
FROM entradas
ORDER BY fecha DESC
LIMIT 10;


Esta consulta selecciona todos los campos (`*`) de la tabla `entradas`, ordena las entradas por la columna `fecha` en orden descendente (mÃ¡s recientes primero) y limita el resultado a las Ãºltimas 10 entradas.
```

---

## 4. Conclusión breve

Este tipo de automatización puede ser muy útil en programación, en lugar de escribir manualmente cada consulta SQL, puedes delegar parte del trabajo a un modelo que, conociendo el esquema de la base de datos, te proponga consultas ya casi listas para pegar en tu gestor de bases de datos o en tu código.


---

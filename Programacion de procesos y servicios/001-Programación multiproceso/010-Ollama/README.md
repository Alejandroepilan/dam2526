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

#### ``ejercicio.py``

```
import subprocess
import json
import os

SCHEMA_PATH = "blog.sql"
MAX_SCHEMA_CHARS = 200_000  # por si el .sql es enorme, evita pasarte de contexto

def cargar_schema_sql(path: str) -> str:
    if not os.path.exists(path):
        return ""
    with open(path, "r", encoding="utf-8", errors="ignore") as f:
        schema = f.read()
    if len(schema) > MAX_SCHEMA_CHARS:
        schema = schema[:MAX_SCHEMA_CHARS] + "\n-- [Truncado para no exceder el contexto]\n"
    return schema

# Pide el prompt dinámicamente (o reemplázalo por una variable)
prompt_usuario = input("Introduce el prompt: ").strip()

# Carga el esquema de blog.sql
schema_sql = cargar_schema_sql(SCHEMA_PATH)

# Construye el contexto a inyectar en el prompt
contexto_sql = ""
if schema_sql:
    contexto_sql = (
        "Eres un asistente experto en SQL. A continuación tienes el esquema de base de datos "
        "extraído del archivo 'blog.sql'. Usa **exclusivamente** esta estructura para responder "
        "preguntas y proponer consultas SQL (estándar ANSI cuando sea posible). "
        "Responde siempre con:\n"
        "1) Breve explicación\n"
        "2) La consulta SQL dentro de un bloque ```sql```.\n\n"
        "=== ESQUEMA (blog.sql) ===\n"
        f"{schema_sql}\n"
        "=== FIN DEL ESQUEMA ===\n\n"
    )
else:
    contexto_sql = (
        "Eres un asistente experto en SQL. (Aviso: no se encontró 'blog.sql', responde de forma "
        "general sin validar contra un esquema cargado.)\n\n"
    )

# Prompt final que se envía al modelo
prompt_final = (
    f"{contexto_sql}"
    f"Pregunta del usuario:\n{prompt_usuario}\n"
)

# Construye el payload para Ollama
payload = {
    "model": "llama3:latest",
    "prompt": prompt_final,
    # Opcionalmente puedes fijar 'stream': True/False; por defecto es True y devolvemos JSONL
    # "stream": True
    # También puedes añadir un 'system' si prefieres separar instrucciones:
    # "system": "Sigue estrictamente el esquema proporcionado y el formato de salida indicado."
}

# Ejecuta la llamada curl
result = subprocess.run(
    [
        "curl", "-s", "http://localhost:11434/api/generate",
        "-d", json.dumps(payload)
    ],
    capture_output=True,
    text=True
)

# Parseo estilo jq + tr
try:
    lines = result.stdout.splitlines()
    response = ""
    for line in lines:
        if not line.strip():
            continue
        obj = json.loads(line)
        if "response" in obj and obj["response"] is not None:
            response += obj["response"]
    print(response.strip())
except Exception as e:
    print("Error parsing output:", e)
    print(result.stdout)

```

---

## 4. Conclusión breve

Este tipo de automatización puede ser muy útil en programación, en lugar de escribir manualmente cada consulta SQL, puedes delegar parte del trabajo a un modelo que, conociendo el esquema de la base de datos, te proponga consultas ya casi listas para pegar en tu gestor de bases de datos o en tu código.


---

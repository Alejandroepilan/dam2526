import subprocess
import json
import os

SCHEMA_PATH = "blog.sql"
MAX_SCHEMA_CHARS = 200_000  # por si el .sql es enorme, evita pasarte de contexto


def cargar_schema_sql(path: str) -> str:
    """
    Lee el contenido del archivo SQL que contiene el esquema de la base de datos.
    Si el archivo no existe, devuelve una cadena vacía.
    Si es muy grande, lo recorta para no pasar demasiado contexto al modelo.
    """
    if not os.path.exists(path):
        return ""
    with open(path, "r", encoding="utf-8", errors="ignore") as f:
        schema = f.read()
    if len(schema) > MAX_SCHEMA_CHARS:
        schema = schema[:MAX_SCHEMA_CHARS] + "\n-- [Truncado para no exceder el contexto]\n"
    return schema


def main():
    # 1) Introduce el prompt / pregunta del usuario
    prompt_usuario = input("Introduce la pregunta del usuario: ").strip()

    # 2) Carga el esquema de blog.sql
    schema_sql = cargar_schema_sql(SCHEMA_PATH)

    # 3) Construye el contexto con el esquema y las instrucciones
    if schema_sql:
        contexto_sql = (
            "Eres un asistente experto en SQL. A continuación tienes el esquema de base de datos "
            "extraído del archivo 'blog.sql'. Usa exclusivamente esta estructura para responder "
            "preguntas y proponer consultas SQL (estándar ANSI cuando sea posible). "
            "Responde siempre con:\n"
            "1) Breve explicación.\n"
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

    # 4) Construye el payload para el modelo
    payload = {
        "model": "llama3:latest",  # o "qwen2.5:7b-instruct-q4_0" según tengas en Ollama
        "prompt": prompt_final,
        # "stream": True  # por defecto suele hacer streaming JSONL
    }

    # 5) Ejecuta la llamada curl usando subprocess.run
    result = subprocess.run(
        [
            "curl", "-s", "http://localhost:11434/api/generate",
            "-d", json.dumps(payload)
        ],
        capture_output=True,
        text=True
    )

    # 6) Parseo del JSON línea a línea (similar a usar jq + tr en Linux)
    try:
        lines = result.stdout.splitlines()
        response = ""
        for line in lines:
            if not line.strip():
                continue
            obj = json.loads(line)
            if "response" in obj and obj["response"] is not None:
                response += obj["response"]
        print("\n=== Respuesta del modelo ===\n")
        print(response.strip())
    except Exception as e:
        print("Error parsing output:", e)
        print("Salida completa de curl:")
        print(result.stdout)


if __name__ == "__main__":
    main()

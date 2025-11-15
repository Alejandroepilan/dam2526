# Ejercicio 6 – Comunicación entre procesos

**Autor:** Alejandro Épila  
**Asignatura:** Programación de servicios y procesos  
**Curso:** 2º DAM  
**Fecha:** Noviembre 2025

---

## 1. Introducción breve y contextualización

Un WebSocket es un canal de comunicación bidireccional y en tiempo real entre un cliente (normalmente un navegador) y un servidor. A diferencia de HTTP clásico (petición → respuesta), con WebSocket ambas partes pueden enviarse mensajes cuando quieran, sin tener que abrir conexiones nuevas cada vez.

---

## 2. Desarrollo detallado y preciso

#### Servidor WebSocket

Este servidor esta preparado para:

- Aceptar conexiones.

- Enviar una tarea repeat_multiply al cliente al conectarse.

- Escuchar el resultado y mostrarlo por consola.

#### Cliente WebSocket

Puntos clave del cliente:

- new ``WebSocket(url)`` → abre la conexión.

- ``onmessage`` → cuando recibe una tarea, realiza el cálculo y responde.

- ``Math.pow(factor, times)`` → hace el cálculo de forma eficiente.

- Se devuelve un JSON con ``type: "result"``, ``task_id``, ``result``, ``duration_ms`` y ``agent``.

- Se gestionan eventos de conexión, cierre y error (con reintentos).

---

## 3. Aplicación práctica

### Como probarlo

#### 1. Lanza el servidor:
  ```
  py servidor.py
  ```

Deberías ver algo como:
  ```
  Servidor WebSocket en ws://127.0.0.1:8765 listo.
  ```

#### 2. Abre el cliente

  - Abre ``cliente.html`` en tu navegador.

#### 3. Observa:

EN la consola dfel navegador verás:

   - “✅ Connected”

   - “🧮 Task received: { … }”

   - “📤 Result sent: { … }”

En la consola de Python verás algo como:

```
Conectado #1 desde ('127.0.0.1', 54321) path=/
Clientes conectados (1):
  - #1 ('127.0.0.1', 54321)
[#1] Tarea enviada task_id=1
[#1] ✅ Resultado task_id=1
          result=1.000435...
          duration_ms=3
          agent=Mozilla/5.0 (...)

```

Esto demuestra que:

- El servidor envía la tarea.

- El cliente la recibe, calcula y responde.

- El servidor muestra el resultado correctamente.

#### ``cliente.html``

```
<!doctype html>
<html>

<head>
  <meta charset="utf-8">
  <title>WS Compute Client</title>
</head>

<body>
  <script>
    // URL del servidor WebSocket local
    const url = "ws://127.0.0.1:8765";
    let ws, reconnectTimer;

    function connect() {
      // Crear conexión WebSocket
      ws = new WebSocket(url);

      // Evento: conexión establecida
      ws.onopen = () => {
        console.log("✅ Connected to", url);
      };

      // Evento: mensaje recibido del servidor
      ws.onmessage = (e) => {
        try {
          const msg = JSON.parse(e.data);
          // Comprobamos si es una tarea de tipo repeat_multiply
          if (msg.type === "task" && msg.op === "repeat_multiply") {
            const { task_id, initial, factor, times } = msg;
            console.log("🧮 Task received:", msg);

            const t0 = performance.now();
            // Cálculo: initial * (factor ** times)
            // Math.pow es más eficiente que multiplicar en un bucle
            const result = initial * Math.pow(factor, times);
            const duration_ms = Math.round(performance.now() - t0);

            // Construimos el mensaje de resultado
            const reply = {
              type: "result",
              task_id,
              result,
              duration_ms,
              agent: navigator.userAgent
            };

            // Enviar resultado de vuelta al servidor
            ws.send(JSON.stringify(reply));
            console.log("📤 Result sent:", reply);
          } else {
            console.log("📩 Message:", msg);
          }
        } catch (err) {
          console.log("📩 Raw message (no JSON):", e.data);
        }
      };

      // Evento: conexión cerrada
      ws.onclose = (e) => {
        console.warn("❌ Closed:", e.code, e.reason);
        scheduleReconnect();
      };

      // Evento: error
      ws.onerror = (e) => {
        console.error("⚠️ Error:", e);
        // Dejamos que onclose gestione el reconectar
      };
    }

    // Reintento automático de conexión
    function scheduleReconnect() {
      if (reconnectTimer) return;
      reconnectTimer = setTimeout(() => {
        reconnectTimer = null;
        console.log("🔄 Reconnecting…");
        connect();
      }, 3000);
    }

    // Iniciar la conexión
    connect();
  </script>
</body>

</html>
```

#### ``servidor.py``

```
import asyncio
import itertools
import json
import websockets
from websockets.exceptions import ConnectionClosed

# Secuencia para IDs de tareas y clientes
TASK_SEQ = itertools.count(1)
CLIENTS = {}  # {cid: ws}
ID_SEQ = itertools.count(1)

async def send_task(ws, *, initial: float, factor: float, times: int):
    """
    Envía al cliente una tarea de multiplicación repetida:
    result = initial * (factor ** times)
    """
    task_id = next(TASK_SEQ)
    payload = {
        "type": "task",
        "op": "repeat_multiply",
        "task_id": task_id,
        "initial": initial,
        "factor": factor,
        "times": times,
    }
    await ws.send(json.dumps(payload))
    return task_id

def list_clients():
    """Muestra por consola la lista de clientes conectados."""
    if not CLIENTS:
        print("No hay clientes conectados.")
        return
    print(f"Clientes conectados ({len(CLIENTS)}):")
    for cid, ws in CLIENTS.items():
        print(f"  - #{cid} {getattr(ws,'remote_address',None)}")

async def handler(ws):
    """
    Función handler que gestiona una conexión entrante:
    - Asigna un ID al cliente
    - Envía una tarea de cálculo
    - Espera el resultado del cliente
    """
    cid = next(ID_SEQ)
    CLIENTS[cid] = ws
    print(f"Conectado #{cid} desde {getattr(ws,'remote_address',None)} path={getattr(ws,'path',None)}")
    list_clients()

    # Enviar una tarea de cálculo nada más conectar
    task_id = await send_task(
        ws,
        initial=1.0000054,
        factor=1.00000043,
        times=1_000_000
    )
    print(f"[#{cid}] Tarea enviada task_id={task_id}")

    try:
        # Bucle de recepción de mensajes del cliente
        async for raw in ws:
            try:
                msg = json.loads(raw)
            except Exception:
                print(f"[#{cid}] Mensaje no-JSON: {raw!r}")
                continue

            # Procesar mensaje de tipo "result"
            if msg.get("type") == "result" and msg.get("task_id") == task_id:
                result = msg.get("result")
                duration = msg.get("duration_ms")
                ua = msg.get("agent")
                print(f"[#{cid}] ✅ Resultado task_id={task_id}")
                print(f"          result={result}")
                if duration is not None:
                    print(f"          duration_ms={duration}")
                if ua:
                    print(f"          agent={ua}")
            else:
                # Aquí se podrían manejar otros tipos de mensajes
                pass

    except ConnectionClosed as e:
        print(f"[#{cid}] conexión cerrada: {e.code} {e.reason}")
    finally:
        CLIENTS.pop(cid, None)
        print(f"Desconectado #{cid}")
        list_clients()

async def main():
    # Crear el servidor WebSocket en localhost:8765
    async with websockets.serve(
        handler,
        host="127.0.0.1",
        port=8765,
        ping_interval=None,   # simple: sin pings automáticos
    ):
        print("Servidor WebSocket en ws://127.0.0.1:8765 listo.")
        # Mantener el servidor corriendo para siempre
        await asyncio.Future()

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nSaliendo…")

```

---

## 4. Conclusión breve

Con este proyecto se ve en la práctica cómo usar WebSocket para comunicación en tiempo real entre un servidor y un cliente web:

- El servidor no se limita a responder peticiones puntuales, sino que mantiene una conexión abierta y puede enviar tareas cuando quiera.

- El cliente ejecuta cálculos complejos en tiempo real y devuelve los resultados, lo que se podría aplicar a:

  - Simuladores que reparten carga de cálculo entre varios clientes.

  - Dashboards que muestran resultados en tiempo real.

---

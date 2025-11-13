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

---

## 4. Conclusión breve

Con este proyecto se ve en la práctica cómo usar WebSocket para comunicación en tiempo real entre un servidor y un cliente web:

- El servidor no se limita a responder peticiones puntuales, sino que mantiene una conexión abierta y puede enviar tareas cuando quiera.

- El cliente ejecuta cálculos complejos en tiempo real y devuelve los resultados, lo que se podría aplicar a:

  - Simuladores que reparten carga de cálculo entre varios clientes.

  - Dashboards que muestran resultados en tiempo real.

---

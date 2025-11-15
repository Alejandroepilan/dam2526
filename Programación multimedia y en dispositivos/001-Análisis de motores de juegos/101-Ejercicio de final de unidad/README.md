# Ejercicio 101 - Ejercicio de final de unidad

**Autor:** Alejandro Épila  
**Asignatura:** Programación multimedia y en dispositivos  
**Curso:** 2º DAM  
**Fecha:** Noviembre 2025

---

## 1. Introducción breve y contextualización

En esta actividad he desarrollado un minijuego tipo Tower Defense usando HTML, Canvas 2D y JavaScript. El objetivo era aplicar lo aprendido sobre animación por bucle, entrada del usuario y dibujo en pantalla mediante el contexto 2D del canvas.

---

## 2. Desarrollo detallado y preciso

El juego incluye un enemigo que sigue un camino predefinido, torres colocadas con el ratón y disparos automáticos cuando el enemigo entra en su rango. El movimiento se gestiona con un bucle usando ``requestAnimationFrame``, las colisiones y distancias se calculan con ``Math.hypot``, y el canvas se usa para dibujar fondo, camino, torres, balas y enemigo en cada frame.

---

## 3. Aplicación práctica

El usuario puede colocar torres haciendo clic en el canvas. El enemigo avanza por el recorrido y las torres disparan de forma automática. Si el enemigo llega al final, el juego muestra “Has perdido”, y si su vida llega a cero, aparece “Has ganado”. Es un ejemplo funcional y simple de lógica de juego con animaciones y elementos interactivos.

#### ``index.html``

```
<!doctype html>
<html>

<head>
  <meta charset="utf-8">
  <title>Mini Tower Defense</title>
  <style>
    body {
      margin: 0;
      background: #111;
      overflow: hidden;
    }

    canvas {
      background: #1e293b;
      display: block;
      margin: 0 auto;
    }
  </style>
</head>

<body>
  <canvas id="game" width="640" height="480"></canvas>

  <script>
    const canvas = document.getElementById("game");
    const contexto = canvas.getContext("2d");

    // el camino que va a seguir el enemigo, punto por punto
    const camino = [
      { x: 20, y: 220 }, { x: 200, y: 220 }, { x: 200, y: 80 },
      { x: 440, y: 80 }, { x: 440, y: 360 }, { x: 620, y: 360 }
    ];

    // enemigo con vida, velocidad y en que punto del camino va
    let enemy = { x: camino[0].x, y: camino[0].y, hp: 100, speed: 1, index: 0 };

    let torres = [];
    let bullets = [];

    let gameOver = false;

    // rango maximo al que dispara una torre
    const RANGO = 120;

    // cuando hago click, creo una torre en esa posicion
    canvas.addEventListener("click", (e) => {
      if (gameOver) return;
      const r = canvas.getBoundingClientRect(); // obtener x,y del click en el canvas
      torres.push({ x: e.clientX - r.left, y: e.clientY - r.top, cd: 0 }); // e.clientX/Y son las coordenadas del click en la pantalla, resto la posicion del canvas y cd es el cooldown
    });

    // -----------------------------------------------------------------------------------------------------------------

    function moveEnemy() {
      if (gameOver) return;

      // siguiente punto del camino
      const t = camino[enemy.index + 1];

      // si no hay siguiente punto, a llegado al final
      if (!t) {
        gameOver = true;
        alert("Has perdido");
        return;
      }

      // calculo hacia donde tiene que ir, diferencia en x e y
      const dx = t.x - enemy.x;
      const dy = t.y - enemy.y;
      const dist = Math.hypot(dx, dy); // distancia al siguiente punto

      // cuando esta a menos de 2 px, pasa al siguiente
      if (dist < 2) { enemy.index++; return; }

      // avanzo al enemigo hacia el siguiente punto, dividido por la distancia para normalizar y multiplicado por la velocidad
      enemy.x += dx / dist * enemy.speed;
      enemy.y += dy / dist * enemy.speed;
    }

    function updateTorres() {
      if (gameOver) return;

      torres.forEach(t => {
        t.cd--; // cooldown baja cada frame

        // calculo la distancia entre la torre y el enemigo, direccion del disparo
        const dx = enemy.x - t.x;
        const dy = enemy.y - t.y;

        // si el enemigo esta dentro del rango y el cooldown esta listo, disparo una bala
        if (Math.hypot(dx, dy) < RANGO && t.cd <= 0) {
          bullets.push({ x: t.x, y: t.y, dx: dx / 20, dy: dy / 20 }); // creo la bala, hacia el enemigo, 20 para que no vaya muy rapido
          t.cd = 30; // reinicio el cooldown
        }
      });
    }

    function moveBalas() {
      if (gameOver) return;

      bullets.forEach(b => { // muevo cada bala, sumando su velocidad
        b.x += b.dx;
        b.y += b.dy;
      });

      bullets = bullets.filter(b => {  // filtro las balas que siguen vivas
        const hit = Math.hypot(b.x - enemy.x, b.y - enemy.y) < 10; // calcula la distancia entre la bala y el enemigo, si menos de 10 hay impacto
        if (hit) enemy.hp -= 10; // le baja la vida

        return !hit && b.x > 0 && b.x < 640 && b.y > 0 && b.y < 480; // si impacta o sale de la pantalla, se elimina la bala
      });

      // si la vida llega a 0 ganas
      if (enemy.hp <= 0 && !gameOver) {
        gameOver = true;
        alert("Has ganado");
      }
    }

    function draw() {
      // ###### el fondo
      contexto.fillStyle = "#1e293b";
      contexto.fillRect(0, 0, 640, 480);

      // ###### el camino
      contexto.strokeStyle = "#38bdf8";
      contexto.lineWidth = 8;
      contexto.beginPath(); // empieza un nuevo camino
      contexto.moveTo(camino[0].x, camino[0].y); // mueve el "lapiz" al primer punto
      for (let p of camino) contexto.lineTo(p.x, p.y); // dibuja lineas hasta cada punto del camino
      contexto.stroke(); // pinta el camino

      torres.forEach(t => {
        // ###### borde con el rango visible torre (stroke = contorno)
        contexto.strokeStyle = "rgba(255,255,255,0.15)";
        contexto.lineWidth = 2;
        contexto.beginPath();
        contexto.arc(t.x, t.y, RANGO, 0, Math.PI * 2); // circulo con el rango de disparo de la torre, donde esta la torre, radio RANGO, del grado 0 a 2PI (360 grados)
        contexto.stroke();

        // ###### circulo del cuerpo de la torre (fill = relleno)
        contexto.fillStyle = "#22c55e";
        contexto.beginPath();
        contexto.arc(t.x, t.y, 10, 0, Math.PI * 2); // lo mismo que para el rango pero el radio es 10 que es el cuerpo de la torre
        contexto.fill();
      });

      // ###### balas
      bullets.forEach(b => {
        contexto.fillStyle = "#fbbf24";
        contexto.fillRect(b.x - 3, b.y - 3, 6, 6);
      });

      // ###### enemigo
      if (!gameOver) {
        contexto.fillStyle = "#ef4444";
        contexto.beginPath();
        contexto.arc(enemy.x, enemy.y, 12, 0, Math.PI * 2);
        contexto.fill();

        // ###### barra de vida
        contexto.fillStyle = "white";
        contexto.fillText("HP: " + enemy.hp, enemy.x - 15, enemy.y - 18);
      }
    }

    // bucle principal del juego
    function loop() {
      if (!gameOver) {
        moveEnemy();
        updateTorres();
        moveBalas();
      }

      draw();

      requestAnimationFrame(loop); // llama en cada frame al loop
    }

    loop();
  </script>
</body>

</html>
```

---

## 4. Conclusión breve

Este proyecto me ha servido para entender cómo combinar dibujo en canvas con lógica de juego, movimiento, colisiones y eventos de usuario. Aunque es un juego muy básico, resume bien los conceptos de la unidad: bucle principal, animación, interacción y actualización continua de la escena.

---

# Examen final

**Autor:** Alejandro Épila  
**Asignatura:** Programación multimedia y en dispositivos  
**Curso:** 2º DAM  
**Fecha:** Noviembre 2025

---

## 1. Introducción breve y contextualización

- Para este proyecto he decidico desarrollar una versión muy básica de un minijuego del tipo **Tower Defense**, donde una serie de enemigos van cruzando por un camino hasta llegar al final y en este caso perder la partida. Para evitar esto el jugador deberá colocar diferentes torres de apoyo para defenderse de los enemigos y evitar así la derrota.

- Para la realización del proyecto he utilizado HTML, Canvas 2D y JavaScript:

  - **HTML** y **Canvas 2D**: gracias a estas dos tecnologias se pueden crear de forma sencilla y práctica gráficos en 2D, para poder dibujar partes del escenario como el fondo, el camino, los enemigos, las torres o las balas.
  - **JavaScript**: en cambio con esta otra tecnologia se maneja la lógica del juego, es decir, con ella podemos crear el movimiento de los enemigos, la colocación de las torres, el recuento de la vida de los enemigos, etc.

- Una simple pero potente combinación con la que podemos contruir gráficos en 2D y su respectiva lógica.

---

## 2. Desarrollo detallado y preciso

### Estructura y variables del juego

- Para empezar creamos un canva en el centro de la pantalla, el cuál guardamos en la constante `canvas`, con su respectivo `contexto`.
- Seguidamente declaramos en el array constante `camino` los puntos x e y que forman el trazo del mismo.
- Ahora declamos la variable `enemy` que contendrá:
  - `x` e `y` -> posición en el camino del enemigo con `camino[0].x/y`.
  - `hp` -> número entero con la salud del enemigo.
  - `speed` -> velocidad del enemigo.
  - `index` -> punto del camino en el que se encuentra el enemigo.
- Luego declaramos el array `torres` y `bullets`, la variable `gameOver` que guarda el estado de la partida y la constante `RANGO` que indica el rango maximo al que dispara una torre.
- Por último capturamos el evento click en pantalla, y si la partida no se ha terminado, obtenemos la posición x e y del click en el canvas. Añadimos al array `torres` los datos `x` e `y` restando las coordenadas de la pantalla a las del canvas y `cd` que es el cooldown del disparo.

### Lógica principal

- Primero declaramos la función `loop()` que es el bucle principal del juego.
- Más adelante vemos que la partida no se haya terminado, sino, ejecutamos las funciones `moveEnemy()`, `updateTorres()` y `moveBalas()` respectivamente.
- Luego ejecutamos la función `draw()`.
- Y por último ejecutamos la función `requestAnimationFrame(loop);` para que en cada frame llame a la función `loop()`, que es básicamente el bucle principal del juego.

### Enemigo

- En la función `moveEnemy()` tenemos:
  - Primero una comprobación del estado de la partida.
  - Ahora guardamos en la constante `t` un `+1` en el index de `camino` para obtener el siguiente punto de avance del enemigo.
  - Justo despues comprobamos si no hay siguiente punto entonces significa que el enemigo ha llegado al final del camino por lo tanto hemos perdido la partida y mostramos una alerta con dicho mensaje.
  - Luego guardamos en las constantes `dx` y `dy` las resta entre el siguiente punto y la posicion actual del jugador, para saber hacia donde tiene que ir y en la constante `dist` la diferencia al siguiente punto. Cuando esta diferencia es menor a `2` sumamos un punto al indice del enemigo.
  - Por último avanzamos al enemigo al siguiente punto, diviendo el calculo de hacia donde tiene que ir `dx` y `dy` entre `dist` para normalizar a un numero más pequeño y lo multiplicamos por su velocidad, para así poder ajustarla.

### Torres

- En la función `updateTorres()` tenemos:
  - Primero una comprobación del estado de la partida.
  - Luego tenemos un `forEach()` sobre el array `torres` que resta 1 punto a `cd` en cada frame.
  - Seguidamente guardamos en `dx` y `dy` el cálculo de la distancia entre la torre y el enemigo, para poder sacar la dirección del disparo.
  - Ahora comprobamos si el enemigo está dentro del `RANGO` de la torre y si el `cd` es menor o igual a `0`, entonces disparamos una bala.
  - Despues creamos la bala y la añadimos a `balas`, en la posición de la torre y directa a la posición del cálculo `dx` y `dy` restándole `20` para que no vaya demasiado rapido. Esto es básicamente la velocidad de la bala, esto se podría guardar en otra constante para así poder modificarse de forma más cómodamente.
  - Por último reiniciamos el `cd` siendo que sea igual a `30`. Esto lo mismo, se podría hacer una constante que guarde el tiempo de cooldown de disparo de las torres.

### Balas

- En la función `moveBalas()` tenemos:
  - Primero una comprobación del estado de la partida.
  - Luego tenemos un `forEach()` sobre el array `balas` para mover cada bala sumándole su velocidad.
  - Ahora con un `filter` filtramos las balas que sigan "vivas", en la constante `hit` calculamos la distancia entre la bala y el enemigo, si es menor de `10` hay impacto en el enemigo.
  - Despues si hay `hit` restamos `10` puntos la vida al enemigo. Y si la bala impacta en el enemigo o simplemente sale del canva la eliminamos del array.
  - Por último comprobamos si la vida del enemigo es menor o igual a `0` y no se ha terminado ya la partida, entonces mostramos un alerta indicando la victoria.

### Dibujo

- En la función `draw()` tenemos:

  - Para empezar dibujamos un rectángulo para el fondo, luego dibujamos una linea con grosor `8` que se vaya moviendo por los diferentes puntos del `camino`.
  - Ahora hacemos un `torres.forEach` para cada torre dibujamos una circunferencia, desde el ángulo `0` a `Math.PI * 2` que es el ángulo 360º, con el radio de `RANGO` para mostrar el alcance de la torre. Y también dibujamos un circulo de radio `10` que será la propia torre.
  - Despues hacemos otro `forEach()` pero esta vez del array `balas` para dibujar un pequeño cuadrado por cada bala en pantalla.
  - Y por último comprobamos que la partida no haya finalizado y dibujamos un circulo que será el enemigo y justo encima le dibujamos el texto con la vida del mismo.

---

## 3. Aplicación práctica

### Colocar torres

- Con este `addEventListener` podemos detectar si se ha hecho click en la pantalla y así poder colocar una torre en la posición clicada.

```
canvas.addEventListener("click", (e) => {
  if (gameOver) return;
  const r = canvas.getBoundingClientRect(); // obtener x,y del click en el canvas
  torres.push({ x: e.clientX - r.left, y: e.clientY - r.top, cd: 0 }); // e.clientX/Y son las coordenadas del click en la pantalla, resto la posicion del canvas y cd es el cooldown
});
```

### Movimiento del enemigo

- Gracias a esta funcion podenmos mover el jugador por los diferentes puntos del camino, y si este llega al último simplemente se pierde la partida.

```
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
```

### Disparo de las torres a los enemigos

- Con esta función podemos hacer que las torres disparen a la posición del enemigo con cierto cooldown.

```
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
```

### Movimiento de las balas

- Esta función nos permite crear el movimiento de las balas disparadas por cada torre y eliminarlas en caso de impacto en el enemigo o si salen de la pantalla.

```
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
```

### Dibujo de componentes

- Con esta función podemos dibujar todos los componentes del minijuego: el fondo, el camino, los bordes del rango de las torres, las torres, las balas, el enemigo y su respectiva barra de vida.

```
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
```

### Bucle prncipal del juego

- Este es el bucle principal del juego que simplemente hace que cada frame, si la partida no ha terminado, ejecute la funcion de mover al enemigo, hacer que las torres disparen, que las balas se muevan y dibujar los componentes del minijuego.

```
function loop() {
  if (!gameOver) {
    moveEnemy();
    updateTorres();
    moveBalas();
  }

  draw();

  requestAnimationFrame(loop); // llama en cada frame al loop
}
```

---

## 4. Conclusión breve

- Sin duda se podrían aplicar infinidad de mejoras al minijuego, desde una pantalla de inicio con guardados de partidas y ajuste, hasta la posibilidad de poder elegir entre varias torres de apoyo según el enemigo al que tengamos que frenar.

- Gracias a este pequeño minijuego del tipo **Tower Defense** he podido utilizar varias tecnologias para dibujar gráficos en 2D y crear lógica. Con lo que he aprendido a dibujar diferentes formas y trazos, calcular distancias entre estas, poder darles movimiento y detectar colisiones.

---

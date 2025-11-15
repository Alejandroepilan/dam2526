# Ejercicio 1 – Arquitectura del juego. Componentes

**Autor:** Alejandro Épila  
**Asignatura:** Programación multimedia y en dispositivos  
**Curso:** 2º DAM  
**Fecha:** Noviembre 2025

---

## 1. Introducción breve y contextualización

En este ejercicio he trabajado con un juego estilo Asteroids donde el movimiento no es instantáneo, sino que depende de inercia, aceleración, rozamiento y velocidad máxima. El objetivo era entender cómo funcionan estas fuerzas dentro de un videojuego y cómo afectan al control del jugador. Además, he añadido dos nuevas funcionalidades al código original:

- Estrellas que se mueven aleatoriamente en el fondo.

- Balas con velocidad modificada para comprobar cómo esto afecta la jugabilidad.

---

## 2. Desarrollo detallado y preciso

He realizado las siguientes modificaciones sobre el código base:

#### Modificaciones en físicas del jugador

- Cambié la aceleración del jugador a ``0.22`` para que acelere más rápido.

- Ajusté el rozamiento a ``0.992`` para que tarde más en frenarse, aumentando la sensación de inercia.

- Modifiqué ``velMax`` a ``9`` para limitar mejor la velocidad máxima.

El jugador ahora se mueve suavemente por el escenario, y al soltar la tecla no se detiene de golpe: sigue desplazándose hasta que el rozamiento reduce su velocidad.

#### Balas con velocidad variable

- Modifiqué la velocidad de bala a ``16``, haciendo que salgan más rápido del cañón.

- Esto afecta a cómo se rompen las rocas y al control de disparo.

#### Estrellas móviles

Añadí una clase ``Estrella`` que ahora incluye:

- Velocidad en X e Y.

- Movimiento continuo.

- Desaparición por un lado y reaparición por el otro.

Esto crea un fondo animado que da sensación de movimiento espacial.

---

## 3. Aplicación práctica

Durante la práctica, probé varios valores para ver diferencias claras:

#### Aceleración y rozamiento

- Con aceleración muy alta, el jugador salía disparado y se hacía difícil controlar.

- Con rozamiento fuerte, el jugador frenaba demasiado rápido y se perdía la sensación de inercia.

Finalmente elegí valores que dan un equilibrio entre realismo y jugabilidad.

#### Velocidad de las balas

- Balas rápidas → más efectivas para romper rocas.

- Balas lentas → más visibles pero menos útiles.

#### Estrellas móviles

Al ejecutarse junto al movimiento del jugador, el fondo parece vivo y dinámico.

Probé los cambios jugando varias rondas del nivel inicial, observando si el manejo era fluido, si las rocas eran fáciles de esquivar y si la velocidad de las balas afectaba a la dificultad.

#### ``index.html``

```
<!doctype html>
<html>

<head>
  <meta charset="utf-8" />
  <title>Asteroids-lite</title>
  <style>
    html,
    body {
      margin: 0;
      padding: 0;
      overflow: hidden;
      background: #000
    }

    canvas {
      display: block;
      background: #000
    }
  </style>
</head>

<body>
  <canvas id="lienzo"></canvas>
  <script>
    const lienzo = document.getElementById("lienzo");
    const contexto = lienzo.getContext("2d");

    function redimensiona() {
      lienzo.width = window.innerWidth;
      lienzo.height = window.innerHeight;
    }
    window.onresize = redimensiona;
    redimensiona();

    let anchura = lienzo.width;
    let altura = lienzo.height;

    function distancia(x1, y1, x2, y2) {
      const dx = x2 - x1;
      const dy = y2 - y1;
      return Math.sqrt(dx * dx + dy * dy);
    }

    class Jugador {
      constructor() {
        this.posx = anchura / 2;
        this.posy = altura / 2;
        this.angulo = 0;
        this.velx = 0;
        this.vely = 0;
        this.aceleracion = 0.22;
        this.rozamiento = 0.992;
        this.velMax = 9;
      }
      dibuja() {
        const noseLen = 22, baseLen = 14, spread = Math.PI * 0.75;
        const noseX = this.posx + Math.cos(this.angulo) * noseLen;
        const noseY = this.posy + Math.sin(this.angulo) * noseLen;
        const leftX = this.posx + Math.cos(this.angulo + spread) * baseLen;
        const leftY = this.posy + Math.sin(this.angulo + spread) * baseLen;
        const rightX = this.posx + Math.cos(this.angulo - spread) * baseLen;
        const rightY = this.posy + Math.sin(this.angulo - spread) * baseLen;

        contexto.fillStyle = "white";
        contexto.beginPath();
        contexto.moveTo(noseX, noseY);
        contexto.lineTo(leftX, leftY);
        contexto.lineTo(rightX, rightY);
        contexto.closePath();
        contexto.fill();

        contexto.fillStyle = "red";
        contexto.beginPath();
        contexto.arc(this.posx, this.posy, 5, 0, Math.PI * 2);
        contexto.fill();
      }
      aplicaThrust(on) {
        if (!on) return;
        this.velx += Math.cos(this.angulo) * this.aceleracion;
        this.vely += Math.sin(this.angulo) * this.aceleracion;
        const v = Math.hypot(this.velx, this.vely);
        if (v > this.velMax) {
          const f = this.velMax / v;
          this.velx *= f; this.vely *= f;
        }
      }
      mueve() {
        this.velx *= this.rozamiento;
        this.vely *= this.rozamiento;
        this.posx += this.velx;
        this.posy += this.vely;

        if (this.posx < 0) this.posx += anchura;
        if (this.posx > anchura) this.posx -= anchura;
        if (this.posy < 0) this.posy += altura;
        if (this.posy > altura) this.posy -= altura;
      }
    }

    const velocidadBala = 16;

    class Bala {
      constructor(x, y, a) {
        this.posx = x;
        this.posy = y;
        this.angulo = a;
        this.velocidad = velocidadBala;
      }
      dibuja() {
        contexto.fillStyle = "dodgerblue";
        contexto.beginPath();
        contexto.arc(this.posx, this.posy, 3, 0, Math.PI * 2);
        contexto.fill();
      }
      mueve() {
        this.posx += Math.cos(this.angulo) * this.velocidad;
        this.posy += Math.sin(this.angulo) * this.velocidad;
      }
    }

    class Estrella {
      constructor() {
        this.posx = Math.random() * anchura;
        this.posy = Math.random() * altura;
        const v = Math.random() * 0.3 + 0.1;
        const dir = Math.random() * Math.PI * 2;
        this.vx = Math.cos(dir) * v;
        this.vy = Math.sin(dir) * v;
      }
      dibuja() {
        contexto.fillStyle = "white";
        contexto.beginPath();
        contexto.arc(this.posx, this.posy, 1, 0, Math.PI * 2);
        contexto.fill();
      }
      mueve() {
        this.posx += this.vx;
        this.posy += this.vy;
        if (this.posx < 0) this.posx += anchura;
        if (this.posx > anchura) this.posx -= anchura;
        if (this.posy < 0) this.posy += altura;
        if (this.posy > altura) this.posy -= altura;
      }
    }

    class Roca {
      constructor() {
        this.radio = Math.random() * 20 + 10;
        let ok = false;
        while (!ok) {
          this.posx = Math.random() * anchura;
          this.posy = Math.random() * altura;
          ok = distancia(this.posx, this.posy, jugador?.posx || anchura / 2, jugador?.posy || altura / 2) > 80;
        }
        this.angulo = Math.random() * Math.PI * 2;
        this.lados = Math.round(Math.random() * 20 + 5);
        const rugosidad = 0.4;
        this.puntas = Array.from({ length: this.lados }, () => 1 + (Math.random() * 2 - 1) * rugosidad);
        const v = Math.random() * 1.6 + 0.4;
        const dir = Math.random() * Math.PI * 2;
        this.vx = Math.cos(dir) * v;
        this.vy = Math.sin(dir) * v;
        this.rot = (Math.random() - 0.5) * 0.04;
      }
      dibuja() {
        contexto.fillStyle = "grey";
        contexto.beginPath();
        for (let i = 0; i < this.lados; i++) {
          const ang = (i / this.lados) * Math.PI * 2 + this.angulo;
          const r = this.radio * this.puntas[i];
          const x = this.posx + Math.cos(ang) * r;
          const y = this.posy + Math.sin(ang) * r;
          if (i === 0) contexto.moveTo(x, y); else contexto.lineTo(x, y);
        }
        contexto.closePath();
        contexto.strokeStyle = "#333";
        contexto.fill();
      }
      mueve() {
        this.angulo += this.rot;
        this.posx += this.vx;
        this.posy += this.vy;

        if (this.posx - this.radio < 0) {
          this.posx = this.radio;
          this.vx = Math.abs(this.vx);
        } else if (this.posx + this.radio > anchura) {
          this.posx = anchura - this.radio;
          this.vx = -Math.abs(this.vx);
        }

        if (this.posy - this.radio < 0) {
          this.posy = this.radio;
          this.vy = Math.abs(this.vy);
        } else if (this.posy + this.radio > altura) {
          this.posy = altura - this.radio;
          this.vy = -Math.abs(this.vy);
        }
      }
    }

    const jugador = new Jugador();

    let estrellas = Array.from({ length: 100 }, () => new Estrella());
    let balas = [];
    let rocas = [];
    let level = 1;
    let rocksPerLevel = 4;
    let levelMessageTimer = 0;

    function spawnRocas(num) {
      for (let i = 0; i < num; i++) {
        rocas.push(new Roca());
      }
    }
    function startLevel() {
      rocas.length = 0;
      spawnRocas(rocksPerLevel);
      levelMessageTimer = 120;
    }
    startLevel();

    let giro = 0;
    let thrust = false;

    document.body.onkeydown = (e) => {
      switch (e.key) {
        case "a": giro = -1; break;
        case "d": giro = 1; break;
        case "w": thrust = true; break;
      }
      if (e.code === "Space") {
        balas.push(new Bala(jugador.posx, jugador.posy, jugador.angulo));
      }
    };
    document.body.onkeyup = (e) => {
      switch (e.key) {
        case "a": if (giro === -1) giro = 0; break;
        case "d": if (giro === 1) giro = 0; break;
        case "w": thrust = false; break;
      }
    };

    function bucle() {
      jugador.angulo += giro * 0.08;
      jugador.aplicaThrust(thrust);

      contexto.fillStyle = "black";
      contexto.fillRect(0, 0, anchura, altura);

      // Estrellas en movimiento
      estrellas.forEach(e => { e.mueve(); e.dibuja(); });

      rocas.forEach(r => { r.dibuja(); r.mueve(); });
      balas.forEach(b => { b.dibuja(); b.mueve(); });
      jugador.mueve();
      jugador.dibuja();

      for (let i = rocas.length - 1; i >= 0; i--) {
        const roca = rocas[i];
        if (distancia(jugador.posx, jugador.posy, roca.posx, roca.posy) < roca.radio + 10) {
          jugador.posx = anchura / 2;
          jugador.posy = altura / 2;
          jugador.velx = 0;
          jugador.vely = 0;
          level = 1;
          rocksPerLevel = 4;
          startLevel();
          break;
        }
      }

      for (let i = rocas.length - 1; i >= 0; i--) {
        for (let j = balas.length - 1; j >= 0; j--) {
          if (distancia(balas[j].posx, balas[j].posy, rocas[i].posx, rocas[i].posy) < rocas[i].radio) {
            rocas.splice(i, 1);
            balas.splice(j, 1);
            break;
          }
        }
      }

      for (let j = balas.length - 1; j >= 0; j--) {
        if (balas[j].posx < 0 || balas[j].posx > anchura || balas[j].posy < 0 || balas[j].posy > altura) {
          balas.splice(j, 1);
        }
      }

      if (rocas.length === 0) {
        level++;
        rocksPerLevel *= 2;
        startLevel();
      }

      contexto.fillStyle = "white";
      contexto.font = "16px monospace";
      contexto.fillText(`Level: ${level}`, 12, 22);

      if (levelMessageTimer > 0) {
        contexto.fillStyle = "rgba(255, 255, 255, 0.85)";
        contexto.font = "28px monospace";
        contexto.textAlign = "center";
        contexto.fillText(`Level ${level}`, anchura / 2, altura / 2);
        contexto.textAlign = "left";
        levelMessageTimer--;
      }

      requestAnimationFrame(bucle);
    }

    bucle();
  </script>
</body>

</html>
```

---

## 4. Conclusión breve

Con este ejercicio he comprendido mejor cómo se aplica la física básica en los videojuegos:

- La aceleración define cómo empieza a moverse algo.

- El rozamiento controla cómo se frena.

- La velocidad máxima evita que los objetos se vuelvan incontrolables.

Al modificar estos parámetros se puede hacer que un juego sea más rápido, más difícil o más realista.

---

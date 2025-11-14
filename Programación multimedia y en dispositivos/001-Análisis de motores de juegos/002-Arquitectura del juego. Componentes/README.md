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

---

## 4. Conclusión breve

Con este ejercicio he comprendido mejor cómo se aplica la física básica en los videojuegos:

- La aceleración define cómo empieza a moverse algo.

- El rozamiento controla cómo se frena.

- La velocidad máxima evita que los objetos se vuelvan incontrolables.

Al modificar estos parámetros se puede hacer que un juego sea más rápido, más difícil o más realista.

---

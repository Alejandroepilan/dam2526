# Ejercicio 1 – 001-Animación 2D y 3D

**Autor:** Alejandro Épila  
**Asignatura:** Programación multimedia y en dispositivos  
**Curso:** 2º DAM  
**Fecha:** Noviembre 2025

---

## 1. Introducción breve y contextualización

En este ejercicio se implementa una versión muy sencilla de un juego tipo Pac-Man utilizando HTML5 y JavaScript.

El escenario se dibuja sobre un elemento ``<canvas>`` de 512×512 píxeles y se representa como una cuadrícula de 16×16 casillas. Cada casilla puede ser pared o camino. El personaje del jugador se dibuja como un círculo rojo y se mueve por el laberinto usando las teclas ``w``, ``a``, ``s``, ``d``.

Con este trabajo se ponen en práctica los conceptos de dibujo en canvas, manejo de matrices para representar mapas y captura de eventos de teclado vistos en la unidad.

---

## 2. Desarrollo detallado y preciso

El código define primero las estructuras básicas del juego:

- Una constante ``tam`` que indica el tamaño de cada casilla (32 píxeles).

- Dos variables ``jugadorX`` y ``jugadorY`` que guardan la posición del jugador en coordenadas de celda.

- Una matriz ``mapa`` de 16×16 que contiene los valores del escenario: el valor 1 representa una pared y el valor 5 marca la casilla de aparición del jugador.

Luego la función ``pintarJugador()`` dibuja la posición actual del jugador.
El movimiento se gestiona con ``onkeydown`` según la tecla, se calcula una casilla nueva y solo se actualiza si no es una pared. Después se limpia el canvas y se vuelve a dibujar todo, manteniendo la lógica del movimiento y las colisiones.

---

## 3. Aplicación práctica

El código completo forma un ejemplo autocontenido que se puede abrir directamente en el navegador: basta con guardar el fichero como ``index.html`` y abrirlo. Al cargar la página se dibuja el laberinto negro sobre fondo vacío mediante ``dibujarMapa()``. El jugador aparece en la casilla donde el mapa tiene el valor 5.

El usuario puede interactuar inmediatamente:

- Con ``w`` se intenta mover una casilla hacia arriba.

- Con ``s`` se intenta mover hacia abajo.

- Con ``a`` se intenta mover hacia la izquierda.

- Con ``d`` se intenta mover hacia la derecha.

---

## 4. Conclusión breve

En este ejercicio se usan matrices para modelar escenarios, renderizado de gráficos simples en canvas y gestión de eventos de teclado para controlar un personaje. A partir de esta base es fácil seguir ampliando el proyecto: se pueden añadir enemigos, puntos que recolectar, sistema de puntuación, etc.

---

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

---

## 4. Conclusión breve

Este proyecto me ha servido para entender cómo combinar dibujo en canvas con lógica de juego, movimiento, colisiones y eventos de usuario. Aunque es un juego muy básico, resume bien los conceptos de la unidad: bucle principal, animación, interacción y actualización continua de la escena.

---

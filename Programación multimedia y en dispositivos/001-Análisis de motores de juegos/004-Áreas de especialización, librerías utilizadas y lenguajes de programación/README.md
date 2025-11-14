# Ejercicio 4 - Áreas de especialización, librerías utilizadas y lenguajes de programación

**Autor:** Alejandro Épila  
**Asignatura:** Programación multimedia y en dispositivos  
**Curso:** 2º DAM  
**Fecha:** Noviembre 2025

---

## 1. Introducción breve y contextualización

En esta actividad he utilizado A-Frame, un framework JavaScript que permite crear experiencias de realidad virtual y aumentada usando HTML. En lugar de programar toda la escena en WebGL o Three.js, A-Frame ofrece etiquetas como ``<a-scene>``, ``<a-sphere>`` o ``<a-plane>`` que se escriben directamente en el HTML. 

Esto facilita mucho la creación de modelos 3D, la configuración de materiales, luces y cámaras, y permite visualizar la escena en navegador e incluso en dispositivos VR compatibles.

---

## 2. Desarrollo detallado y preciso

Dentro de ``<a-scene>`` he añadido:

- Una esfera ``<a-sphere>`` posicionada en ``0 1.25 -5`` con radio ``3``.
  
  En el atributo ``material`` he configurado:

  - ``src: nasatierra.jpg`` como textura principal de la esfera.

  - ``metalness: 0.2`` para que no sea totalmente metálica.

  - ``roughness: 0.5`` para que tenga una rugosidad intermedia.

  - ``roughnessMap: rugosidad.jpg`` para usar una imagen como mapa de rugosidad, añadiendo detalles a cómo se refleja la luz.

También he añadido:

- Un cielo ``<a-sky>`` de color negro para que destaque la esfera iluminada.

- Dos luces.

- Una cámara básica con ``look-controls`` para poder mover la vista con el ratón.

---

## 3. Aplicación práctica

Para completar la escena, he añadido un plano ``<a-plane>`` que actúa como suelo:

- La posición ``0 0 -10`` y la rotación ``-90 0 0`` hacen que el plano quede horizontal bajo la esfera, en el fondo de la escena.

- El tamaño ``width="20"`` y ``height="20"`` asegura que el suelo sea suficientemente grande para que se vea desde la cámara.

- El color ``#7BC8A4`` (verde azulado) permite diferenciar claramente el suelo del cielo oscuro y de la esfera texturada.

Al abrir el archivo en el navegador se ve claramente:

- La esfera texturada con la imagen de la Tierra.

- El suelo debajo.

- La iluminación afectando la esfera, mostrando reflejos y rugosidad.

---

## 4. Conclusión breve

Esta actividad me ha servido para practicar cómo aplicar texturas, materiales y luces dentro de A-Frame. Al añadir la textura de la Tierra y un mapa de rugosidad a la esfera, he podido ver cómo A-Frame gestiona estos efectos visuales y cómo la iluminación cambia completamente la apariencia del modelo.

---

# Ejercicio 2 – Librerías de componentes nativas y multiplataforma

**Autor:** Alejandro Épila  
**Asignatura:** Desarrollo de interfaces  
**Curso:** 2º DAM  
**Fecha:** Noviembre 2025

---

## 1. Introducción breve y contextualización

El objetivo del ejercicio es crear un formulario funcional que utilice los siguientes elementos de forma correcta, siguiendo las normas de HTML5 y sin librerías externas.

- ``<form>`` → Contenedor principal que agrupa los elementos del formulario y define cómo se envían los datos.

- ``<input>`` → Permite introducir datos de diferentes tipos (texto, números, rangos, etc.).

- ``<select>`` → Muestra una lista desplegable para seleccionar una opción.

- ``<fieldset>`` y ``<legend>`` → Sirven para agrupar campos relacionados, mejorando la legibilidad y organización.

---

## 2. Desarrollo detallado y preciso

El ejercicio se ha realizado en un archivo llamado ``mi_formulario.html``, en este se incluye un formulario que contiene:

 - Un campo de texto para el nombre.
 - Un control deslizante para la edad, junto con un ``<span>`` que gracias a una función en JS muestra la edad seleccionada.
 - Un desplegable para el país.
 - Un segundo grupo para información de intereses personales.

El código se estructura en dos bloques principales, agrupados con ``<fieldset>`` para diferenciar la información personal de los intereses.

```
<fieldset>
  <legend>Información personal</legend>
  ...

</fieldset>

<fieldset>
  <legend>Intereses personales</legend>
  ...

</fieldset>
```

De esta manera, el formulario resulta más claro y accesible.

---

## 3. Aplicación práctica

Al abrir el archivo ``mi_formulario.html`` en un navegador, se muestra un formulario donde el usuario puede:

1. Introducir su nombre.

2. Seleccionar su edad con el deslizador.

3. Elegir su país en una lista desplegable.

4. Escribir su hobby en el segundo bloque.

El botón ``Enviar`` enviará la información al archivo indicado en el atributo ``action`` (``quienteprocesa.php``).

#### Errores comunes a evitar:

- No incluir los atributos ``name`` en los campos. Sin ellos, los datos no se envían al servidor.

- Colocar los fieldset fuera del ``<form>``.

---

## 4. Conclusión breve

El ejercicio permite comprender la importancia de los formularios en HTML5 y la función de cada elemento:

- ``<form>`` como contenedor principal.

- ``<input>`` para recoger distintos tipos de información.

- ``<select>`` para listas desplegables.

- ``<fieldset>`` y ``<legend>`` para agrupar y dar contexto a los campos relacionados.

La estructura del formulario es simple, accesible y cumple con los estándares del lenguaje.
Además, demuestra cómo HTML5 facilita la creación de interfaces intuitivas.

---

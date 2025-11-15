# Examen final

**Autor:** Alejandro Épila  
**Asignatura:** Desarrollo de interfaces  
**Curso:** 2º DAM  
**Fecha:** Noviembre 2025

---

## 1. Introducción breve y contextualización

- Para esta actividad he desarrollado una minilibreria con cuatro componentes UI básicos utilizando las tecnologias HTML, Tailwind CSS y un poco de JavaScript para las pequeñas funcionalidades.

  - **HTML**: con esta tecnologia he podido crear los esqueletos de los diferentes inputs.
  - **Tailwind CSS**: gracias a esta libreria le he podido añadir estilos a los inputs de una forma cómoda pero muy estética.
  - **JavaScript**: y con esta última tecnologia le he podido dar algo de funcionalidad a algunos de los inputs.

- El objetivo era crear una serie de componentes que fueran reutilizables para crear diferentes formularios e interfaces que se puedan utilizar en aplicaciones de gestión empresarial.

---

## 2. Desarrollo detallado y preciso

### Campo de texto con etiqueta

- Primero creamos un `<div>` que contendrá, un `<label>` y despues un `<input type="text">`.
- Luego simplemente queda añadirle los estilos que se requieran, en este caso los añado en forma de clases ya que es el funcionamiento de la libreria **Tailwind CSS**.

### Campo de texto con icono

- Para este otro componente creamos un `<div>` que contendrá un `<span>` en el que dentro pondremos el icono correspondiente, para la simplicidad del proyecto simplemente he utilizado un emoji. Seguidamente añadimos un `<input type="text">`. Y añadimos los respectivos estilos.

### Selector personalizado

- En este selector creamos un `<div>`, dentro habrá un `<label>` con la etiqueta del campo y un `<button>` para poder desplegar el menú de selección.
- Por último creamos otro `<div>` con la clase `hidden`, la cual hace que esté oculto. Así al hacer click en el botón de selección y mediante **JavaScript** podemos hacer que este se muestre o se oculte al escoger una opción.

### Campo para añadir etiquetas

- Este último campo se crea añadiendo un `<div>` que simplemente contendrá un `<input type="text">` y que al pulsar la tecla **ENTER** después de haber escrito la etiqueta correspondiente, se creará al lado de este.

---

## 3. Aplicación práctica

### HTML y Tailwind CSS

#### 1. Campo de texto sencillo con una etiqueta encima.

```
<div class="space-y-1">
  <label class="text-sm text-gray-300">Nombre</label>
  <input type="text" placeholder="Escribe algo..."
    class="w-full px-3 py-2 rounded-lg bg-gray-800 border border-gray-700 text-sm outline-none focus:border-blue-500" />
  <p class="text-xs text-gray-400">Campo de texto sencillo con label.</p>
</div>
```

#### 2. Campo de texto sencillo con un icono al lado.

```
<div class="space-y-1">
  <label class="text-sm text-gray-300">Correo</label>

  <div class="relative">
    <!-- Icono -->
    <span class="absolute left-3 top-1/2 -translate-y-1/2 text-gray-400 text-sm">
      ✉️
    </span>

    <!-- Input -->
    <input type="text" placeholder="Escribe algo..."
      class="w-full pl-9 pr-3 py-2 rounded-lg bg-gray-800 border border-gray-700 text-sm outline-none focus:border-blue-500" />
  </div>

  <p class="text-xs text-gray-400">Campo de texto con icono delante.</p>
</div>
```

#### 3. Selector de opción con menú personalizado

```
<div class="space-y-1" id="simpleSelect">
  <label class="text-sm text-gray-300">Estado</label>

  <button class="w-full px-3 py-2 rounded-lg bg-gray-800 border border-gray-700 text-sm flex justify-between"
    id="selectTrigger">
    <span id="selectValue">Seleccionar...</span>
    <span>▼</span>
  </button>

  <div class="hidden bg-gray-800 border border-gray-700 rounded-lg mt-1 text-sm" id="selectMenu">
    <button class="block w-full px-3 py-2 text-left hover:bg-gray-700" data-value="Activo">Activo</button>
    <button class="block w-full px-3 py-2 text-left hover:bg-gray-700" data-value="Pendiente">Pendiente</button>
    <button class="block w-full px-3 py-2 text-left hover:bg-gray-700" data-value="Inactivo">Inactivo</button>
  </div>

  <p class="text-xs text-gray-400">Select de estados.</p>
</div>
```

#### 4. Campo para añadir etiquetas.

```
<div class="space-y-1" id="tagInput">
  <label class="text-sm text-gray-300">Etiquetas</label>

  <div class="flex flex-wrap gap-1 p-2 rounded-lg bg-gray-800 border border-gray-700">
    <input id="tagField" type="text" class="bg-transparent outline-none text-sm flex-1"
      placeholder="Pulsa Enter..." />
  </div>

  <p class="text-xs text-gray-400">Escribe y pulsa Enter para añadir una etiqueta.</p>
</div>
```

### JavaScript

- Primero guardamos en constantes las diferentes id de los componentes del selector. Luego al hacer click en el botón muestro u oculto el menú de selección. Para luego recorrer todas las opciones del menú y si se selecciona alguna, cambio el texto del input por la opción seleccionada y por último oculto el menú.

```
// SELECT BASICO

// guardo las referencias a los elementos principales del select
const trigger = document.getElementById("selectTrigger"); // boton que abre o cierra el menu
const menu = document.getElementById("selectMenu");       // el menu con las opciones
const val = document.getElementById("selectValue");       // el texto que muestra la opcion seleccionada

// al hacer click en el boton, muestro u oculto el menu
trigger.onclick = () => menu.classList.toggle("hidden");

// recorro todas las opciones del menu
menu.querySelectorAll("button").forEach(btn => {
  btn.onclick = () => {
    // cuando pulso una opcion, actualizo el texto del select
    val.textContent = btn.dataset.value;

    // cierro el menu despues de elegir
    menu.classList.add("hidden");
  };
});
```

- Primero guardo en una constante la id del input, seguidamente el `<div>` donde se encuentra el input será el que contenga las etiquetas creadas. Luego comprobamos cuando se haya pulsado la tecla **ENTER**, evitamos que haga el salto de línea al haber pulsado dicha tecla y cogemos el texto escrito sin espacios de más. Para luego crear un `<span>` que contenga el texto que se ha escruto en el input. Por último inserto la etiqueta al lado del input y vacío el mismo.

```
// TAG INPUT BASICO

// guardo la referencia del input donde escribo las etiquetas
const tagField = document.getElementById("tagField");

// el padre del input es el contenedor donde iran las etiquetas creadas
const tagBox = tagField.parentElement;

// escucho cuando pulsan una tecla dentro del input de etiquetas
tagField.addEventListener("keydown", (e) => {

  // si pulsan Enter, intento crear una etiqueta
  if (e.key === "Enter") {

    e.preventDefault(); // evito que el Enter haga un salto de linea por defecto

    const text = tagField.value.trim(); // cojo el texto sin espacios de mas
    if (!text) return; // si el texto esta vacio no hago nada

    // creo un elemento span que sera la etiqueta
    const tag = document.createElement("span");
    tag.className = "bg-blue-600 text-xs px-2 py-1 rounded-full"; // estilos basicos
    tag.textContent = text; // le pongo el texto que ha escrito el usuario

    // inserto la etiqueta antes del input para que visualmente quede a su lado
    tagBox.insertBefore(tag, tagField);

    // limpio el input para poder escribir otra etiqueta
    tagField.value = "";
  }
});
```

---

## 4. Conclusión breve

- Esta es una libreria muy simple, pero muy funcional a la vez, ya que nos permite con unas pocas líneas de codigo añadir un componente con muchas partes pero de forma rápida sin tener que vovler a escribir decenas de líneas.

- Estos componentes se podrían mejorar de muchas formas entre ellas, añadir validaciones a los inputs antes de mandar los datos, de esta forma poder introdcuir mensajes de error o validación y también se podrían crear bastantes mas componetes reutilizables.

---

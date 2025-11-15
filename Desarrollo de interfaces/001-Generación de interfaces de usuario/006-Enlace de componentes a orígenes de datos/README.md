# Ejercicio 6 - Enlace de componentes a orígenes de datos

**Autor:** Alejandro Épila  
**Asignatura:** Desarrollo de interfaces  
**Curso:** 2º DAM  
**Fecha:** Noviembre 2025

---

## 1. Introducción breve y contextualización

En este ejercicio he trabajado con datos en formato JSON para mostrarlos dinámicamente en una tabla HTML. Esto sigue el trabajo previo realizado en clase sobre cómo manejar arrays de objetos con JavaScript y cómo generar contenido HTML desde código. El objetivo es aprender a poblar una interfaz con datos reales y añadir una columna adicional relacionada con una mecánica de taller.

---

## 2. Desarrollo detallado y preciso

Primero he creado un array JSON con varios clientes, cada uno con nombre, coche y teléfono. Después he definido una variable ``mecanica_usada`` que representa el trabajo realizado en un taller. Para generar la tabla he usado el método forEach, creando filas ``<tr>`` y celdas ``<td>`` mediante ``document.createElement``. Cada cliente se añade como una nueva fila en el ``<tbody>``, incluyendo la columna extra donde se muestra la mecánica usada. Todo el código está escrito con JavaScript básico, sin librerías externas.

---

## 3. Aplicación práctica

El resultado final muestra una tabla completa con los datos de los clientes y la mecánica aplicada. Esta estructura se puede usar en un panel de gestión de talleres para listar clientes y los trabajos realizados recientemente. El ejercicio demuestra cómo pasar de datos JSON a una representación visual, algo muy común en aplicaciones empresariales.

#### ``004-poblar datos con mecánica.html``

```
<!doctype html>
<html lang="es">

<head>
  <meta charset="utf-8">
  <title>004 - Poblar datos con mecanica</title>
  <style>
    body {
      font-family: system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
      background: #0f172a;
      color: #e5e7eb;
      padding: 20px;
    }

    h1 {
      font-size: 20px;
      margin-bottom: 12px;
    }

    table {
      border-collapse: collapse;
      width: 100%;
      max-width: 800px;
      background: #020617;
      border: 1px solid #1f2937;
    }

    th,
    td {
      border: 1px solid #1f2937;
      padding: 6px 10px;
      font-size: 14px;
      text-align: left;
    }

    th {
      background: #111827;
    }

    tbody tr:nth-child(even) {
      background: #020617;
    }

    tbody tr:nth-child(odd) {
      background: #020617;
    }
  </style>
</head>

<body>

  <h1>Listado de clientes con mecanica usada</h1>

  <table id="tablaClientes">
    <thead>
      <tr>
        <th>Nombre</th>
        <th>Coche</th>
        <th>Telefono</th>
        <th>Mecanica usada</th>
      </tr>
    </thead>
    <tbody>
      <!-- aqui se rellenan las filas con JS -->
    </tbody>
  </table>

  <script>
    // array JSON de clientes (ejemplo sencillo)
    const clientes = [
      { nombre: "Taller Pepito", coche: "Golf 1.9 TDI", telefono: "600123123" },
      { nombre: "Juan Garcia", coche: "BMW 320d", telefono: "611222333" },
      { nombre: "Autos Valencia", coche: "Clio 1.2", telefono: "699888777" }
    ];

    // variable de mecanica usada, algo relacionado con el taller
    const mecanica_usada = "Cambio de aceite y revision basica";

    // referencia a la tabla
    const tabla = document.getElementById("tablaClientes").querySelector("tbody");

    // recorro el array de clientes y creo una fila por cada uno
    clientes.forEach(cliente => {
      const fila = document.createElement("tr");

      // nombre
      const tdNombre = document.createElement("td");
      tdNombre.textContent = cliente.nombre;
      fila.appendChild(tdNombre);

      // coche
      const tdCoche = document.createElement("td");
      tdCoche.textContent = cliente.coche;
      fila.appendChild(tdCoche);

      // telefono
      const tdTelefono = document.createElement("td");
      tdTelefono.textContent = cliente.telefono;
      fila.appendChild(tdTelefono);

      // mecanica usada (misma variable para todos, a modo de ejemplo)
      const tdMecanica = document.createElement("td");
      tdMecanica.textContent = mecanica_usada;
      fila.appendChild(tdMecanica);

      // añado la fila completa al cuerpo de la tabla
      tabla.appendChild(fila);
    });
  </script>

</body>

</html>
```

---

## 4. Conclusión breve

La actividad me ha permitido reforzar el uso de JSON, la manipulación del DOM y la generación dinámica de tablas. También he añadido una variable externa al JSON para ampliar la información visualizada. Este tipo de ejercicios ayuda a entender cómo funcionan las interfaces que muestran datos reales en tiempo real, conectando directamente con los contenidos de la unidad sobre JavaScript y estructuras de datos.

---

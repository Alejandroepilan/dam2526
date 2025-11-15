# Ejercicio 8 – Sincronización entre procesos

**Autor:** Alejandro Épila  
**Asignatura:** Programación de procesos y servicios  
**Curso:** 2º DAM  
**Fecha:** Noviembre 2025

---

## 1. Introducción breve y contextualización

En esta actividad se desarrolla un pequeño sistema de gestión de libros para una biblioteca digital usando programación orientada a objetos.

El objetivo es simular un caso real en el que una biblioteca necesita:

- Registrar libros nuevos.

- Buscar libros por título o autor.

- Listar todos los libros disponibles.

---

## 2. Desarrollo detallado y preciso

Se define una clase ``Libro`` que representa el modelo de datos principal. Tiene tres atributos básicos:

- ``titulo``

- ``autor``

- ``isbn``

La clase ``Biblioteca`` se encarga de gestionar una colección de libros. Internamente utiliza una lista para almacenarlos:

- ``self.libros``: lista de objetos Libro.

Métodos implementados:

- ``agregar_libro(libro)``: añade un nuevo libro a la colección.

- ``buscar_por_titulo(titulo)``: busca libros cuyo título contenga el texto introducido (búsqueda parcial y sin distinguir mayúsculas/minúsculas).

- ``buscar_por_autor(autor)``: igual que la anterior, pero por autor.

- ``listar_libros()``: muestra todos los libros registrados.

Se ha desarrollado una interfaz sencilla basada en un menú por consola, este permite al usuario:

1. Añadir libro.
2. Buscar libro por título.
3. Buscar libro por autor.
4. Listar todos los libros.
5. Salir.

El programa se ejecuta en un bucle ``while`` hasta que el usuario elige la opción de salir.

---

## 3. Aplicación práctica

A continuación se muestra un ejemplo de ejecución del programa simulando el uso por parte de un usuario.

#### Ejemplo 1: Añadir un libro

```
Bienvenido a la Biblioteca Digital
1. Añadir Libro
2. Buscar Libro por Título
3. Buscar Libro por Autor
4. Listar Todos los Libros
5. Salir

Elige una opción: 1
Ingresa el título del libro: libro1
Ingresa el autor del libro: autor1
Ingresa el ISBN del libro: 1234

Libro añadido con éxito.
```

#### Ejemplo 2: Buscar por título

```
Elige una opción: 3
Introduce parte o todo el autor a buscar: 1

Resultados encontrados:
Título: libro1, Autor: autor1, ISBN: 1234
```

#### Ejemplo 3: Listar todos los libros

```
Elige una opción: 4

--- Lista de Libros ---
Título: libro1, Autor: autor1, ISBN: 1234
```

#### ``libro.py``

```
class Libro:
  def __init__(self, titulo, autor, isbn):
    self.titulo = titulo
    self.autor = autor
    self.isbn = isbn

  def __str__(self): # Se usa para representar el libro como una cadena
    return f"Titulo: {self.titulo}, Autor: {self.autor}, ISBN: {self.isbn}"
```

#### ``biblioteca.py``

```
from libro import Libro

class Biblioteca:
  def __init__(self):
    self.libros = []

  def agregar_libro(self, libro):
    self.libros.append(libro)
    print("\nLibro añadido con exito.\n")

  def buscar_por_titulo(self, titulo):
    return [libro for libro in self.libros if titulo.lower() in libro.titulo.lower()]

  def buscar_por_autor(self, autor):
    return [libro for libro in self.libros if autor.lower() in libro.autor.lower()]

  def listar_libros(self):
    if not self.libros:
      print("\nNo hay libros en la biblioteca.\n")
    else:
      print("\n--- Lista de libros ---")
      for libro in self.libros:
        print(libro)
      print()
```

#### ``main.py``

```
from biblioteca import Biblioteca
from libro import Libro

def menu():
  biblioteca = Biblioteca()

  while True:
    print("Bienvenido a la Biblioteca Digital")
    print("1. Añadir libro")
    print("2. Buscar libro por titulo")
    print("3. Buscar libro por autor")
    print("4. Listar todos los libros")
    print("5. Salir")

    opcion = input("\nElige una opcion: ")

    if opcion == "1":
      titulo = input("Ingresa el titulo del libro: ")
      autor = input("Ingresa el autor del libro: ")
      isbn = input("Ingresa el ISBN del libro: ")
      libro = Libro(titulo, autor, isbn)
      biblioteca.agregar_libro(libro)

    elif opcion == "2":
      titulo = input("Introduce parte o todo el titulo a buscar: ")
      resultados = biblioteca.buscar_por_titulo(titulo)
      if resultados:
        print("\nResultados encontrados:")
        for libro in resultados:
          print(libro)
        print()
      else:
        print("\nNo se encontraron libros con ese titulo.\n")

    elif opcion == "3":
      autor = input("Introduce parte o todo el autor a buscar: ")
      resultados = biblioteca.buscar_por_autor(autor)
      if resultados:
        print("\nResultados encontrados:")
        for libro in resultados:
          print(libro)
        print()
      else:
        print("\nNo se encontraron libros de ese autor.\n")

    elif opcion == "4":
      biblioteca.listar_libros()

    elif opcion == "5":
      print("¡Gracias por usar la biblioteca digital!")
      break

    else:
      print("\nOpcion no valida. Intentalo de nuevo.\n")

if __name__ == "__main__":
  menu()
```

---

## 4. Conclusión breve

Este ejercicio permite aplicar de forma práctica los conceptos fundamentales de la programación orientada a objetos trabajados en la unidad:

- **Clases y objetos:** se han definido las clases ``Libro`` y Biblioteca como modelos del mundo real.

- **Encapsulación de datos y comportamiento:** cada clase agrupa sus atributos y métodos relacionados.

- **Estructuras de datos:** se ha utilizado una lista para almacenar múltiples objetos ``Libro``.

- **Algoritmos simples de búsqueda:** se han aplicado búsquedas lineales con coincidencia parcial sobre la lista de libros.

- **Interacción con el usuario:** mediante un menú por consola que simula una interfaz sencilla de un sistema real de gestión.

---

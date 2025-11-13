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

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

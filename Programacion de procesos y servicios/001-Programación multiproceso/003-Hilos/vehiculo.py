from datetime import date

class Vehiculo:
  def __init__(self, marca: str = "", modelo: str = "", anio_fabricacion: int = 0):
    self.__marca = marca
    self.__modelo = modelo
    self.__anio_fabricacion = anio_fabricacion
    self.__historial = "" # Historial como texto plano

  def set_marca(self, marca: str) -> None:
    self.__marca = marca

  def get_marca(self) -> str:
    return self.__marca

  def set_modelo(self, modelo: str) -> None:
    self.__modelo = modelo

  def get_modelo(self) -> str:
    return self.__modelo

  def set_anio_fabricacion(self, anio: int) -> None:
    self.__anio_fabricacion = anio

  def get_anio_fabricacion(self) -> int:
    return self.__anio_fabricacion

  def get_historial(self) -> str:
    return self.__historial

  def add_reparacion(self, concepto: str, fecha: str = None, coste: float = None) -> None:
    # Añade una reparacion al historial como linea de texto.
    # - fecha: 'YYYY-MM-DD' (opcional). Si no se pasa, usa hoy.
    # - coste: numero opcional.
    f = fecha if fecha else str(date.today())
    linea = f"[REPARACION] {f} – {concepto}"
    if coste is not None:
      linea += f" – coste: {coste:.2f}€"
    self.__historial += linea + "\n"

  def add_mantenimiento(self, concepto: str, fecha: str = None, km: int = None) -> None:
    # Añade un mantenimiento al historial como linea de texto.
    # - fecha: 'YYYY-MM-DD' (opcional). Si no se pasa, usa hoy.
    # - km: kilometraje opcional.
    f = fecha if fecha else str(date.today())
    linea = f"[MANTENIMIENTO] {f} – {concepto}"
    if km is not None:
      linea += f" – km: {km}"
    self.__historial += linea + "\n"

  def mostrar_detalles(self) -> str:
    #Devuelve un texto con todos los detalles.
    detalles = (
      f"Marca: {self.__marca}\n"
      f"Modelo: {self.__modelo}\n"
      f"Año: {self.__anio_fabricacion}\n"
      "Historial:\n"
    )
    # Si no hay historial, lo indicamos.
    if self.__historial == "":
      return detalles + "(sin entradas)\n"
    return detalles + self.__historial

from vehiculo import Vehiculo

coche = Vehiculo("BMW", "E36 325i", 1992)


# Establecer y obtener atributos
coche.set_marca("BMW")
coche.set_modelo("E36 325i")
coche.set_anio_fabricacion(1992)

print(coche.get_marca(), coche.get_modelo(), coche.get_anio_fabricacion())
print("-------------------------------------------")

# Añadir entradas al historial
coche.add_reparacion("Cambio bomba de agua", fecha="2025-11-10", coste=220.0)
coche.add_mantenimiento("Cambio de aceite 5W40", fecha="2025-11-12", km=245000)


coche.add_reparacion("Cambio alternador", coste=150.0)
coche.add_mantenimiento("Cambio de aceite 5W40", km=270000)

print(coche.mostrar_detalles())
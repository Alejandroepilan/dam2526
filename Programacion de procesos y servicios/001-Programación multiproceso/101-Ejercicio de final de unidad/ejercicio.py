import time
from multiprocessing import Pool, cpu_count


def simular_pieza(args):
    """
    Simula el cálculo pesado para una pieza mecánica.
    En un caso real podría ser una simulación física.
    Aquí usamos una operación numérica costosa como ejemplo.
    """
    nombre_pieza, complejidad = args

    acumulador = 0
    # Bucle "pesado" para simular carga de CPU
    for i in range(complejidad):
        acumulador += (i * i) % 97  # operación tonta pero costosa

    # Devolvemos el resultado junto con el nombre de la pieza
    return nombre_pieza, acumulador


def ejecutar_secuencial(piezas):
    print("=== Ejecución secuencial ===")
    inicio = time.time()

    resultados = []
    for pieza in piezas:
        resultado = simular_pieza(pieza)
        resultados.append(resultado)

    fin = time.time()
    tiempo_total = fin - inicio

    for nombre, valor in resultados:
        print(f"Pieza: {nombre:15s} | Resultado simulación: {valor}")

    print(f"\nTiempo total (secuencial): {tiempo_total:.2f} segundos\n")
    return tiempo_total


def ejecutar_en_paralelo(piezas):
    print("=== Ejecución en paralelo (multiproceso) ===")
    inicio = time.time()

    # Número de procesos = núcleos disponibles
    num_procesos = cpu_count()
    print(f"Usando {num_procesos} procesos en paralelo.\n")

    with Pool(processes=num_procesos) as pool:
        resultados = pool.map(simular_pieza, piezas)

    fin = time.time()
    tiempo_total = fin - inicio

    for nombre, valor in resultados:
        print(f"Pieza: {nombre:15s} | Resultado simulación: {valor}")

    print(f"\nTiempo total (paralelo): {tiempo_total:.2f} segundos\n")
    return tiempo_total


def main():
    # Lista de piezas mecánicas (nombre, complejidad)
    # Complejidad controla las iteraciones: cuanto más grande, más tarda
    piezas = [
        ("Biela", 300_000_00),
        ("Cigüeñal", 290_000_00),
        ("Pistón", 270_000_00),
        ("Disco de freno", 160_000_00),
        ("Válvula", 300_000_00),
    ]

    print("Simulación de piezas mecánicas con programación multiproceso\n")

    # 1) Modo secuencial
    tiempo_secuencial = ejecutar_secuencial(piezas)

    # 2) Modo paralelo
    tiempo_paralelo = ejecutar_en_paralelo(piezas)

    # 3) Comparativa
    if tiempo_paralelo > 0:
        mejora = tiempo_secuencial / tiempo_paralelo
    else:
        mejora = 0

    print("=== Comparativa final ===")
    print(f"Tiempo secuencial: {tiempo_secuencial:.2f} s")
    print(f"Tiempo paralelo:  {tiempo_paralelo:.2f} s")
    print(f"Factor de mejora aproximado: x{mejora:.2f}")


if __name__ == "__main__":
    main()

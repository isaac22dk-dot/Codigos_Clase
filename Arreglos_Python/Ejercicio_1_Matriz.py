def calcular_promedio_matriz():
    print("=== PROMEDIO DE UNA MATRIZ ===")
    filas = int(input("Escriba un numero de filas: "))
    columnas = int(input("Escriba un numero de columnas: "))
    suma_total = 0
    matriz = []

    for f in range(filas):
        fila_temporal = []
        for c in range(columnas):
            valor = float(input(f"Ingrese valor para posicion [{f+1},{c+1}]: "))
            fila_temporal.append(valor)
            suma_total += valor 
            
        matriz.append(fila_temporal)

    total_elementos = filas * columnas

    if total_elementos > 0:
        promedio = suma_total / total_elementos
        print(f"Promedio={promedio}")
    else:
        print("No se puede calcular el promedio (matriz vacía).")

if __name__ == "__main__":
    calcular_promedio_matriz()
import random
def Personal_Matriz():
    print("CREACION DE LA MATRIZ")
    filas = int(input("Ingrese el numero de filas -> "))
    columnas = int(input("Ingrese el numero de columnas -> "))
    matriz = []
    for f in range(filas):
        fila_temporal = []
        for c in range(columnas):
            numero = random.randint(0, 9)
            fila_temporal.append(numero)
        matriz.append(fila_temporal)
    print("Matriz creada! (Aun sin mostrar)")
    Opc = -1
    while Opc != 5:
        print("--------------------------------------------------")
        print("Opc. 1 -> Buscar si hay (x) numero en la matriz y cuantas veces aparece")
        print("Opc. 2 -> Calcular la suma de todos los numeros de la matriz")
        print("Opc. 3 -> Calcular la moda de la matriz")
        print("Opc. 4 -> Mostrar la matriz")
        print("Opc. 5 -> Salir")
        Opc = int(input(("Seleccione lo que quiere hacer: ")))
        print("--------------------------------------------------")
        match Opc:
            case 1:
                buscar = int(input("Ingrese el numero que quiere buscar: "))
                conteo = 0
                for f in range(filas):
                    for c in range(columnas):
                        if matriz[f][c] == buscar:
                            conteo += 1
                if conteo == 0:
                    print(f"El numero {buscar} no se encuentra en la matriz.")
                else:
                    print(f"El numero {buscar} si esta y aparece {conteo} veces.")
            case 2:
                suma = 0
                for f in range(filas):
                    for c in range(columnas):
                        suma += matriz[f][c]
                print(f"La suma de todos los numeros en la matriz es: {suma}")
            case 3:
                todos = []
                for fila in matriz:
                    for valor in fila:
                        todos.append(valor)
                moda = todos[0]
                mayor_conteo = 0
                for num in todos:
                    conteo = todos.count(num)
                    if conteo > mayor_conteo:
                        mayor_conteo = conteo
                        moda = num
                if mayor_conteo == 1:
                    print("No hay moda (todos los valores aparecen una sola vez)")
                else:
                    print(f"La moda es: {moda} (aparece {mayor_conteo} veces)")
            case 4:
                print("MATRIZ")
                for f in range(filas):
                    for c in range(columnas):
                        print(f"{matriz[f][c]}", end="  ")
                    print()
Personal_Matriz()
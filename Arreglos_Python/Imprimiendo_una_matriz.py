#Creación de una matriz 3x3 dinámica
matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

#Recorrido clásico por indices,
#len(matriz)=Numero de filas(3), len(matriz[0])=Numero de elementos en la fila 1 (3)

for f in range(len(matriz)):
    for c in range(len(matriz[0])):
        print(f"Posicion [{f}] [{c}] (matriz [{f}][{c}])")
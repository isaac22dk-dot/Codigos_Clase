import random

class MatrizDinamica:
    def __init__(self, filas: int, columnas: int):
        self.filas = filas
        self.columnas = columnas
        self.matriz = []

    def llenar_matriz(self):
        for f in range(self.filas):
            fila_temporal = []
            for c in range(self.columnas):
                numero = random.randint(0, 5)
                fila_temporal.append(numero)
            self.matriz.append(fila_temporal)

    def mostrar_matriz(self):
        for f in range(self.filas):
            for c in range(self.columnas):
                print(f"{self.matriz[f][c]}", end="  ")
            print()

def ejecutar_ejemplo_aleatorio():
    print("=== CONFIGURACION DEL PANEL ===")
    f = int(input("Ingrese el numero de filas: "))
    c = int(input("Ingrese el numero de columnas: "))

    mi_matriz = MatrizDinamica(f, c)
    mi_matriz.llenar_matriz()

    print("--- Estado del panel de Nodos ---")
    mi_matriz.mostrar_matriz()

    print("--- Diagnostico ---")

    nodos = 0
    for fila in mi_matriz.matriz:
    
        nodos += sum(1 for valor in fila if valor == 0)
        
    print(f"ALERTA: Se detectaron {nodos} nodos(s) fuera de linea (Valor 0)")

if __name__ == "__main__":
    ejecutar_ejemplo_aleatorio()
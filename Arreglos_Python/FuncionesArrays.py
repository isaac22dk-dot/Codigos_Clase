datos = [10,20,30]
print(datos)
print(f" Longitud del arreglo: {len(datos)}")
print(f" Valor minimo del arreglo: {min(datos)}")
print(f" Valor maximo del arreglo: {max(datos)}")
print(f" Suma de los valores del arreglo: {sum(datos)}")

print("---------------------------------------------------------")

nombres = ["Juan", "Maria"]
nombres.append("Jesus")

nombres.insert(1, "Panfilo")
print(nombres)

extraido = nombres.pop(1)
print(extraido)
print(nombres)

nombres.remove("Jesus")
print(nombres)

print("---------------------------------------------------------")

valores = [4, 2, 1, 7]
valores.sort()
print(valores)
valores.sort(reverse=True)
print(valores)

colores = ["rojo", "verde", "azul"]
posicion = colores.index("verde")
print(posicion)

votos = ["a", "b", "b", "c", "d"]
total_b = votos.count("b")
print(total_b)

print("---------------------------------------------------------")

A = [2, 5, 8, 100, 1, 2, 100, 5, 5, 5]
for i in range(len(A)):
    print(f"La posicion {i} tiene valor {A[i]}")

print("---------------------------------------------------------")

resultado = 0
A = [2, 5, 8, 100, 1, 2, 100, 5, 5, 5] 
for i in A: 
    print(f"{i} ", end="")
    resultado += i
print(f"La suma de los valores del arreglo es: {resultado}")
print(f"Y el promedio es de: {resultado / len(A)}")
moda = max(A, key=A.count)
print(f"La moda del arreglo es: {moda}")

print("---------------------------------------------------------")

#A = [0] * 5 
#print("Introduce 5 valores:")  
#for i in range(5): 
#    A[i] = int(input()) 

#print("valores del arreglo")
#for i in range(5): 
#    print(A[i])

#print("---------------------------------------------------------")

cantidad = int(input("Introduce la cantidad de tiempos que quieres ingresar:"))
A = [0] * cantidad
print(f"Introduce {cantidad} tiempos de respuesta (m/s): ")

for i in range(cantidad): 
    A[i] = int(input()) 

print("valores del arreglo")
for i in range(cantidad): 
    print(f"Tiempo {i+1}: {A[i]}")

print(f" Pico de latencia (Maximo): {min(A)}")
print(f" Tiempo de respuesta mas bajo (Minimo): {max(A)}")

print(f" Promedio de respuesta: {sum(A)/len(A)} m/s")

Conteo = [0] * len(A)
moda = 0
mayor = 0
for i in range(len(A)):
    Conteo[i] = A.count(A[i])
    if Conteo[i] > mayor:
        mayor = Conteo[i]
        moda = A[i]
print(f" La moda del arreglo es: {moda} y se repite {mayor} veces")

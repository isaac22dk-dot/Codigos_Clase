b = 0 
c = [1, 2, 3, 4, 5, 6, 7, 8, 9, 8] 

for a in range(10):
    if c[a] % 2 == 0: #El operador % devuelve el residuo de la division, si es 0 es par
        b += c[a] #Este hace que b vaya sumando los valores pares de c

print(b) #Nos da el resultado de la suma de los valores pares del arreglo c

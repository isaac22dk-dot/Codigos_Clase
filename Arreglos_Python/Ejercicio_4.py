numeros = [5, 2, 8, 7, 0, 3] 
izq = 0 
der = 5 

while izq <= der: 
    numeros[der] = numeros[izq] 
    izq += 1 
    der -= 1 

print(numeros)

#Resultado [5, 2, 8, 8, 2, 5]
from Implementacion_TDA_Natural import Natural

def main():

    obj = Natural()
    opcion = -1

    while opcion != 5:
        print("Menu para la implementacion del TDA Natural")
        print("Opcion 1: Sucesion")
        print("Opcion 2: Suma")
        print("Opcion 3: Producto")
        print("Opcion 4: Comparacion")
        print("Opcion 5: Salir")
        try:
            opcion = int(input("Ingrese una opcion: "))
            match opcion:
                case 1:
                    numero = int(input("Ingrese un numero: "))
                    resultado = obj.sucesion(numero)
                    print(f"El sucesor de {numero} es {resultado}")
                    
                case 2:
                    numero1 = int(input("Ingrese el primer numero: "))
                    numero2 = int(input("Ingrese el segundo numero: "))
                    resultado = obj.suma(numero1, numero2)
                    print(f"La suma de {numero1} y {numero2} es {resultado}")
                    
                case 3:
                    numero1 = int(input("Ingrese el primer numero: "))
                    numero2 = int(input("Ingrese el segundo numero: "))
                    resultado = obj.producto(numero1, numero2)
                    print(f"El producto de {numero1} y {numero2} es {resultado}")

                case 4:
                    numero1 = int(input("Ingrese el primer numero: "))
                    numero2 = int(input("Ingrese el segundo numero: "))
                    resultado = obj.comparacion(numero1, numero2)
                    print(f"La comparacion de {numero1} y {numero2} es {resultado}")
                    if resultado:
                        print(f"{numero1} es igual a {numero2}")
                    else:
                        print(f"{numero1} no es igual a {numero2}")
                case 5:
                    print("Saliendo del programa...")
                case _:
                    print("Opcion invalida. Por favor, ingrese un numero entre 1 y 5.")

        except ValueError:
            print("Opcion invalida. Por favor, ingrese un numero entero.")
main()


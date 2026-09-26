from TAD_Cadena import Cadena

def main():
    obj = Cadena()
    opcion = -1

    while opcion != 5:
        print("Menu")
        print("Opcion (1) Concatenar")
        print("Opcion (2) Longitud")
        print("Opcion (3) Vacia")
        print("Opcion (4) Son iguales")
        print("Opcion (5) Salir")
        try:
            opcion = int(input("Ingrese una opcion: "))
            match opcion:
                case 1:
                    cadena1 = input("Ingrese la primera cadena: ")
                    cadena2 = input("Ingrese la segunda cadena: ")
                    obj.concatenar(cadena1, cadena2)
                    
                case 2:
                    cadena = input("Ingrese una cadena: ")
                    resultado = obj.longitud(cadena)
                    print(f"La longitud de la cadena es: {resultado}")
                case 3:
                    cadena = input("Ingrese una cadena: ")
                    resultado = obj.es_vacia(cadena)
                    if resultado:
                        print("La cadena esta vacia")
                    else:
                        print("La cadena no esta vacia")
                case 4:
                    cadena1 = input("Ingrese la primera cadena: ")
                    cadena2 = input("Ingrese la segunda cadena: ")
                    resultado = obj.son_iguales(cadena1, cadena2)
                    if resultado:
                        print("Las cadenas son iguales")
                    else:
                        print("Las cadenas no son iguales")
                case 5:
                    print("Saliendo del programa...")
                case _:
                    print("Opcion invalida. Por favor, ingrese un numero entre 1 y 5.")
        except ValueError:
            print("Opcion invalida. Por favor, ingrese un numero entero.")
main()   

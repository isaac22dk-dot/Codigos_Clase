from Ejemplos_Recursivos import Recursividad


def main():
    obj = Recursividad()
    opcion = -1
    while opcion != 9:
        print("\nMenu")
        print("Opcion (1) Factorial iterativo")
        print("Opcion (2) Factorial recursivo")
        print("Opcion (3) Fibonacci recursivo")
        print("Opcion (4) Fibonacci iterativo")
        print("Opcion (5) Imprimir")
        print("Opcion (6) Imprimir descendente")
        print("Opcion (7) Imprimir ascendente")
        print("Opcion (8) Invertir cadena")
        print("Opcion (9) Ecuacion recurrente")
        print("Opcion (10) Salir")
        opcion = int(input("Seleccione una opcion: "))

        match opcion:
            case 1:
                n = int(input("Ingrese el caso: "))
                print(obj.factorial_iterativo(n))
            case 2:
                n = int(input("Ingrese el caso: "))
                print(obj.factorial_recursivo(n))
            case 3:
                n = int(input("Ingrese el caso: "))
                print(obj.fibonacci_rec(n))
            case 4:
                n = int(input("Ingrese el caso: "))
                print(obj.fibonacci_iter(n))
            case 5:
                n = int(input("Ingrese el caso: "))
                obj.imprimir(n)
            case 6:
                n = int(input("Ingrese el caso: "))
                obj.imprimir_descendente(n)
            case 7:
                n = int(input("Ingrese el caso: "))
                obj.imprimir_ascendente(n)
            case 8:
                palabra = input("Introduce una palabra: ")
                print("Palabra invertida:", obj.invertir_cadena(palabra))
            case 9:
                n = int(input("Ingrese el caso: "))
                print(obj.ecuacion_recurrente(n))
            case 10:
                print("Saliendo del programa...")
            case _:
                print("Opcion no valida")


if __name__ == "__main__":
    main()
from TAD_Valores_Reales import Valores_Reales

def main():
    obj = Valores_Reales()
    opcion = -1
    while opcion != 5:
        print("Menu")
        print("Opcion (1) Division")
        print("Opcion (2) Raiz cuadrada")
        print("Opcion (3) Complejo")
        print("Opcion (4) Comparacion")
        print("Opcion (5) Salir")
        try:
            opcion = int(input("Ingrese una opcion: "))
            match opcion:
                case 1:
                    numero1 = float(input("Ingrese el primer numero: "))
                    numero2 = float(input("Ingrese el segundo numero: "))
                    resultado = obj.division(numero1, numero2)
                    print(f"Resultado: {resultado}")
                case 2:
                    numero = float(input("Ingrese un numero: "))
                    resultado = obj.raiz_cuadrada(numero)
                    print(f"Resultado: {resultado}")
                case 3:
                    numero1 = float(input("Ingrese el primer numero: "))
                    numero2 = float(input("Ingrese el segundo numero: "))
                    resultado = obj.complexion(numero1, numero2)
                    print(f"Resultado: {resultado}")
                case 4:
                    numero1 = float(input("Ingrese el primer numero: "))
                    numero2 = float(input("Ingrese el segundo numero: "))
                    resultado = obj.comparacion(numero1, numero2)
                    print(f"Resultado: {resultado}")
                case 5:
                    print("Saliendo del programa...")
                case _:
                    print("Opcion invalida. Por favor, ingrese un numero entre 1 y 5.")
        except ValueError:
            print("Opcion invalida. Por favor, ingrese un numero entero.")
main()   
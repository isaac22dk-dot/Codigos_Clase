from TAD_Natural import NaturalTAD

def main():
    obj = NaturalTAD()
    opcion = -1
    while opcion != 5:
        print("Menu")
        print("Opcion (1) Menor o igual")
        print("Opcion (2) Menor")
        print("Opcion (3) Mayor")
        print("Opcion (4) Mayor o igual")
        print("Opcion (5) Salir")
        try:
            opcion = int(input("Ingrese una opcion: "))
            match opcion:
                case 1:
                    numero1 = int(input("Ingrese el primer numero: "))
                    numero2 = int(input("Ingrese el segundo numero: "))
                    resultado = obj.menorigual(numero1, numero2)
                    print(f"Es menor o igual: {resultado}")
                case 2:
                    numero1 = int(input("Ingrese el primer numero: "))
                    numero2 = int(input("Ingrese el segundo numero: "))
                    resultado = obj.menor(numero1, numero2)
                    print(f"Es menor: {resultado}")
                case 3:
                    numero1 = int(input("Ingrese el primer numero: "))
                    numero2 = int(input("Ingrese el segundo numero: "))
                    resultado = obj.mayor(numero1, numero2)
                    print(f"Es mayor: {resultado}")
                case 4:
                    numero1 = int(input("Ingrese el primer numero: "))
                    numero2 = int(input("Ingrese el segundo numero: "))
                    resultado = obj.mayorigual(numero1, numero2)
                    print(f"Es mayor o igual: {resultado}")
                case 5:
                    print("Saliendo del programa...")
                case _:
                    print("Opcion invalida. Por favor, ingrese un numero entre 1 y 5.")

        except ValueError:
            print("Opcion invalida. Por favor, ingrese un numero entero.")
main()   
        

from Lista_enlazada import ListaEnlazada

if __name__ == "__main__":
    lista1 = ListaEnlazada()
    op = -1

    while op != 0:
        print("\n---_Operaciones sobre listas ligadas_---: ")
        print("1. Crear lista")
        print("2. Mostrar lista")
        print("4. Insertar elemento al inicio")
        print("5. Insertar elemento al final")
        print("0. Salir")
        print("   ")
        op = int(input("Elige una opcion: "))

        match op:
                case 1:
                    lista1.crear_lista()
                case 2:
                    lista1.mostrar_lista()
                case 4:
                    dato = int(input("Introduce el elemento a insertar al inicio: "))
                    lista1.insertar_inicio(dato)
                case 5:
                    dato = int(input("Introduce el elemento a insertar al final: "))
                    lista1.insertar_final(dato)
                case 0:
                    print("Adios")
                case _:
                    print("Opción no válida")

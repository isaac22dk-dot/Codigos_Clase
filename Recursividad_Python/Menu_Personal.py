from Personal import ListaCompras


def main():
    obj = ListaCompras()
    lista = []
    opcion = -1
    while opcion != 8:
        print("\nLista de compras")
        print("Opcion (1) Agregar producto")
        print("Opcion (2) Mostrar productos")
        print("Opcion (3) Mostrar productos al reves")
        print("Opcion (4) Contar productos")
        print("Opcion (5) Buscar producto")
        print("Opcion (6) Mostrar lista numerada")
        print("Opcion (7) Eliminar producto")
        print("Opcion (8) Salir")
        opcion = int(input("Seleccione una opcion: "))

        match opcion:
            case 1:
                producto = input("Producto a agregar: ").lower()
                lista.append(producto)
                print("Agregado.")
            case 2:
                if len(lista) == 0:
                    print("La lista esta vacia.")
                else:
                    obj.mostrar_productos(lista)
            case 3:
                if len(lista) == 0:
                    print("La lista esta vacia.")
                else:
                    obj.mostrar_al_reves(lista)
            case 4:
                print("Total de productos:", obj.contar_productos(lista))
            case 5:
                producto = input("Producto a buscar: ").lower()
                if obj.buscar_producto(lista, producto):
                    print("Si esta en la lista.")
                else:
                    print("No esta en la lista.")
            case 6:
                if len(lista) == 0:
                    print("La lista esta vacia.")
                else:
                    obj.mostrar_numerado(lista)
            case 7:
                producto = input("Producto a eliminar: ").lower()
                if obj.buscar_producto(lista, producto):
                    lista = obj.eliminar_producto(lista, producto)
                    print("Eliminado.")
                else:
                    print("Ese producto no esta en la lista.")
            case 8:
                print("Saliendo...")
            case _:
                print("Opcion no valida")


if __name__ == "__main__":
    main()
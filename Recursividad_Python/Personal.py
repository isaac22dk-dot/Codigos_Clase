class ListaCompras:

    # 1. Mostrar los productos de la lista
    def mostrar_productos(self, lista: list) -> None:
        if len(lista) == 0:
            return
        print("-", lista[0])
        self.mostrar_productos(lista[1:])

    # 2. Mostrar los productos al reves
    def mostrar_al_reves(self, lista: list) -> None:
        if len(lista) == 0:  
            return
        self.mostrar_al_reves(lista[1:])  
        print("-", lista[0])

    # 3. Contar cuantos productos hay
    def contar_productos(self, lista: list) -> int:
        if len(lista) == 0: 
            return 0
        return 1 + self.contar_productos(lista[1:])

    # 4. Buscar si un producto esta en la lista
    def buscar_producto(self, lista: list, producto: str) -> bool:
        if len(lista) == 0:
            return False
        if lista[0] == producto:
            return True
        return self.buscar_producto(lista[1:], producto)

    # 5. Funcionalidad adicional: mostrar la lista numerada
    def mostrar_numerado(self, lista: list, numero: int = 1) -> None:
        if len(lista) == 0:
            return
        print(f"{numero}. {lista[0]}")
        self.mostrar_numerado(lista[1:], numero + 1)  # el numero avanza en cada llamada

    # 6. Funcionalidad adicional: eliminar un producto y devolver la lista nueva
    def eliminar_producto(self, lista: list, producto: str) -> list:
        if len(lista) == 0:
            return []
        if lista[0] == producto:
            return lista[1:]
        return [lista[0]] + self.eliminar_producto(lista[1:], producto)
from Nodo import Nodo
class ListaEnlazada:
    def __init__(self):
        # Se inicializa el inicio de la lista
        self.p = None #  "p" sera nuestro puntero al primer nodo

    def crear_lista(self):
        print("\n--- CREACION DE LISTAS LIGADAS ---")
        dato = int(input("Inttroduce el primer elemento de la lista: "))
        self.p = Nodo(dato)
        t = self.p # "t" marca el final de la lista para ir enlazando

        res = int(input("Desea ingresar mas nodos a la lista? (1= Si, 0= No): "))
        while res ==1:
            nuevo_dato = int(input("Escribe el elemento: "))
            q = Nodo(nuevo_dato)
            t.liga = q # El anterior apunta al nuevo
            t = q # "t" avanza al nuevo final
            res = int(input("Desea ingresar mas nodos a la lista ? (1= Si, 0= No): "))

    def mostrar_lista(self):
        print("\n--- Elementos de la lista ---")
        q = self.p
        if q is None:
            print("La lista esta vacia")
            return

        #Repetir mientras q <> Nill
        while q is not None:
            print(f"[{q.info}] -> ", end="")
            q = q.liga # Q = Q.LIGA
        print("NILL")

    def insertar_inicio(self, dato: int):
        q = Nodo(dato)
        q.liga = self.p
        self.p = q
        print(f"Elemento {dato} insertado al inicio.")
    def insertar_final(self, dato: int):
        if self.p is None:
            self.insertar_inicio(dato)
            return

        t = self.p
        while t.liga is not None:
            t = t.liga

        q = Nodo(dato)
        t.liga = q
        print(f"Elemento {dato} insertado al final.")
        

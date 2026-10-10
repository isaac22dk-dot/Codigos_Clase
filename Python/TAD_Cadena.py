class Cadena:
    """Implementacion del TDA cadena (string)"""

    def concatenar(self, cadena1: str, cadena2: str) -> str:
        return cadena1 + " " +cadena2

    def longitud(self, cadena: str) -> int:
        return len(cadena)

    def es_vacia(self, cadena: str) -> bool:
        return cadena == ""

    def son_iguales(self, cadena1: str, cadena2: str) -> bool:
        return cadena1 == cadena2
    
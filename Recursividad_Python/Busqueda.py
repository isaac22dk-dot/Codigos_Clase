import os

def listar_archivos_recursivamente(ruta_directorio: str, nivel: int = 0):
    try:
        # 1. Preparar la indentacion visual
        indentacion = "  " * (nivel * 3)
        nombre_carpeta = os.path.basename(os.path.normpath(ruta_directorio))
        print(f"{indentacion} Carpeta: {nombre_carpeta}")

        elementos = os.listdir(ruta_directorio)

        # 2. Imprimir los archivos primero
        for elemento in elementos:
            ruta_completa = os.path.join(ruta_directorio, elemento)
            if os.path.isfile(ruta_completa):
                print(f"{indentacion} {elemento}")

        # 3. Llamada recursiva para las subcarpetas
        for elemento in elementos:
            ruta_completa = os.path.join(ruta_directorio, elemento)
            if os.path.isdir(ruta_completa):
                listar_archivos_recursivamente(ruta_completa, nivel + 1)
    except PermissionError:
        print(f"!!! No se pudo acceder a la carpeta: {ruta_directorio} (Permiso denegado)")


def main():
    ruta_inicial = os.path.expanduser(input("Ingresa la ruta inicial: "))
    print(f"Iniciando la busqueda en: {ruta_inicial}\n")
    if os.path.exists(ruta_inicial):
        listar_archivos_recursivamente(ruta_inicial, 0)
    else:
        print("La ruta no existe.")


if __name__ == "__main__":
    main()
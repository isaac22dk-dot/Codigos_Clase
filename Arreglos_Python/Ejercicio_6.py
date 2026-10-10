#Ejercicio personal
#Empleados

empleados = []
def main():
    opc = -1
    while opc != 5:
        print("---------------------------------------------------------")
        print("Menu de opciones:")
        print("1. Agregar empleado")
        print("2. Eliminar empleado")
        print("3. Mostrar empleados")
        print("4. Buscar empleado")
        print("5. Salir")
        opc = int(input("Ingrese una opcion: "))
        print("---------------------------------------------------------")
        match opc:
            case 1:
                print("Agregar empleado:")
                nombre = input("Ingrese el nombre del empleado: ")
                apellido = input("Ingrese el apellido del empleado: ")
                sueldo = float(input("Ingrese el sueldo del empleado: "))
                empleados.append((nombre, apellido, sueldo))
                print(f"Empleado {nombre} {apellido} agregado.")
            case 2:
                if len(empleados) == 0:
                    print("No hay empleados registrados.")
                else:
                    for i, emp in enumerate(empleados):
                        print(f"{i}. {emp[0]} {emp[1]} - ${emp[2]}")
                        pos = int(input("Numero del empleado a eliminar: "))
                        if 0 <= pos < len(empleados):
                            eliminado = empleados.pop(pos)
                            print(f"Empleado {eliminado[0]} {eliminado[1]} eliminado.")
                        else:
                            print("Numero de empleado invalido.")
            case 3:
                print("Lista de empleados:")
                if len(empleados) == 0:
                    print("No hay empleados registrados.")
                else:
                    for i, empleado in enumerate(empleados):
                        print(f"{i}. {empleado}")
            case 4:
                nombre = input("Nombre: ")
                apellido = input("Apellido: ")
                nombres_apellidos = [(emp[0], emp[1]) for emp in empleados]
                if (nombre, apellido) in nombres_apellidos:
                    pos = nombres_apellidos.index((nombre, apellido))
                    print(f"Encontrado en la posicion {pos}")
                else:
                    print("Empleado no encontrado.")
            case 5:
                print("Saliendo del programa...")
            case _:
                print("Opcion invalida. Por favor, ingrese un numero entre 1 y 5.")
main()
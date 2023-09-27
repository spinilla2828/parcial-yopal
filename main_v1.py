
# Función principal para gestionar el menú
def main():
    while True:
        print("\nMenú Principal:")
        print("1. Agregar estudiante.")
        print("2. Buscar estudiante.")
        print("3. Buscar estudiantes por asignatura.")
        print("4. Mostrar todos los estudiantes.")
        print("5. Salir del programa.")
        opcion = input("Seleccione una opción (1/2/3/4/5): ")

        if opcion == "1":
            nombre = input("Ingrese el nombre del estudiante: ")
            edad = input("Ingrese la edad del estudiante: ")
            asignaturas = input("Ingrese las asignaturas en las que está inscrito (separadas por coma): ").split(',')
            agregar_estudiante(nombre, edad, asignaturas)
        elif opcion == "2":
            nombre = input("Ingrese el nombre del estudiante que desea buscar: ")
            buscar_estudiante(nombre)
        elif opcion == "3":
            asignatura = input("Ingrese el nombre de la asignatura que desea buscar: ")
            buscar_estudiantes_por_asignatura(lista_estudiantes, asignatura)
        elif opcion == "4":
            mostrar_estudiantes(lista_estudiantes)
        elif opcion == "5":
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

# Inicialización del programa
if __name__ == "__main__":
    main()

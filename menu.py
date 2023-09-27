# Función para mostrar la información de todos los estudiantes
def mostrar_estudiantes(lista_estudiantes):
    if not lista_estudiantes:
        print("No hay estudiantes registrados.")
    else:
        print("Lista de estudiantes:")
        for estudiante in lista_estudiantes:
            print(f"Nombre: {estudiante.nombre}")
            print(f"Edad: {estudiante.edad}")
            print("Asignaturas inscritas:")
            for asignatura in estudiante.asignaturas:
                print(f"- {asignatura}")
            print("\n")

# Función para buscar estudiantes por asignatura
def buscar_estudiantes_por_asignatura(lista_estudiantes, asignatura_buscada):
    estudiantes_encontrados = []
    for estudiante in lista_estudiantes:
        if asignatura_buscada in estudiante.asignaturas:
            estudiantes_encontrados.append(estudiante)

    if not estudiantes_encontrados:
        print(f"No hay estudiantes inscritos en la asignatura: {asignatura_buscada}")
    else:
        print(f"Estudiantes inscritos en la asignatura {asignatura_buscada}:")
        for estudiante in estudiantes_encontrados:
            print(f"Nombre: {estudiante.nombre}")
            print(f"Edad: {estudiante.edad}")
            print("\n")

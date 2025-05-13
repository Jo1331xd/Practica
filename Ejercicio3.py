print("Calculo promedio de calificaciones de estudiantes de la UAM")

num_estudiantes = int(input("Ingrese la cantidad de estudiantes: "))


for estudiante in range(num_estudiantes):
    print(f"\nEstudiante {estudiante + 1}")
    total_promedio = 0  # Acumulador para el promedio general
    num_asignaturas = 3  # Número fijo de asignaturas


    for asignatura in range(num_asignaturas):
        print(f"\nAsignatura {asignatura + 1}")
        total_calificaciones = 0  # Acumulador para el promedio de la asignatura
        num_tareas = 3  # Número fijo de tareas

    
        for tarea in range(num_tareas):
            calificacion = float(input(f"Ingrese la calificación de la tarea {tarea + 1}: "))
            total_calificaciones += calificacion

    
        examen = float(input("Ingrese la calificación del examen: "))
        total_calificaciones += examen

        
        promedio_asignatura = total_calificaciones / (num_tareas + 1)
        print(f"Promedio de la asignatura {asignatura + 1}: {promedio_asignatura:.2f}")

    
        total_promedio += promedio_asignatura

    
    promedio_general = total_promedio / num_asignaturas
    print(f"\nPromedio general del estudiante {estudiante + 1}: {promedio_general:.2f}")
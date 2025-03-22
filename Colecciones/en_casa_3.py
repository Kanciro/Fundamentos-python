
nombres = ["Will Ramos", "Nicol Amaya", "Zack Sandón", "Jhon Medina", "David Rodríguez", "Isabella Martinez"]
calificaciones = [8.5, 7.2, 9.0, 6.8, 9.5, 8.0]


print("=== INFORME DE CALIFICACIONES ===")
print("Posición | Nombre             | Calificación")
print("---------|--------------------|------------")


for i in range(len(nombres)):
    print(f"{i + 1:^6}| {nombres[i]:<19}| {calificaciones[i]:^12}")


print("\n=== SISTEMA DE CONSULTA ===")
print(f"Ingresa un número (1-{len(nombres)}) para ver la calificación.")
print("Otro número para salir.")

while True:
    try:
        posicion = int(input("\nPosición del alumno: "))

       
        if 1 <= posicion <= len(nombres):
            indice = posicion - 1  
            print(f"Alumno: {nombres[indice]}")
            print(f"Calificación: {calificaciones[indice]}")
        else:
            print("Posición incorrecta. Fin de consulta.")
            break  

    except ValueError:
        print("Debes ingresar un número.")
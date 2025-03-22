numeros = [34, 12, 89, 45, 23, 67, 9, 51, 78]
continuar = True

while continuar:
    print("\n" + "=" * 40)
    print("=== OPERACIONES CON VALORES NUMÉRICOS ===")
    print("=" * 40)

    print("\nColección actual:", numeros)
    print(f"Cantidad de elementos: {len(numeros)}")

    print("\nMENÚ DE OPCIONES:")
    print("1. Calcular suma total")
    print("2. Reordenar valores")
    print("3. Eliminar un valor")
    print("4. Salir")

    opcion = input("\nSelecciona una opción (1-4): ")

    if opcion == "1":
        suma = sum(numeros)
        print(f"\nLa suma total de los valores es: {suma}")

    elif opcion == "2":
        print("\n=== OPCIONES DE ORDENAMIENTO ===")
        print("1. Ordenar de menor a mayor")
        print("2. Ordenar de mayor a menor")

        opcion_orden = input("Selecciona una opción (1-2): ")

        if opcion_orden == "1":
            numeros.sort()
            print("\nColección ordenada de menor a mayor")
        elif opcion_orden == "2":
            numeros.sort(reverse=True)
            print("\nColección ordenada de mayor a menor")
        else:
            print("\nOpción no válida. No se realizó ningún ordenamiento.")

    elif opcion == "3":
        try:
            indice = int(input(f"\nIngresa la posición del valor a eliminar (1-{len(numeros)}): "))

            if 1 <= indice <= len(numeros):
                valor_eliminado = numeros.pop(indice - 1)
                print(f"\nSe ha eliminado el valor {valor_eliminado} en la posición {indice}")
            else:
                print("\nPosición fuera de rango. No se eliminó ningún valor.")
        except ValueError:
            print("\nDebes ingresar un número válido.")

    elif opcion == "4":
        print("\nFinalizando aplicación. ¡Hasta pronto!")
        continuar = False

    else:
        print("\nOpción no válida. Por favor, intenta nuevamente.")

mi_lista = [1, 2, 3, 4, 2, 5, 2, 6, 7, 2]

numero_a_borrar = int(input("Ingresa el número que deseas borrar de la lista: "))

nueva_lista = [numero for numero in mi_lista if numero != numero_a_borrar]

print("Lista final:", nueva_lista)

num_elementos = int(input("¿Cuántos elementos deseas ingresar en la lista? "))
mi_lista = []
for i in range(num_elementos):
    elemento = input(f"Ingresa el elemento {i + 1}: ")
    mi_lista.append(elemento)
print("Contenido de la lista:", mi_lista)
lista_invertida = mi_lista[::-1]
print("Contenido invertido de la lista:", lista_invertida)

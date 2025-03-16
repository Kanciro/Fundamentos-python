
frase1 = input("Ingresa la primera frase: ")
frase2 = input("Ingresa la segunda frase: ")

lista1 = list(frase1)
lista2 = list(frase2)


letras_repetidas = []
longitud_minima = min(len(lista1), len(lista2))
for i in range(longitud_minima):
    if lista1[i] == lista2[i]:
        letras_repetidas.append(lista1[i])

print("Letras repetidas en la misma posición:", letras_repetidas)
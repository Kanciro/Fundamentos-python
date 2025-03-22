
texto = input("Escribe algo aquí: ")


letras = list(texto)


print("\nAquí están las letras que escribiste:")
for posicion, letra in enumerate(letras):
    print(f"Letra en la posición {posicion}: '{letra}'")


solo_letras = []
for letra in letras:
    if letra.isalpha():  
        solo_letras.append(letra)  


letras_finales = tuple(solo_letras)

print("\nSolo las letras:")
print(f"Escribiste {len(letras)} caracteres en total.")
print(f"De esos, {len(solo_letras)} son letras.")
print("\nLas letras que escribiste son:")
print(letras_finales)

# 7. Muestra las letras juntas como texto
texto_final = ''.join(letras_finales)
print(f"\nTexto final (solo letras): '{texto_final}'")
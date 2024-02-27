# Analizador de texto:

song = input("Por favor, escribe una oración que te guste: ").lower()
print("\n")

letra1 = input("Por favor, ingrese la primera de 3 letras a elección: ").lower()
letra2 = input("Por favor, ingrese la segunda de 3 letras a elección: ").lower()
letra3 = input("Por favor, ingrese la última letras a elección: ").lower()

print("\n")
print("Cuantas veces se repiten las letras en nuestro texto: \n")

listaLetras = []
listaLetras.append([letra1, letra2, letra3])

song.count(letra1)
song.count(letra2)
song.count(letra3)

conteo1 = song.count(letra1)
conteo2 = song.count(letra2)
conteo3 = song.count(letra3)

print(f"La letra: '{letra1}' aparece en el texto: {conteo1} veces. \n La letra: '{letra2}' aparece: {conteo2} veces. \n Por ultimo la letra: '{letra3}' aparece: {conteo3} veces en el texto seleccionado.")
print("\n")

listaSong = song.split()

largo = len(listaSong)

print(f"El texto que has seleccionado contiene: {largo} palabras")
print("\n")






# lenLetrasSong = len(listaLetras[0] in song)
# lenLetrasSong1 = len(listaLetras[1] in song)
# lenLetrasSong2 = len(listaLetras[2] in song)

# print(lenLetrasSong)

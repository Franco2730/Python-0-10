# Analizador de texto:

song = input("Por favor, escribe una oración que te guste: ").lower()

letra1 = input("Por favor, ingrese la primera de 3 letras a elección: ").lower()
letra2 = input("Por favor, ingrese la segunda de 3 letras a elección: ").lower()
letra3 = input("Por favor, ingrese la última letras a elección: ").lower()
print("\n")

print("Cuantas veces se repiten las letras en nuestro texto: \n")

listaLetras = []
listaLetras.append([letra1, letra2, letra3])

conteo1 = song.count(letra1)
conteo2 = song.count(letra2)
conteo3 = song.count(letra3)

print(f"La letra: '{letra1}' aparece en el texto: {conteo1} veces. \nLa letra: '{letra2}' aparece: {conteo2} veces. \nPor ultimo la letra: '{letra3}' aparece: {conteo3} veces en el texto seleccionado.")

listaSong = song.split()

largo = len(listaSong)
print('\n')
print(f"El texto que has seleccionado contiene: {largo} palabras")
print("\n")
primeraLetra = listaSong[0][0]
ultimaLetra = listaSong[-1][-1]

print(f"La primera letra de tu texto es: {primeraLetra}, y la ultima es: {ultimaLetra}")
print("\n")

print("Palabras separadas y luego juntas:")
print("\n")

listaSong.reverse()
print(listaSong)

listaSongJuntas = ' '.join(listaSong)
print(listaSongJuntas)
print("\n")
print("¿ Aparece la palabra Python en nuestro texto? :")


if("Python".lower() in song):
     print("Si, si aparece en el texto")
else: print("No, no aparece en el texto")
print("\n")
print("\n")
print("\n")



#* Esta función es divertida, pero puede parecer irrelevante. Pero si tienes paciencia, entenderás cual puede ser su verdadero poder. 

#* Lo que hace ZIP es básicamente combinar dos o más listas entrelazando sus elementos en tuples. Supongamos que tenemos la lista nombres por un lado y por otro lado la lista de edades. Si utilizamos zip y pasamos como argumentos los nombres de las dos listas lo que obtendremos es una lista de tuples en los que se han juntado un elemento de cada lista en orden. 

nombres = ['Franco', 'Carina', 'Mariano']
edades = [30, 50, 57]
ciudades = ['Madrid', 'Estados Unidos', 'Argentina']

lista_convinada = list(zip(nombres, edades, ciudades))

print(lista_convinada)

# [('Franco', 30, 'Madrid'), ('Carina', 50, 'Estados Unidos'), ('Mariano', 57, 'Argentina')]

#* Que pasa si queremos armar una frase con cada elemento de todas las listas ? Asi de simple:

for name, age, city in lista_convinada:
    print(f'{name} tiene {age} años y vive en: {city}')

# Franco tiene 30 años y vive en: Madrid
# Carina tiene 50 años y vive en: Estados Unidos
# Mariano tiene 57 años y vive en: Argentina



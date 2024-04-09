
#* Ahora vamos a tratar de crear un loop for en el que necesitemos acceder a los indices de los elementos de una lista con los elementos que tenemos hasta ahora: Recordemos que no es la mejor manera para hacer esto

# lista = ['Charger', 'Charger Daytona', 'Challenger', 'Supra', 'H. Civic', 'Eclipse']
# indice = 1

# for item in lista:
#     print(f'Auto número {indice}: {item}')
#     indice += 1

# Auto número 1: Charger
# Auto número 2: Charger Daytona   
# Auto número 3: Challenger        
# Auto número 4: Supra
# Auto número 5: H. Civic
# Auto número 6: Eclipse

#todo--------------

#* En Python, el método Enumerate() es una ayuda extra que nos permite contar mientras revisamos una lista de cosas. Imagina que tienes una lista de tus autos favoritos y quieres revisar cada uno de ellos. Pero, al mismo tiempo, quieres saber el número de ese auto en tu lista, ¿verdad? Aquí es donde enumerate() entra en juego.

#* Digamos que tienes la misma lista que en el ejemplo anterior

autos = ['Charger', 'Charger Daytona', 'Challenger', 'Supra', 'H. Civic', 'Eclipse']

#* Usando enumerate(), puedes ver cada auto uno por uno y también saber su número en la lista. Es como si estuvieras diciendo "¡Aquí está el auto número 1!" y luego "¡Ahora el auto número 2!", y así sucesivamente.

# for numero, auto in enumerate(autos, start = 1):
#     print(f"Auto número {numero}: {auto}")

# Auto número 1: Charger
# Auto número 2: Charger Daytona   
# Auto número 3: Challenger        
# Auto número 4: Supra
# Auto número 5: H. Civic
# Auto número 6: Eclipse

#* ¿Lo ves? enumerate() te ayuda a contar tus autos mientras los revisas uno por uno. Es como tener un asistente que te recuerda qué número de auto estás viendo en tu lista. ¡Es muy útil cuando necesitas saber tanto el elemento como su posición en la lista! Veamos otros ejemplos:

#* En síntesis, enumerate devuelte tupples:

lista2 = ['a', 'b', 'c']

for item in enumerate(lista2):
    print(item)

# (0, 'a')
# (1, 'b')
# (2, 'c')

#* En los parámetros que recibe el método enumerate podemos ver que también le podemos decir que comience en un determinado número. En el ejemplo pasado, al no colocarle nada, comenzó desde el 0. En el ejemplo de los autos le colocamos: enumerate(autos, start = 1) por eso, la lista comenzó desde ese número. Hagamos el anterior comenzando en 1 y separemos el indice del ítem:

lista3 = ['a', 'b', 'c']

for indice, item in enumerate(lista2, start = 1):
    print(indice, item)

# 1 a
# 2 b
# 3 c

#* También podemos juntar el enumerate con el range. Podemos enumerar un rango de niveles, por ejemplo:

for indice, item in enumerate(range(0, 10), start = 1):
    print(f'En {indice}, pertenece al número: {item}')

# El indice 1, pertenece al número: 0
# El indice 2, pertenece al número: 1
# El indice 3, pertenece al número: 2
# El indice 4, pertenece al número: 3
# El indice 5, pertenece al número: 4
# El indice 6, pertenece al número: 5
# El indice 7, pertenece al número: 6
# El indice 8, pertenece al número: 7
# El indice 9, pertenece al número: 8
# El indice 10, pertenece al número: 9

#* Si lo hacemos al revés, podríamos enseñar programación: (que el indice comience en 0 y el ítem en 1)

for indice, item in enumerate(range(1, 10)):
    print(f'En la programación, al momento de iterar un objeto iterable el indice número: {indice}, pertenece al elemento número: {item}')

# En la programación, al momento de iterar un objeto iterable el índice número: 0, pertenece al elemento número: 1
# En la programación, al momento de iterar un objeto iterable el indice número: 1, pertenece al elemento número: 2
# En la programación, al momento de iterar un objeto iterable el indice número: 2, pertenece al elemento número: 3
# En la programación, al momento de iterar un objeto iterable el indice número: 3, pertenece al elemento número: 4
# En la programación, al momento de iterar un objeto iterable el indice número: 4, pertenece al elemento número: 5
# En la programación, al momento de iterar un objeto iterable el indice número: 5, pertenece al elemento número: 6
# En la programación, al momento de iterar un objeto iterable el indice número: 6, pertenece al elemento número: 7
# En la programación, al momento de iterar un objeto iterable el indice número: 7, pertenece al elemento número: 8
# En la programación, al momento de iterar un objeto iterable el indice número: 8, pertenece al elemento número: 9

#* Algo un poco más difícil que nos toque hacer pero el saber NUNCA ESTÁ DE MÁS, es a una lista llamada mi_lista, que contiene las 5 primeras letras del abecedario, se transforme en una lista de tuples, en vez de una lista de strings, una lista que contenga tuples con su número de índice e item.

# mi_lista = [ 'a', 'b', 'c', 'd', 'e' ]

# mis_tuples = list(enumerate(mi_lista)) # El método enumerate tiene adentro a la lista, para enumerar cada elemento de esa lista con un número de índice. Todo esto, estará encerrado en paréntesis para hacerle un casting y transformar todo a una gran lista de tuples enumerados. Todo dentro de una variable y abajo la imprimimos y vemos el resultado. 

# print(mis_tuples)

# [(0, 'a'), (1, 'b'), (2, 'c'), (3, 'd'), (4, 'e')]

#*Supongamos que necesitamos ingresar a la lista de los tuples y acceder al elemento d:

mi_lista = [ 'a', 'b', 'c', 'd', 'e' ]

mis_tuples = list(enumerate(mi_lista)) 

print(mis_tuples[3][1]) # Accedemos al tuple en la tercera posición y a su índice número 1 (que es el segundo elemento)

# d


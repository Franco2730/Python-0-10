
#* Los métodos sirven para encontrar los valores mayores y menores en una colección. (cualquier iterable)
#* Esto también sirve para strings en cuanto al abecedario

mayor = max(1, 10, 100, 1000, 10000, 100000, 1000000)
menor = min(1, 10, 100, 1000, 10000, 100000, 1000000)

# print(mayor) #1000000
# print(menor) #1

#todo ------Otro ejemplo: ------

#*Veamos en otro ejemplo como sacamos el número mas chico y el mas grande dentro de una lista para formar una oración

lista = [1, 10, 100, 1000, 10000, 100000, 1000000]

# print(f'El menor número es el: {min(lista)} y el mayor es el: {max(lista)}')

# El menor número es el: 1 y el mayor es el: 1000000

#todo ------Otro ejemplo: ------

#* Veamos como podemos utilizar esto con los strings: Como ya sabemos, los strings son una cadena de caracteres, y si buscamos el str con el menor número de caracteres no hace referencia a las letras, si no, a que tan proximo está de la letra A en el alfabeto. 

nombres = ['Franco', 'Carina', 'Mariano', 'Lautaro', 'Julia', 'Florencia']
nombre = "Carina"

# print(min(nombres)) # Carina => es el nombre que mas se acerca a la A
# print(min(nombre))  # C => si bien, no es la letra que mas se acerca a la A, python primero examina las letras mayúsculas y luego las minusculas. Si el nombre hubiese sido: carina el min de ese nombre, claramente es la: a.

#* Si quisieramos corregir ese pequeño poisible error de que primero Python ve las mayusculas y luego las demás. Podemos utilizar el método lower() para volver todo a minuscula

# print(f'La letra que mas se acerca en el abecedario es la letra: {min(nombre.lower())}')

# La letra que mas se acerca en el abecedario es la letra: a

#todo ------Otro ejemplo: ------

#* Ahora bien, que sucede si trabajamos estos métodos con un diccionario con una clave y un valor. Al colocar min o max, estaremos buscando el min, max de la clave o el valor ? Vamos a ver !!

dicc = {'C1': 100, 'C2': 10}

print(min(dicc)) # C1 => como puede ser posible ? Le pedimos el menor del diccionario y nos arrojó esa clave, y esto es correcto, ya que esa clave es la menor, para tomar en cuenta el menor o mayor de sus valores recordemos que tenemos el método values():
print(min(dicc.values())) # 10


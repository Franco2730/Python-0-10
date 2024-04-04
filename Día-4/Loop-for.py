# Como ya habíamos mencionado, los loops for son aquellos bucles que se repiten una cantidad DEFINIDA de iteraciones. Supongamos que tenemos el siguiente escenario:

nombres = ['Juan', 'Agustina', 'Marcos', 'Carlos', 'Belen', 'Fran']

# Ahora pensemos que queremos colocar: Hola, como estas? por cada nombre que haya en la lista llamada nombres. En castellano diriamos algo como:

#* por cada ELEMENTO en NOMBRES:
#*     imprimir("Hola")

#! La sentencia anterior es en español, veamos como se vería en código:
# Por cada, en ingles, se dice FOR 
# en, se dice IN
# elemento es una variable interna que le asignamos a los elementos de la lista, pero podriamos haber puesto element, i, ele, perro. Tenemos que saber que eso representa cada uno de nuestros elementos. 

#* FOR elemento IN nombres: 
#*      print("Hola")

#* FOR ele IN nombres: 
#*      print("Hola")

#* FOR i IN nombres: 
#*      print("Hola")

for nombre in nombres:
    print("loop for activado")



#* Algo SUPER interesante de saber es, como vemos en nuestra lista llamada nombres, tenemos 6 elementos (los 6 nombres), cuando hacemos el bucle for que vimos anteriormente, la variable interna que llamamos elemento, ele o i va a contener (como cajita que es) en su interior, al elemento que este iterando en cada vuelta, es decir, cuando el loop for apenas comienza la variable interna elemento tendrá el valor juan y se imprimirá en consola Hola.
#* Vuelve el loop a comenzar pero en su segunda vuelta, la variable elemento tendrá el valor de Agustin, acto segudo solo se imprimirá Hola en consola, ya que esa es la orden que le dimos, asi con el tercer elemento que es Marcos hasta llegar a Fran e imprimir el sexto Hola en consola:

# Hola 
# Hola 
# Hola 
# Hola 
# Hola 
# Hola 

#* Pero como podemos estar analizando, si elemento contiene un valor (un nombre distinto en cada vuelta) no podriamos realizar un saludo un poco mas personalizado? Veamos !!!

for elemento in nombres:
    print('Hola ', elemento, '¿Como estás el día de hoy?')

# Hola  Juan ¿Como estás el día de hoy?
# Hola  Agustina ¿Como estás el día de hoy?
# Hola  Marcos ¿Como estás el día de hoy?
# Hola  Carlos ¿Como estás el día de hoy?
# Hola  Belen ¿Como estás el día de hoy?
# Hola  Fran ¿Como estás el día de hoy?

#* ----------------------------------
    
autos = ['chevy', 'falcon', 'dodge', 'peugeot', 'fiat', 'ferrari']

for autito in autos:
    print(autito)

# chevy
# falcon
# dodge
# peugeot
# fiat
# ferrari
    
for autito in autos:
    print('Me gustaría tener un:',autito)

# Me gustaría tener un: chevy      
# Me gustaría tener un: falcon     
# Me gustaría tener un: dodge      
# Me gustaría tener un: peugeot    
# Me gustaría tener un: fiat       
# Me gustaría tener un: ferrari

#* ----------------------------------

    
#* Podemos hacer un loop for con dos variables dentro y que ambas cambien en cada iteración:
    
abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i','j','k', 'l', 'm', 'n', 'ñ','o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

for i in abc:
    numeroDeLetra = abc.index(i) + 1 # aclaramos que sea más uno para no arrancar en cero
    print(f'La letra {numeroDeLetra}: {i}')

# La letra 1: a
# La letra 2: b
# La letra 3: c
# La letra 4: d
# La letra 5: e
# La letra 6: f
# La letra 7: g
# La letra 8: h
# La letra 9: i
# La letra 10: j
# La letra 11: k
# La letra 12: l
# La letra 13: m
# La letra 14: n
# La letra 15: ñ
# La letra 16: o
# La letra 17: p
# La letra 18: q
# La letra 19: r
# La letra 20: s
# La letra 21: t
# La letra 22: u
# La letra 23: v
# La letra 24: w
# La letra 25: x
# La letra 26: y
# La letra 27: z
    
#* ----------------------------------

#* Ahora vamos a recorrer una lista de amigos y, ademas de recorrer dicha lista, dentro del bucle for vamos a verificar si el nombre (en cada vuelta del loop) comienza con una letra especifica, esto se logra con el método startwith()
    
amigos = ['Emilia', 'Emanuel', 'Luciano', 'Rocio', 'Romina', 'Federico']

for nombre in amigos:
    if nombre.startswith("E"):
        print(nombre)
    else:
        print("Nombre que no comienza con la E")

# Emilia
# Emanuel
# Nombre que no comienza con la E
# Nombre que no comienza con la E
# Nombre que no comienza con la E
# Nombre que no comienza con la E

#* ----------------------------------

numeros = [1, 2, 3, 4, 5]
mi_valor = 0

for numero in numeros:
    mi_valor = mi_valor + numero

print(mi_valor)

# 15

#* ----------------------------------

#Los str al igual que las listas, son objetos iterables. Es decir, podemos recorrer todos sus elementos.

palabra = 'Python'

for letra in palabra:
    print(letra)

# P
# y
# t
# h
# o
# n

#* No necesariamente tenemos que tener una variable externa:

for i in "Kodland":
    print(i)

# K
# o
# d
# l
# a
# n
# d

#* Podemos iterar un tuple:

for nro in (1, 2, 3):
    print(nro)

# 1
# 2
# 3

#* Podemos iterar en una lista que contenga listas:

for objeto in [[1, 2, 3], [4, 5, 6], [7, 8, 9]]:
    print(objeto)

# [1, 2, 3]
# [4, 5, 6]
# [7, 8, 9]

#* Importate, tomando en cuenta el ejercicio anterior, que sucede si queremos imprimir los numeros por separado ? En vez de una sola variable llamada objeto debemos crear una variable por cada elemento del objeto para que en cada iteracion, esta agarre al primer, segundo y tercer elemento de cada objeto. 

for a, b, c in [[1, 2, 3], [4, 5, 6], [7, 8, 9]]:
    print(a, b, c)

# 1 2 3
# 4 5 6
# 7 8 9

for a, b, c in [[1, 2, 3], [4, 5, 6], [7, 8, 9]]:
    print(a)
    print(b)
    print(c)

# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9

#* ----------------------------------

#* Tenemos esta otra situación donde tenemos un diccionario con su clave valor.

dicc = {'clave1': 'a', 'clave2': 'b', 'clave3': 'c'}

#todo Podemos ver que si colocamos una sola variable interna, en cada iteración, python solo va a imprimir las claves, más no los valores. 

for item in dicc:
    print(item)
    
# clave1
# clave2
# clave3

#* Para imprimir clave valor, deberiamos colocar dos variables internas y el metodo items() para poder visualizar

for item, value in dicc.items():
    print(item, value)

# clave1 a
# clave2 b
# clave3 c

#* o si hubiesemos querido ver solo los valores, tambien tenemos el método value():

for item in dicc.values():
    print(item)

# a
# b
# c
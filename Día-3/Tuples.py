# Los tuples son una coleccion de elementos parecida a las listas pero son INMUTABLES. Una vez que un elemento fue asignado a un tuple no puede cambiarse ni reasignarse. 
# Ya que los tuples son muy similares a las listas, incluso son mas limitados por ser inmutables. ¿Por qué usaríamos tuples y no listas?
# En primer lugar porque los tuples ocupan menor cantidad de memoria.
# Segundo: Al no poder ser modificadas, usaríamos los tuples para cuando queremos almacenar estructuras que NO queremos que sean modificadas, es decir, a prueba de daño. 

#* Se escriben como las listas pero en vez de usar [] se pueden escribir entre () o sin nada:
mi_tuple = 'perro', 'gato', 'gallo'
mi_tuple2 = ['perro', 'gato', 'gallo']
print(type(mi_tuple)) # <class 'tuple'>

print(mi_tuple, mi_tuple2) # ('perro', 'gato', 'gallo')  ['perro', 'gato', 'gallo']


miTuple = (1, 2, 3, 4, 5)
# miTuple[2] = 100 => Esto dará un error porque si recordamos: Los tuples SON INMUTABLES.

print(miTuple[1]) # 2
print(miTuple[-2]) # 4


miTuple2 = (1, 2, 3, (4, 5, 10), 20)

print(miTuple2[3]) # (4, 5, 10)
print(miTuple2[3][0]) # 4

# En los tuples tambien podemos hacer CASTING (transformar datos)

tuple = (1, 2, 3, 4)
tupleList = list(tuple)

print(type(tupleList)) # <class 'list'>


#* También podemos asignar el contenido de un tuple a diferentes variables:
tup = (1, 2, 3, 4, 5)

a, b, c, d, e = tup

print(a, b, c, d, e) # 1 2 3 4 5 => ¿Qué es lo que ha pasado? Simplemente, al crear un determinado número de valores y ese mismo número determinado de variables, lo que ha sucedido es que se asignan automáticamente. Si tuviera más o menos valores o variables, automáticamente la consola nos arroja un error de que esperaba mas o menos valores o variables. Esto funciona en las listas, diccionarios y tuples

#* Para pedir cuantos elementos tiene nuestro tuple:
t = (1, 2, 3, 4, 5, 1)

print(len(t)) # 6

#* Para saber cuantas veces aparece repetido un elemento en nuestro tuple:
print(t.count(1)) # 2 => lo que le pasamos por parametro es lo que examinará para ver si está repetido

#* Para saber el número de índice:
print(t.index(3)) # 2 => en el indice 2 de nuestro tuple llamado t se encuentra el número 3.


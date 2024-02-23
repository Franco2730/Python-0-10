# Elementos, al igual que las listas, pero con algunas diferencias que los hacen muy particulares. Los sets se pueden declarar de dos maneras. 
# Usando la palabra clave set y luego poner los elementos entre paréntesis
# set(1, 2, 3, 4)

# o usando llaves sin colocar la palabra set
# { 1, 2, 3, 4 }

# A pesar que las llaves son las mismas que usamos para declarar diccionarios, Python se da cuenta ya que su contenido es distinto al que usamos en los diccionarios.
# Luego, para escribir sus elementos, como dijimos, hay dos formas. Si usaste la palabra set con los paréntesis, este solo requiere un argumento, es decir que entre los paréntesis, deberemos colocar corchetes: set([ 1, 2, 3, 4 ])

# Pero si creamos el set con los corchetes, entonces podemos poner todos los elementos directamente, la particularidad mas importante de los sets es porque solo admiten ELEMENTOS ÚNICOS, acá los elementos NO SE REPITEN. Si agregamos un elemento repetido Python directamente no los agrega dejando los elementos únicos.

# Los elementos en los sets no están ordenados con números de índices (como los diccionarios), si bien veremos elementos desplegados en una secuencia, no podes indexarlos ni organizarlos ni nada que tenga que ver con su posición interna. 

# Otra situación importante a destacar es que además sus elementos son inmutables.

mi_set = set([ 1, 2, 3, 4, 5 ]) # También es válido: (( 1, 2, 3, 4, 5 )) o ({ 1, 2, 3, 4, 5 })
print(mi_set)       # {1, 2, 3, 4, 5}
print(type(mi_set)) # <class 'set'>

otro_set = { 1, 2, 3 }
print(otro_set)       # {1, 2, 3}
print(type(otro_set)) # <class 'set'>

#* Recordemos que los objetos SETS no tienen índices, no podremos buscar un elemento según su posición de índice. A continuación, vamos a ver como los objetos sets NO ADMITEN ELEMENTOS REPETIDOS:

set_repetido = set([ 1, 1, 1, 2, 3, 4, 5, 5, 5, 6, 6, 7, 7, 7, 7, 8, 8, 2, 9, 2, 10 ])
print(set_repetido) # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

#* Importante las siguientes aclaraciones: Los Sets SI ACEPTAN TUPLES EN SU INTERIOR: 
setTuple = set([ 1, 2, 3, ('a', 'b', 'c'), 4, 5 ])
print(setTuple)       # {1, 2, 3, 4, 5, ('a', 'b', 'c')}
print(type(setTuple)) # <class 'set'>

#! Pero NO ACEPTAN LISTAS NI DICCIONARIOS:
#*¿Por qué si aceptan tuples pero no aceptan listas ni diccionarios? Simplemente porque los tuples son inmutables y el set requiere que sus elementos sean inmutables. Y las listas y diccionario son mutables.

#* Podemos preguntar cuántos elementos hay en un set:
print(len(setTuple)) # 6

#* Podemos preguntar si un elemento se encuentra en un Set:
print(2 in setTuple) # True
print(9 in setTuple) # False

#* Como podemos unir algunos Sets:
s1 = {1, 2, 3}
s2 = {3, 4, 5} # De forma intencional hice que el número 3 esté en ambos sets.
s3 = s1.union(s2)
print(s3) # {1, 2, 3, 4, 5}

#* Vamos a agregar un elemento a un set:
s1.add(4)
s1.add(1)

print(s1) # {1, 2, 3, 4} => Al set {1, 2, 3} le agregamos el n° 4 y el n° 1. Solo se agregó el 4 ya que, como bien sabemos, los sets no admiten elementos repetidos asique, omitió ese código y siguió con la ejecución del programa.

#* Vamos a eliminar un elemento de un set:
s1.remove(1)
print(s1) # {2, 3, 4} => Con el método remove, lo que le pasamos por parámetro, lo elimina de nuestro set.

#* ¿Qué pasa si queremos eliminar un elemento inexistente de nuestro set? Nos devuelve un error.
# s1.remove(9)
# print(s1) # KeyError: 9 => No se puede eliminar algo que no existe en los sets.

#* En vez de eliminar, podemos tratar de DESCARTAR un elemento. La diferencia es que cuando tratamos de eliminar un elemento que no existe, como ya vimos, la consola nos devuelve un error. Si intentamos descartar un elemento inexistente, la consola no nos devolvería un error, simplemente no haría nada. 

#* Un elemento que podemos utilizar para eliminar es pop(). Pero RECORDAR, en los sets no hay índices, no existe un primer ni segundo elemento. Con lo cual, el método pop eliminaría un elemento al azar. Teniendo eso en cuenta, pop puede resultar ser un tanto peligroso: Podría servir para un sorteo, por ejemplo.
print(s1) # {2, 3, 4}
s1.pop()
print(s1) # {3, 4}

#* Otro método que tenemos es para vaciar nuestro set llamado clear():
s1.clear()
print(s1) # set()









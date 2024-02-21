# Una lista es una secuencia ordenada de objetos, las listas también pueden ser asignadas a una variable y los elementos pueden ser str, int o cualquier tipo de datos que veremos en el futuro. Incluso una lista puede estar compuesta de objetos de diferentes tipos de datos se escriben entre corchetes y sus elementos tienen que estar separados por coma. 
# También se pueden anidar listas, O sea como podemos tener una lista de strings o de int, también podemos tener una lista con listas adentro.
# Se pueden indexar y / o fraccionar. 
# Tenemos métodos para manipularlas y A DIFERENCIA DE LOS STRINGS, una lista no es inmutable, por lo que si podemos modificar y organizar su contenido.

mi_lista = ['a', 'b', 'c']
# print(type(mi_lista)) # <class 'list'>

#* También podemos crear una lista con diferentes tipos de datos:
mi_lista2 = ['Hola', 22, 1.5]
# print(type(mi_lista2)) # <class 'list'>

#* También podemos saber cuántos elementos contiene una lista con el método LEN
mi_lista3 = ['Hola', 22, 1.5, "Cielo", {"nombre": "Franco"}]
largo = len(mi_lista3)
# print(largo) # 5 => Contiene 5 elementos. 
# print(type(largo)) # <class 'int'>

#* También podemos indexar y extraer alguno de sus elementos y meterlo dentro de una variable:
objetoNombre = mi_lista3[4]
# print(objetoNombre) # {'nombre': 'Franco'}

objetos = mi_lista3[0 : 3]
# print(objetos) # ['Hola', 22, 1.5]

#* Tenemos dos listas y queremos concatenarlas: Pero vamos a encontrar un problema, cuando imprimimos lista + lista2 no estamos creando una nueva lista, no modificamos las originales, por lo tanto, no podríamos trabajar sobre la lista unificada. 
lista = ['a', 'b', 'c'] 
lista2 = ['d', 'e', 'f']

# print(lista + lista2) # ['a', 'b', 'c', 'd', 'e', 'f']

#* Para "unificar" las listas, bien podríamos crear una tercer variable que contenga ambas listas, ahí se creará un nuevo espacio de memoria que contendrá toda esa información junta:
lista3 = lista + lista2
# print(lista3) # ['a', 'b', 'c', 'd', 'e', 'f'] => Esta si sirve como elemento único.

#* Si podemos sobre escribir un solo elemento, que en los str no podíamos hacerlo
mi_lista3[3] = "Auto"
# print(mi_lista3) # ['Hola', 22, 1.5, 'Auto', {'nombre': 'Franco'}]

#* Podemos agregar un nuevo elemento:
mi_lista3.append("Boooooca Booooooca")
# print(mi_lista3) # ['Hola', 22, 1.5, 'Auto', {'nombre': 'Franco'}, 'Boooooca Booooooca']

#* Podemos eliminar - remover un elemento existente:
# mi_lista3.pop()
# print(mi_lista3) # ['Hola', 22, 1.5, 'Auto', {'nombre': 'Franco'}] => Se eliminó booooca boooooca ya que el método pop, si no le pasamos parámetros, elimina el último elemento.

#* Pero si aclaramos que elemento deseamos eliminar, simplemente al pop le pasamos por parámetros el índice del elemento que queremos remover. 
mi_lista3.pop(4)
# print(mi_lista3) # ['Hola', 22, 1.5, 'Auto', 'Boooooca Booooooca'] => El objeto con mi nombre estaba en el índice indicado, por eso se ha eliminado.

#* También podemos, por supuesto, almacenar ese elemento eliminado en una variable para luego manipularlo. 
eliminado = mi_lista3.pop(4)
# print(eliminado) # {'nombre': 'Franco'}

#* Vamos a ordenar una lista con el método sort. Este método trabaja con los indices pero NO DEVUELVE NADA. Por eso no se puede hacer lo siguiente:
desorden = ['b', 'm', 'a', 'j', 'c']
listaOrdenada = desorden.sort()
print(listaOrdenada) # None => Nos dice que es un objeto sin valor, veamos su tipo...
print(type(listaOrdenada)) # <class 'NoneType'> => Efectivamente, es un objeto sin valor alguno

#* Entonces como te estarás imaginando, la forma correcta de ordenar sería la siguiente:
desorden = ['b', 'm', 'a', 'j', 'c']
desorden.sort()
print(desorden) # ['a', 'b', 'c', 'j', 'm'] => Se ordenó alfabéticamente

#* Pero si fuese necesario crear otra variable para guardar la lista ordenada, podemos hacer lo siguiente:
desor = ['b', 'm', 'a', 'j', 'c']
desor.sort()
ordenadita = desor
print(ordenadita) # ['a', 'b', 'c', 'j', 'm']

#* También se puede utilizar con números
desorden1 = [3, 5, 9, 1, 2, 7, 4, 6, 8, 10]
desorden1.sort() 
print(desorden1) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#* Lógicamente podemos invertir el orden de la lista:
desorden1.reverse()
print(desorden1) # [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]



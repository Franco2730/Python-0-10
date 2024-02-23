## Para comprender que son los elementos de tipo diccionario, vamos a pensar en un diccionario común donde tenemos: "La palabra": "La definición". Es decir: Palabra clave: valor.
## En Python es bastante parecido ya que un diccionario es una colección de pares siendo que cada par cuenta con una clave y un valor. Las claves son únicas e irrepetibles.  
## Los diccionarios en Python se escriben entre llaves y cada clave estará separada de su valor por dos puntos y los pares estarán separados por una coma entre si.
## A diferencia de las listas, los diccionarios no tienen un orden especifico, no tienen índice. Con lo cual, no importa el orden en que hayas escrito los pares, para Python es irrelevante. No podremos buscar un elemento No podremos buscar un elemento por su índice. El primer elemento tendría el índice 1 a diferencia de otros tipos de datos donde el primer elemento es el indice 0
## ¿Entonces? ¿Cuándo debemos utilizar listas y cuando debemos utilizar diccionarios? 

#* Como dijimos, en los diccionarios no importa el orden, es decir que no se pueden ordenar con los métodos sort o reverse. Entonces una buena ocasión para utilizar un diccionario es cuando queremos almacenar valores a los que podamos acceder sin conocer su ubicación exacta si no, su relación con otro concepto. Por ejemplo si quisiéramos exponer los datos de una persona. 

paciente = {'nombre': 'Manuel',
             'Apellido': 'Pretti',
             'peso': 95.6,
             'talla': 1.75}

print(paciente['talla']) # 1.75

print(paciente['peso']) # 95.6

print(paciente['nombre']) # Manuel

# #  -----

 # Las claves NO SE PUEDEN REPETIR.
 # Los valores SI SE PUEDEN REPETIR

diccionario = {'c1': 'valor1', 'c2': 'valor1', 'c3': 'valor3'}

print(type(diccionario)) # <class 'dict'>
print(diccionario) # {'c1': 'valor1', 'c2': 'valor1', 'c3': 'valor3'}

resultadoBusqueda = diccionario['c2']
print(resultadoBusqueda) # valor1


#* Imaginemos que tenemos un diccionario llamado cliente y queremos hacer consultas acerca de sus datos. Lo podríamos hacer de la siguiente forma  
cliente = {'Nombre': 'Franco', 'Apellido': 'Rosales', 'edad': 30, 'Peso': '90kg', 'Estatura': 1.96}
consulta = cliente['Nombre']
consulta2 = cliente['edad'] 

print(consulta) # Franco
print(consulta2) # 30

# Un diccionario puede contener todo tipo de datos, todos los que hemos aprendido Y todos los que nos falta aprender, un diccionario puede contener listas y puede tener diccionarios en su interior. 

#* En el siguiente diccionario vamos a tener números enteros, arreglos y diccionarios y trataremos de ingresar a cada valor explicando como:
dict = {'c1': 55, 'c2': [10, 20, 30], 'c3': {'cla1': 'valo1', 'cla2': 'valo2'}, 'c4': {'Nombre': 'Franco', 'Apellido': 'Rosales', 'edad': 30, 'Peso': '90kg', 'Estatura': 1.96}}

c1 = dict['c1']
print(c1) # 55 => Así de facil, como ya sabiamos, imprimimos un elemento cuando se encuentra solo.

c2 = dict['c2'][2] # => Acá estamos creando una variable llamada c2 que contendra del dict el elemento c2 en su posicion 2.
print(c2) # 30 

#* No hace falta crear una variable para hacer cualquier consulta, podemos simplemente imprimirlas de la siguiente forma:
print(dict['c3']) # => {'cla1': 'valo1', 'cla2': 'valo2'}
print(dict['c3']['cla2']) # => Acá estamos diciendo: imprimir, del dict el elemento 'c3' pero puntualmente lo que haya en la cla2. Lo que se imprime en pantalla es: valo2
print(dict['c4']['Peso']) # => 90kg

#* Ejercicio: Del siguiente diccionario trata de extraer la letra e pero en mayuscula. 
dicc = {'c1':['a', 'b', 'c'], 'c2':['d', 'e', 'f']}

print(dicc['c2'][1].upper()) # E


#* Como podemos agregar un elemento a un diccionario ya creado ?
dic = { 1: 'a', 2: 'b' }
print(dic) # {1: 'a', 2: 'b'}

dic[10] = 'Marado' # Cuando hacemos esto, como si fuese una consulta, el diccionario se pregunta: El elemento por el cual están preguntando existe ? Si este existe se muestra, si no, se crea.
print(dic) # {1: 'a', 2: 'b', 10: 'Marado'}

#* Tambien podemos sobreescribir un elemento de nuestro diccionario: Directamente PISAMOS la que existe:
dic[2] = 'B'
print(dic) # {1: 'a', 2: 'B', 10: 'Marado'}

#* Y si queremos conocer TODAS las claves de nuestro diccionario? :
print(dic.keys()) # dict_keys([1, 2, 10])

#* Y si queremos conocer TODOS los valores de nuestro diccionario? :
print(dic.values()) # dict_values(['a', 'B', 'Marado'])

#* Y si queremos conocer TODO lo que hay en nuestro diccionario: 
#* El hecho de que los items (elementos) esten entre parentesis nos da una pauta de que, lo que hay dentro de los diccionarios es algo que se llama TUPLES y eso es lo que veremos la clase que viene.
print(dic.items()) # dict_items([(1, 'a'), (2, 'B'), (10, 'Marado')]) 


#* También podemos asignar el contenido de un diccionario a diferentes variables:
diccio = (1, 2, 3, 4, 5)

a, b, c, d, e = diccio

print(a, b, c, d, e) # 1 2 3 4 5 => ¿Qué es lo que ha pasado? Simplemente, al crear un determinado número de valores y ese mismo número determinado de variables, lo que ha sucedido es que se asignan automáticamente. Si tuviera más o menos valores o variables, automáticamente la consola nos arroja un error de que esperaba mas o menos valores o variables. Esto funciona en las listas, diccionarios y tuples





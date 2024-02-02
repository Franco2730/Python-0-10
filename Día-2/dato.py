# Tipos de Datos en Python:

# En Python, los tipos de datos son la categorización de los valores que pueden ser almacenados y manipulados en un programa. Estos tipos de datos son fundamentales para realizar operaciones y almacenar información de manera eficiente. A continuación, te presentaré algunos de los tipos de datos más comunes en Python:

# Cadenas de texto / string (str): Representan secuencias de caracteres, esto se toma como str a todo elemento que esté encerrado entre comillas, sean dobles o simples. Por lo general son un conjunto de letras que conforman una palabra, aunque también puede ser un numero o un bool ("2", "true") pero pierden su tipo de información y no se pueden hacer operaciones ni matemáticas ni boleanas. Ej:
texto = "Hola mundo, soy un string","#%!", "3,14"

# Enteros / integer (int): Representan números enteros, positivos o negativos, sin decimales, que no esté encerrado entre comillas (si no, seria str) la ventaja de esto es que, lógicamente se pueden hacer operaciones matemáticas con ellos. Ej:
numero_entero = 10, 22, 100

# Floating (float): Representan números decimales, como los int también pueden ser positivos o negativos y también se pueden realizar operaciones matemáticas (tampoco pueden estar entre comillas ya que ÚNICAMENTE los str van entre ellas) cualquier número tanto int o float puede ir entre comillas, pero dejan de ser números como tal para ser tratados como letras: uno, dos, tres. Ej:
numero_decimal = 3.14, -1.25, 8.00

# Listas (lst): La lista es una colección ordenada de objetos, las listas se escriben entre corchetes y pueden contener objetos de todos tipos, pueden ser muchos str, int o una colección de muchos tipos de datos. Lo importante es que sus elementos tienen un orden y esto es fundamental ya que cada elemento tiene un índice (del 0 al que tenga.) Ej: el str marte tiene el índice 4
lista_numeros = ["sal", 2, -3,  14, "martes", "franco"]
                #  0    1   2    3     4         5

# Tuples (tup): Se los escribe entre paréntesis y son muy parecidos a las listas, ya que son un conjunto ordenado de elementos y estos elementos pueden contener cualquier tipo de datos, pero tienen una gran diferencia y es que su orden es inmutable. En las listas hay métodos que nos permiten agregar, eliminar y hasta ordenar los elementos. Los tuples son intocables. 
tupla_colores = ('rojo', 'verde', 'azul')

# Diccionarios (dic): Este tipo de datos se lo define como dic, y su contenido va entre llaves. Los dic consisten en pares de palabras agrupados, cada par contiene una clave y un valor. Como si pensáramos en un diccionario común, donde vemos una palabra (clave) y a continuación su descripción y/o explicación (valor). Importante recalcar que los pares NO están ordenados dentro de los diccionarios y cada par tiene su orden interno 
diccionario_edades = {'Juan': 25, 'Color': 'rojo', 'Carlos': 22, 'Arte': 'Cine'}

# sets (set): Se los escribe entre llave y un set es un conjunto ordenado ÚNICO. Tanto las listas como los tuples pueden tener elementos repetidos más no los sets. Acá cada elemento es único e irrepetible. 
conjunto_vocales = {'a', 'e', 'i', 'o', 'u'}

# Booleanos (bool): Estos son valores muy sencillo, pueden tener únicamente dos valores. verdadero o falso (true o false). Esto es muy util para cuando necesitamos que nuestro código tome decisiones. Para saber si una condición se cumple (true) o no se cumple (false).
es_verdadero = True


# Notas Adicionales:

#     Mutable vs Inmutable:
#         Los datos mutables pueden cambiar después de su creación (por ejemplo, listas y diccionarios).
#         Los datos inmutables no pueden cambiar después de su creación (por ejemplo, enteros, flotantes y tuplas).

#     Indexación:
#         Muchos tipos de datos (como listas y cadenas de texto) son indexables, lo que significa que puedes acceder a elementos específicos utilizando índices.

#     Operaciones y Métodos:
#         Cada tipo de dato tiene operaciones y métodos específicos asociados que puedes realizar.

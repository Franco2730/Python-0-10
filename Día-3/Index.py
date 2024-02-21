# # Un string es una secuencia de caracteres, con lo cual, cada caracter tiene un lugar, un indice determinado. Toda cadena comienza con un indice 0. Es decir: "Hola mundo" tiene 10 caracteres ya que el espacio cuenta como un caracter. la letra H esta en la posición 0 y la letra m en el indice 5. Veamos como hacerlo con el primer método que aprenderemos hoy.

mi_texto = "Hola mundo"

print(mi_texto.index("o")) #1 -> Ya que toma la primer coincidencia.
print(mi_texto.index("m")) #5

# Si quisieramos saber, en vez de en que posición está la letra m, como podemos preguntar: ¿Qué hay en la posicion 3?

print(mi_texto[3]) #a
print(mi_texto[6]) #u

# También podemos utilizar indices negativos, recordando que la primer letra corresponde al indice 0, números negativos comenzarian de derecha a izquierda:

print(mi_texto[-9]) #0
print(mi_texto[-6]) # " " -> espacio vacío.

# También le podemos pedir que busque algo en particular y darle parametros, es decir, decirle desde donde hasta donde puede buscar:

otro_texto = "Este es otro texto de prueba"

print(otro_texto.index('e', 21, 27)) #25 -> Le pedimos al programa que analice a partir del caracter 21 hasta el caracter 27. De esa forma, omitió 5 coincidencias de letra e.

# En vez de utilizar números negativos, podemos utilizar el metodo rindex() es igual al método index con la única diferencia que analiza de derecha a izquierda, las posiciones del string siguen siendo primera letra index 0. 

mi_texto_revez = "Hola mundo"

print(mi_texto_revez.rindex("o")) #9 -> Ya que toma la primer coincidencia.
print(mi_texto_revez.rindex("m")) #5
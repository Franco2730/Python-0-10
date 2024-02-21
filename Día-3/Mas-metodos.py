# Hasta ahora hemos aprendido a usar los métodos Indes y Format. En esta clase aprenderemos:

#* - upper() -> Pasar un texto a mayúsculas.
#* - lower() -> Pasar a minúsculas.
#* - split() -> Separa en partes (listas).
#* - join() -> Unir items usando separador, ya veremos mas de que se trata.
#* - find() -> Encontrar un sub-string
#* - replace() -> Reemplazar un substring

#! Estos son solo 8 métodos de más de 30 que hay para manipular los strings, no vamos a entrar en detalle con cada uno ya que algunos no se utilizan demasiado y por un tema de tiempo. En el archivo Métodos de Strings.pdf encontrarás todos los métodos existentes por si los quieres tener a mano :D

texto = "Este es el texto del profe Fran"

mayus = texto
mayus2 = texto.upper() #ESTE ES EL TEXTO DEL PROFE FRAN
# Y si traemos un concepto de la clase pasada ? Como podemos hacer si queremos colocar en mayusculas el nombre Fran ? 
mayus3 = texto[27 : ].upper() # FRAN

minuscula = texto.lower() # este es el texto del profe fran -> Sacó las mayusculas del principio y del nombre. Pasa todo a minusculas.

#* El siguiente método separa los elementos del str y los coloca como elementos separados en una lista: Dicho método, al no colocarle parametros este separa los elementos tomando como parametro los espacios vacios. Diferente será el segundo ejemplo:
separar = texto.split() # ['Este', 'es', 'el', 'texto', 'del', 'profe', 'Fran']
separar2 = texto.split('e') # ['Est', ' ', 's ', 'l t', 'xto d', 'l prof', ' Fran']

#* El siguiente método es para unir cadenas de carácteres, por el contrario de split. Lo que verémos a continuación es como unir strings con el método join. 
#* En las variables e y e2 podemos ver como hay comillas vacías y con un guión, esto significa que yo le pedí que juntara el contenido de las variables que detalle en los corchetes SEPARADOS por lo que hay dentro de esas comillas. Si dejamos comillas vacías, será un espacio vacío, si no, lo que pongamos.
a = "Aprender"
b = "Python"
c = "es"
d = "grandioso !!"
e = " ".join([a, b, c, d]) # Aprender Python es grandioso !!
e2 = "-".join([a, b, c, d]) # Aprender-Python-es-grandioso !!

#* El siguiente método es find(), este busca un determinado caracter dentro de nuestro str, es muy similar al método index(). La diferencia entre ellos es que si utilizamos find para encontrar un elemento que no existe en nuestro str nos da como resultado -1 mientras que si lo hacemos con index() nos devuelve un error.
encontrar = texto.find('F') #27
encontrar = texto.find('i') #-1 -> Ya que no existe la i en nuestro texto, nos devuelve -1

#* El siguiente método sirve para reemplazar un fragmento del texto y cambiarlo por otro, este método requiere 2 parametros, el primer parametro será la palabra que quiero reemplazar y el segundo parametro la palabra que necesito colocar en su lugar. Tambien lo podemos hacer con letras, es decir si en el primer parametro colocamos la letra e y en el segundo la letra X, la letra x reemplazará todas las letras e.
reemplazar = texto.replace('Fran', 'Conan') # Este es el texto del profe Conan
reemplazar2 = texto.replace('e', 'x') # Estx xs xl txxto dxl profx Fran -> No reemplazó la primer 'E' ya que es mayuscula y no es el mismo elemento. 

print(reemplazar2) 




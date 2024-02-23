# Un elemento de tipo booleano puede tener dos valores: Verdadero o False. Este tema es extremadamente importante ya que nos ayudará a que nuestros programas vayan tomando sus propias decisiones.

# Podemos declarar estos valores de forma directa o indirecta. Si los declaramos de forma directa quedaría algo como: True y False SIEMPRE CON MAYUSCULA LA PRIMERA LETRA
# Mi_bool = True 
# Mi_bool = False
# Si lo declaramos de forma indirecta quedaría algo como:
# Mi_bool = 5 > 4 --> esto es True
# Mi_bool = 5 < 4 --> esto es False

# Las expresiones que permiten establecer comparaciones son los signos:
# -	>	Mayor que
# -	<	Menor que
# -	>=	Mayor o igual que
# -	<=	Menor o igual
# -	=	Igual que
# -	¡=	Diferente

# Cada vez que vayamos a construir una variable utilizando esas expresiones, el resultado será un resultado de tipo booleano.  
#* Booleano de forma directa:
mi_bool = True
mi_bool = False
print(type(mi_bool)) # <class 'bool'>

#* Booleano de forma indirecta: Acá se puede jugar con todas las expresiones que vimos al principio. Te lo dejo de tarea ;)
numero = 5 > 2 + 3
print(numero) # False
print(type(numero)) # <class 'bool'>

#* Podemos obtener un resultado booleano en una lista:
lista = [1, 2, 3, 4]
control = 5 in lista
control2 = 5 not in lista

print(type(control)) # <class 'bool'>
print(control) # False -> Es falso que 5 se encuentra en lista
print(control2)# True -> Es true que 5 no se encuentra en lista.


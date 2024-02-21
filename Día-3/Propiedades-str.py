# Los Strings son inmutables. 

# Los strings son capaces de concatenarse con el signo +.

# Tambien pueden tener mas de una línea con 3 comillas simples '''

# Podemos verificar si un str contiene una cadena de caracteres Ejemplo:
        # mi_texto = "Hola mundo"
        # print("Hola" in mi_texto) => True

# Podemos calcular el largo de un string, es decir, decir cuantos caracteres contiene. Ejemplo:
        # mi_texto = "Hola mundo" 
        # print(len(mi_texto)) => 10

# Digamos que el nombre de mi madre no se escribe con K si no, con C. #! Pero el siguiente ejemplo nos devolverá un error ya que, como habiamos dicho al principio de esta lección, los strings son inmutables.

nombre = "Karina"
# nombre[0] = "C"
# print(nombre) => Error. 

#* Una forma correcta de hacerlo, sería cambiar el contenido de la variable, es decir, pisar la información erronea de la misma variable.
nombre = "Carina"
print(nombre) # Carina

#* Veamos como podemos concatenar (aunque esto ya lo sabemos hacer):
n1 = "Fran"
n2 = "co"
print(n1 + n2) # Franco

#* También podemos multiplicar un str. Por ejemplo:
curso = "Python es lo mejor, en serio que " * 10
print(curso) # Python es lo mejor, en serio que Python es lo mejor, en serio que Python es lo mejor, en serio que Python es lo mejor, en serio que Python es lo mejor, en serio que Python es lo mejor, en serio que Python es lo mejor, en serio que Python es lo mejor, en serio que Python es lo mejor, en serio que Python es lo mejor, en serio que 

#* Veamos como podemos hacer el salto de línea con las 3 comillas simples:
poema = '''Mil pequeños peces blancos
como si hirviera
el color del agua'''

print(poema)
# Mil pequeños peces blancos
# como si hirviera
# el color del agua

#* Algo muy útil es que podemos corroborar si dentro de una cadena de carácteres hay un sub string. Vamos a utilizar el poema anterior:
print("agua" in poema) #True => ya que si se encuentra agua en poema
print("sol" in poema) #False => ya que no se encuentra sol en poema

#*También podemos preguntar si algo NO SE ENCUENTRA:
print("soldado" not in poema) #True => Es verdad que NO SE ENCUENTRA
print("color" not in poema) #False => Es mentira que NO SE ENCUENTRA ya que si se encuentra

#* Como podríamos corroborar el largo de los carácteres de un string:
frase = "Hola mundo"
frase2 = "Hola mundo.."

print(len(frase))  #10
print(len(frase2)) #12 
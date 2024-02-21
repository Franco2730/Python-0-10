# #* En esta lección, vamos a aprender a extraer una parte de un str para manipular a nuestra necesidad. Esta práctica se la conoce como: Slicing (rebanar) Los pasos son similares a los que vimos en la clase pasada con el método Index. Ahora veamos:

# mi_variable = "Esta palabra será extraída"
# print(mi_variable[5 : 12]) # palabra -> palabra fue extraída ya que le pedimos al programa que, en la variable mi_variable, extraiga lo que haya entre el carácter 5 y 12. El primer parámetro incluye a su carácter, mientras que el segundo parámetro no lo hace, con lo cual, hay que colocar un indice mayor al carácter que queremos extraer. En otras palabras, si tengo un str "Hola" y lo quiero extraer, debo colocar 0 : 5 

# # También podemos brindar un tercer factor, si colocamos dos puntos serían las letras que queremos saltear:

# ejemplo = "0123456789"
# print(ejemplo[0 : 10 : 2]) #02468 -> Le pedimos que tome desde el primer elemento en la posición 0 hasta la posición 10 pero que vaya de 2 en 2. Con lo cual, agarro los números pares en este caso. 

ultimo = "Ahora vamos a escribir un texto un poco más extenso jejeje"
print(ultimo[0 : ]) # Ahora vamos a escribir un texto un poco más extenso jejeje -> Al no colocarle el segundo factor, el programa entiende que tiene que tomar hasta el último carácter de la cadena ya que no siempre sabremos la cantidad de caracteres que tiene nuestro str. Lo mismo ocurre si no colocamos el primer factor y si el último, si colocamos en este ejemplo:
print(ultimo[ : 58]) # Se va a imprimir todo el texto. Lo mismo pasaría si le pusiéramos el tercer factor para ir de 2 en 2, de 3 en 3 y así.


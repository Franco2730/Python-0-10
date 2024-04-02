# Los operadores de comparación son herramientas fundamentales en programación que permiten comparar valores y determinar relaciones entre ellos. Estos operadores evalúan las expresiones y devuelven un resultado booleano (True o False) que indica si la comparación es verdadera o falsa.

# Los operadores de comparación más comunes en Python son:
x = 5
y = 5
#     Igualdad (==): Comprueba si dos valores son iguales.

# Ejemplo de igualdad:

if x == y:
    print("x es igual a y")

# Desigualdad (a=): Comprueba si dos valores son diferentes.
a = 10
b = 20
# Ejemplo de desigualdad:

if a != b:
    print("a no es igual a b")

# Comprueba si un valor es mayor que otro.
edad = 18
# Ejemplo de mayor que:

if edad > 17:
    print("Es mayor de edad")

# Menor que: Comprueba si un valor es menor que otro.
temperatura = 25
# Ejemplo de menor que:

if temperatura < 30:
    print("La temperatura es baja")

# Comprueba si un valor es mayor o igual que otro.
num1 = 15
num2 = 10
# Ejemplo de mayor o igual que:

if num1 >= num2:
    print("num1 es mayor o igual que num2")

# Menor o igual que (<=): Comprueba si un valor es menor o igual que otro.
saldo = 1000
gasto = 1200
# Ejemplo de menor o igual que

if saldo <= gasto:
    print("No tienes suficiente saldo")

# Estos operadores de comparación son esenciales para controlar el flujo de un programa y tomar decisiones basadas en las relaciones entre los valores. Nos permiten construir condiciones que guían el comportamiento de nuestro código de manera eficiente y precisa.
    
#* Veamos más ejemplos: 
    
#todo ¿Cual es la diferencia entre = y ==? 

#* Operador de ASIGNACIÓN:
    
mi_variable = 'Hola mundo' # Un solo signo de igual es un término de ASIGNACIÓN. Es decir: Decimos que, por favor, a mi_variable se le asigne el valor del str Hola mundo.

#* Operador de COMPARACIÓN:

10 == 20 # Al colocar dos signos igual, no estamos asignando, más bien, es como una pregunta. ¿El número 10 es igual al número 2? Su respuesta será un booleano.
print('Otros ejemplos:\n')
#* Mezclamos ambos comparadores:

mi_booleano = 10 == 20 # Si imprimimos en consola esta variable nos daremos cuenta que, lo que en realidad estamos haciendo es: Asignarle, a la variable mi_booleano la comparación de 10 y 20. Es decir: a dicha variable le asignamos el booleano (True / False) que resulte de la comparación que tiene como valor. 
print(mi_booleano) #! False

otro_bool = 10 == 5 + 5
print(otro_bool) #* True => Se comparó un número con una operación matemática cual resultado dio ese mismo número

otro_bool2 = 'blanco' == 'Blanco'
print(otro_bool2) #! False => Al tener la B mayúscula y minúscula el str no es el mismo.

otro_bool3 = 'blanco' == 'Blanco'.lower()
print(otro_bool3) #* True => al aplicarle al segundo str el método lower, transformamos su mayúscula en minúscula, con lo cual, ambos str son iguales.

otro_bool4 = '100' == 100
print(otro_bool4) #! False => No es lo mismo un INT de un STR

otro_bool5 = 100.0 == 100
print(otro_bool5) #* True => Si bien uno es FLOAT y el otro es INT. Ambos tienen el mismo valor. Son iguales.

#todo. Veamos el operador de DIFERENCIA (! =) 
# Debido a una extensión que cuento en mi editor de código, el operador de diferencia es un signo de exclamación seguido de un signo de igual sin espacio entre si. Debido a mi extensión, dicho operador se verá de la siguiente forma: != Y esto es exactamente lo mismo que lo anterior pero, por lógica, todo lo contrario.

mi_bool = 100 != 100 #! False => Ambos INT son iguales

mi_bool2 = 100 != '100' #* True => Es verdadero que son DIFERENTES ya que uno es INT y el otro STR.

#todo. Después tenemos los signos mayor, menor y esto respeta las leyes matemáticas. 

mi_bool3 = 100 < 50 #! False => Es falso que 100 es menor que 50

mi_bool4 = 100 > 10 #* True => Es verdadero que 100 es mayor que 10

#todo. Que sucede cuando queremos preguntar si es menor o igual (< =) <=. O tal vez queremos preguntar si es mayor o igual: (> =) >=

mi_bool5 = 18 >= 18 #* True => Es verdadero que 18 es mayor O IGUAL a 18

mi_bool6 = 19 <= 15 #! False => Es falso que 19 es menor o igual a 15.


#* Hay otra situación bastante típica y cotidiana que nos podemos encontrar y es que sucede si queremos hacer más de una comparación? Es decir, que sucede si, por ejemplo:
#* Queremos preguntar: ¿Tenes 18 años o más O venís con tus padres? En este ejemplo estamos haciendo dos comparaciones:

edad = 18 >= 18 # => Si esto da True la primera condición se cumple
# viene_con_padres = True o False => Depende la condición es si se cumple o no.

#* En la próxima clase estaremos viendo como juntar dos comparaciones como el ejemplo anterior:



# En la siguiente consigna, no estamos dando una comparación si no, una orden. estamos asignamos un valor a una variable.
notaFranco = 5.5

# Si queremos comparar, vamos a colocar doble signos iguales para preguntar si algo es igual a algo, por ejemplo:
mi_bool = 100 == 100 # Esto daría como resultado True... ya que 100 es igual a 100

# Tambien podemos comparar strins:
mi_bool2 = "Blanco" == "blanco" # => False, ya que Python es sensible a mayusculas, para que sea True debemos:
mi_bool3 = "Blanco" == "blanco".lower() # => Acá daría True ya que transformamos todos los caracteres en minusculas. 

if notaFranco >=7.0:
    print("Felicitaciones Dani !!!\n\n")
else:
    print("No vas a recibir ningun regalo \n\n")


# temperatura = 1000

# if temperatura >= 40:
#     print("Vamos a la playa a bañarnos\n\n")
# elif temperatura >=20:
#     print("Vamos al parque por una gaseosa\n\n")
# else:
#     print("Juguemos dentro de casa\n\n")

#* Hasta ahora sabemos pasar argumentos a funciones pero, como hacemos para que una función tome tantos argumentos como el usuario vaya a pasar: Simplemente con dos comandos: *args / **kwargs.

#* Ahora vamos a ver a "*args" esto viene de la palabra argumentos, y esto significa que la cantidad y calidad de argumentos que una función recibirá por parámetro será variable a las necesidades del usuario.

#* Por ejemplo, en el siguiente ejemplo veremos como una función recibe por parámetro a *args y esto hace referencia a que le podemos pasar por parámetro la cantidad de elementos que nosotros queramos y en el cuerpo de dicha función, el código especifica que vamos a iterar sobre cada uno de esos elementos sin importar, como bien dijimos, de su cantidad:

def suma(*args):
    for numerito in args:
        print(numerito)

# suma(1, 3, 9, 10, 20, 33, 48, 59, 79, 112)

# 1
# 3
# 9
# 10
# 20
# 33
# 48
# 59
# 79
# 112


#* Otros ejemplos, comenzando con los ya conocidos dos elementos:

def suma2(a, b):
    return a + b

# print(suma2(10, 20)) # => 30


#* Pero y que sucede si el usuario le brinda un tercer parámetro al momento de llamar a la función? La consola nos devolverá un error que dice: Hay 2 posiciones para los argumentos, pero fueron pasados 3.

def suma3(a, b):
    return a + b

# print(suma3(10, 20, 30)) # => TypeError: suma3() takes 2 positional arguments but 3 were given


#* Volvemos a ejemplificar un ejemplo con un args:

def suma4(*args):
    total = 0

    for argumentito in args:
        total = total + argumentito
    return total

# print(suma4(10, 20, 30, 40, 50, 60, 70, 80, 90, 100)) # => 550


#* Hay que tener en cuenta que lo importante es el asterisco ya que este dice TODOS los args. Pero perfectamente podemos poner otra palabra:

def suma5(*empanadas):
    sum = 0
    for empanadita in empanadas:
        sum = sum + empanadita
    return sum

# print(suma5(10, 5, 10)) # => 25

#* tareas:

#* Crea una función llamada suma_cuadrados que tome una cantidad indeterminada de argumentos numéricos, y que retorne la suma de sus valores al cuadrado.

#* Por ejemplo para los argumentos suma_cuadrados(1,2,3) deberá retornar 14 (1+4+9).

def suma_cuadrados(*args):
    res = 0
    for i in args:
        res = res + i ** 2
    return res
        
# print(suma_cuadrados(1,2,3))


#* Crea una función llamada suma_absolutos, que tome un conjunto de argumentos de cualquier extensión, y retorne la suma de sus valores absolutos (es decir, que tome los valores sin signo y los sume, o lo que es lo mismo, los considere a todos -negativos y positivos- como positivos).

def suma_absolutos(*argumentos):
    res = 0
    for i in argumentos:
        res = res + abs(i)
    return res

# print(suma_absolutos(-10, 10, 20)) # => 40



#* Crea una función llamada numeros_persona que reciba, como primer argumento, un nombre, y a continuación, una cantidad indefinida de números.
#* La función debe devolver el siguiente mensaje:
#* "{nombre}, la suma de tus números es {suma_numeros}"

def numeros_persona(nombre, *args):
    suma_numeros = sum(args) # la función sum: Se utiliza para calcular la suma de todos los elementos en una lista, tupla u otro iterable.
    return f'{nombre}, la suma de tus números es {suma_numeros}'

# print(numeros_persona("Franco", 1, 2, 3, 6, 12, 1, 25, 50, 900)) # => Franco, la suma de tus números es 1000




#* Argumentos indefinidos **kwargs: Su correcta pronunciación es: 'Key Word args' y esto nos da una idea de que tipo de dato maneja. Ya que si tiene una palabra clave estamos usando UN DICCIONARIO.

def newFuncion(**kwargs):
    return kwargs


# print(newFuncion(clave1= 1, clave2= 2, clave3 = 3)) # => {'clave1': 1, 'clave2': 2, 'clave3': 3}



#* Vamos con otros ejemplos. Vamos a crear una función que pase por todos los elementos pasados como parametro y haremos que se muestren en pantalla y ademas de eso, sumar su valor.

def newFuncion2(**kwargs):
    total = 0

    for clave, valor in kwargs.items():
        print(f"{clave} = {valor}")
        total = total + valor
    return total

# print(newFuncion2(a = 10, b = 100, c = 1000, d = 10000))

# a = 10
# b = 100
# c = 1000
# d = 10000
# 11110 => total = total + valor



#* Ahora vamos a crear una función que mezcle parametros normales (num1, num2) ese tipo de parametros, un *args y un **kwargs. TODO JUNTO y si !! asi es el orden que debemos cuidar. Si llegamos a pasar todo junto por parametros, es primordial saber que primero van los parametros normales, luego el *args y por ultimo el key word args. 

def prueba(num1, num2, *args, **kwargs):

    print(f'El primer valor es: {num1}')
    print(f'El segundo valor es: {num2}')

    for cadaArgumento in args:
        print(f' El tercer valor es el argumento = {cadaArgumento}')

    for clave, valor in kwargs.items():
        print(f'El cuarto valor son los sig args: {clave} = {valor}')


# prueba(10, 20, 100, 200, 300, key1 = 1000, key2 = 2000, key3 = 3000)


#* El primer valor es: 10
#* El segundo valor es: 20

#* El tercer valor es el argumento = 100
#* El tercer valor es el argumento = 200
#* El tercer valor es el argumento = 300

#* El cuarto valor son los sig args: key1 = 1000
#* El cuarto valor son los sig args: key2 = 2000
#* El cuarto valor son los sig args: key3 = 3000




#* Tarea:


#* Crea una función llamada cantidad_atributos que cuente la cantidad de parémetros que se entregan, y devuelva esa cantidad como resultado.

def cantidad_atributos(**kwargs):
    total = 0
    for i in kwargs:
        total = total + 1
    return total

# print(cantidad_atributos(a = 1, b = 2, c = 3)) # 3




#* Crea una función llamada lista_atributos que devuelva en forma de lista los valores de los atributos entregados en forma de palabras clave (keywords). La función debe preveer recibir cualquier cantidad de argumentos de este tipo.

def lista_atributos(**kwargs):
    mi_lista = list(kwargs.values())
    return mi_lista

print(lista_atributos(a = 1, b = 2, c = 3))




#* Crea una función llamada describir_persona, que tome como parámetros su nombre y luego una cantidad indetermida de argumentos. Esta función deberá mostrar en pantalla:

#* Características de {nombre}:
#* {nombre_argumento}: {valor_argumento}
#* {nombre_argumento}: {valor_argumento}
#* etc...
#* Por ejemplo:

#* describir_persona("María", color_ojos="azules", color_pelo="rubio")

#* Mostrará en pantalla:

#* Características de María:
#* color_ojos: azules
#* color_pelo: rubio

def describir_persona(name, **kwargs):
    print(f'Caracteristicas de {name}:')
    
    for clave, valor in kwargs.items():
        print(f'{clave}: {valor}')

describir_persona('Franco', color_ojos = 'marron', color_pelo = 'castaño')


from random import choice

#* Bienvenidos al juego de: El Ahorcado :D 
#* Lo primero que vamos a hacer es crear una lista con palabras que el sistema tendrá a su disposición para elegir una

palabras = ["ventrílocuo", "auto", "velocidad", "metacrilato", "electroencefalografista", "guitarra", "python", "programacion", "otorrinolaringólogo", "musica"]

#* Vamos a necesitar una variable que contenta las letras correctas (las letras con las que el usuario haya acertado).
letras_correctas = []

#* Otra variable serán las letras incorrectas que el usuario ha errado
letras_incorrectas = []

#* Las próximas variables seran sobre las vidas (la vamos a inicializar en 6 ya que todavía no ha perdido ninguna "vida"), los aciertos y la variable que especificará que el juego ha terminado.

intentos = 6

aciertos = 0

juego_terminado = False


#* Vamos a definir una Fn que reciba una lista de palabras por parametro para que pueda seleccionar aleatoriamente alguna de ellas. 
def elegir_palabra(lista_palabra):
    # vamos a crear una variable que va a contener una palabra de la lista que la fn recibió por parametro con la ayuda del metodo choice
    palabra_elegida = choice(lista_palabra)
    # La sig. variable contendrá las letras que no se han repetido en la palabra. y ademas su diametro
    letras_unicas = len(set(palabra_elegida))

    return palabra_elegida, letras_unicas


#* Fn donde se le pedirá una letra al usuario:
def pedir_letra():

    while True:
        letra_elegida = input("Dime una letra: ").lower()
        if len(letra_elegida) == 1 and letra_elegida.isalpha():
            return letra_elegida
        else:
            print("Por favor, ingresa una sola letra válida.")

    return letra_elegida


    # Otra alternativa bastante legible acerca de la función pedir:letra() podría ser:
    '''def pedir_letra():
            letra_elegida = ''
            es_valida = False
            abecedario = 'abcdefghijklmnñopqrstuvwxyz'

            while not es_valida:
                letra_elegida = input("Elige una letra: ).lower()
                if letra_elegida in abecedario and len(letra_elegida) == 1:
                    es_valida = True
                else:
                    print("No has elegido una letra correcta")
            return letra_elegida            

    '''


#* La proxima Fn se va a encargar de mostrar el tablero. (un guión por cada letra):
# Esta función recivirá la palabra elegida que el sistema seleccionó para comparar los lugares y simular la palabra pero con guiones
def mostrar_nuevo_tablero(palabra_elegida):

    lista_oculta = []

    for l in palabra_elegida:
        if l in letras_correctas:
            lista_oculta.append(l)
        else:
            lista_oculta.append('_')
    print(' '.join(lista_oculta))


#* La sig Fn sirve para chequear si la letra que ingreso el usuario está en la palabra. Esta Fn es muy importante ya que determinará si tenemos que agregar la letra a la variable de aciertos o si le debemos descontar una vida al jugador o si este ha ganado...
# Primero vamos a definir dicha funcion con algunos parametros, recordemos que esos parametros pueden tener cualquier nombre, yo le puse algunos nombres significativos pero no tienen que ver con el resto del programa como tal. 
def chequear_letra(letra_elegida, palabra_oculta, vidas, coincidencias):
    # Inicializamos una variable como False porque todavia seguimos jugando. 
    fin = False

    if letra_elegida in palabra_oculta and letra_elegida not in letras_correctas:
        letras_correctas.append(letra_elegida)
        coincidencias = coincidencias + 1

    elif letra_elegida in palabra_oculta and letra_elegida in letras_correctas:
        print("Ya has elegido esa letra herman@")
        
    else:
        letras_incorrectas.append(letra_elegida)
        vidas = vidas - 1
    
    if vidas == 0:
        fin = perder()
    elif coincidencias == letras_unicas:
        fin = ganar(palabra_oculta)
    
    return vidas, fin, coincidencias


def perder():
    print("Te has quedado sin vidas... :( ")
    print("La palabra secreta era: ",palabra)

    return True


def ganar(palabra_descubierta):
    mostrar_nuevo_tablero(palabra_descubierta)
    print("¡¡¡ Has ganado, felicitaciones !!!")

    return True


#* Ya creamos todas las funciones, a continuación deberemos unir todas las funciones:

#* Lo primero, es que el programa elija una palabra aleatoria, con lo cual, debemos ejecutar la Fn: elegir_palabra(): dicha funcion los solicita una lista por parametros, asique, utilizaremos la lista que creamos al principio. 
#* Tambien debemos recordar que nos retorna la función, y esta retorna la palabra como tal y las letras únicas de esa palabra, entonces, debemos guardar la ejecución 
palabra, letras_unicas = elegir_palabra(palabras)

while not juego_terminado:
    print("\n" + "x" * 20 + "\n")
    mostrar_nuevo_tablero(palabra)
    print("\n")
    print("Letras incorrectas: ", '-'.join(letras_incorrectas))
    print(f'Vidas: {intentos}')
    print("\n" + "x" * 20 + "\n")

    letra = pedir_letra()

    intentos, terminado, aciertos = chequear_letra(letra, palabra, intentos, aciertos)

    juego_terminado = terminado



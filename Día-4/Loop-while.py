
#* Así como los bucles for se ejecutan por una cantidad definida de veces, podemos decir que los bucles While se ejecutan mientras se cumpla una condición y dejan de iterar cuando esa condición ha dejado de cumplirse. Y si prestamos atencion a la palabra que acabo de decir: MIENTRAS...

#* While en ingles significa mientras y una caracteristica de este tipo de bucles es que no podemos preveer cuantas veces se va a ejecutar puesto que dependera de algo que puede ser dinamico, por ejemplo:

# Todos los juegos (o la mayoria) el protagonista cuenta con una barra de salud o vidas. El juego se reiniciará WHILE (mientras) que la cantidad de vida sea mayor a cero. Caso contrario, reiniciar para darle otra oportunidad al jugador. Cuando la condicion deje de cumplirse (la cantidad de vida llegue a cero) se dejará de reiniciar el juego para mostrar en pantalla: GAME OVER. Su sintaxis es:

# mientas una_condicion_se_cumpla:
#     un_codigo
# si no:
#     otro codigo

#* Hay que tener MUCHO cuidado con el bucle WHILE, ya que debemos manejar muy bien el corte de la condición. En caso de que no especifiquemos que una condicion llegue a su fin, tendremos un bucle infinito.

# monedas = 5

# while monedas > 0:
#     print(f"Tengo {monedas} monedas")
#     monedas -= 1 # Esta linea es fundamental para evitar ingresar en un loop infinito, es lo mismo que colocar monedas = monedas - 1. Se puede leer: que monedas es igual a la cantidad que tengo en esa variable menos 1
# else:
#     print('No tengo mas dinero')


# Tengo 5 monedas
# Tengo 4 monedas
# Tengo 3 monedas
# Tengo 2 monedas
# Tengo 1 monedas
# No tengo mas dinero 

# respuesta = 's'

# while respuesta == 's':
#     respuesta = input("Quieres seguir ? (s / n)").lower()
# else:
#     print("Gracias !!")


#* Existen 3 palabras que esto aplica TANTO para el loop FOR como para el loop WHILE y estas son:

#* PASS: (Cuando no sabemos que colocar en el cuerpo de un bucle) esta palabra reservada no hace nada, simplemente guarda el lugar para cuando necesitemos completar. Si dejamos un bucle sin cuerpo nos podría dar un error, con pass es como si no hubiera nada, pero guarda su lugar.

#todo. En el siguiente ejemplo nos daría un error: IndentationError: expected an indented block. Ya que no podemos dejar un bucle vacío. 
# respuesta = 's'

# while respuesta == 's':

# print("Hola")

#* Para remediar esto, tenemos la palabra pass: No habrá error alguno y el codigo estará listo para cuando nosotros queramos completarlo. 

respuesta = 's'

while respuesta == 's':
    pass

print("Hola")

#* BREAK: (Quiere decir interrumpir) Estamos interrumpiendo la iteración actual del loop en el que estamos para salir directamente de este. Por ejemplo, en el siguiente codigo, como ya sabemos, se va a imprimir letra por letra del ingreso del usuario:

nombre = input('Tu nombre: ') # franco

for letra in nombre: 
    print(letra)

# f
# r
# a
# n
# c
# 0


#* Pero que pasa si nosotros queremos que, al momento de detectar una letra en particular, interrumpamos y termine el código:

nombre = input('Tu nombre: ') # franco

for letra in nombre: 
    if letra == 'c':
        break
    print(letra)

# f
# r
# a
# n

#* CONTINUE: Esto, como su nombre nos indica significa continuar y lo que hace es similar a la acción de break ya que interrumpe la iteración actual pero no interrumpe el loop en si mismo si no, que vuelve al comienzo y continua con la iteracion siguiente. Ejemplo: Tomando el ejemplo anterior, en vez de CORTAR el loop cuando este encuentre la letra 'c'. Lo que hará CONTINUE es saltear esa iteración, saltear la iteración donde se cumpla la condición y continuar con la ejecución:

nombre = input('Tu nombre: ') # franco

for letra in nombre: 
    if letra == 'c':
        continue
    print(letra)

# f
# r
# a
# n
# o


# Para entender que es una variable pensemos en una caja. Una caja donde podamos guardar nuestro libro favorito.
libroFavorito = "GOT - A Feast for Crows"

# Pero como dijimos anteriormente, las variables son como cajas, las cajas se abren y podemos cambiar su contenido, exactamente igual que las variables, el contenido de esas cajas pueden variar (por eso se llaman variables)
libroFavorito = "GOT - A Dance with Dragons"

# Las variables en la programación, son un pequeño espacio de programación donde nosotros podemos agregar contenido o tal vez, dejar vacío para agregar algo más tarde.

# Tambien podemos hacer una operación matemática:
edad = 20
edad2 = 40

sumar = edad + edad2 

# print(sumar) # => 60


#En el siguiente ejemplo veremos la diferencia entre lo que hicimos con la variable sumar, y lo que sucede cuando un int se convierte en un str:

edad3 = "20"
edad4 = "40"

sumar2 = edad3 + edad4

print(sumar2) # => 2040


# Que sucede cuando queremos pedirle información al usuario (como vimos en la clase pasada para la marca de gaseosa) pero queremos retener esa información en alguna cajita ?

estacion = input("Dime tu estación favorita: ")

print("Tu estacion favorita es " + estacion) # => - Dime tu estación favorita: Invierno
                                             #    - Tu estacion favorita es Invierno

# También podemos sumar palabras, que en programación se conoce como CONCATENAR, es decir, podemos juntar muchos strings para formar un saludo:

nombre1 = input("Dime tu nombre: ") # => Franco
nombre2 = input("Dime el nombre de tu amigo: ") # => Luciano

print(nombre1 + " y " + nombre2 + " son dos usuarios activos.") # => Dime tu nombre: Franco
                                                                #    Dime el nombre de tu amigo: Luciano
                                                                # Franco y Luciano son dos usuarios activos.



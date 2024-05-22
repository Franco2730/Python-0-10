# isalpha() es un método de cadena en Python que se utiliza para verificar si todos los caracteres en una cadena son caracteres alfabéticos. Devuelve True si todos los caracteres en la cadena son letras del alfabeto (a-z o A-Z), y False si la cadena contiene al menos un carácter que no es una letra.

# Aquí hay un ejemplo de cómo se usa el método isalpha()

cadena1 = "Hola"
cadena2 = "Hola123"

print(cadena1.isalpha())  # Devuelve True porque todos los caracteres son letras.
print(cadena2.isalpha())  # Devuelve False porque la cadena contiene caracteres no alfabéticos.

#!----------------------------------------------------------------------------------------------------------
# choice() es una función del módulo random en Python que se utiliza para elegir aleatoriamente un elemento de una secuencia, como una lista o una tupla. Aquí tienes un ejemplo de cómo usar 

import random

colores = ['rojo', 'verde', 'azul', 'amarillo']

color_aleatorio = random.choice(colores)
print("Color aleatorio elegido:", color_aleatorio)

# En este ejemplo, random.choice(colores) seleccionará aleatoriamente un color de la lista colores y lo devolverá. Luego, lo asignamos a la variable color_aleatorio y lo imprimimos. Dependiendo de la ejecución, puede imprimir "rojo", "verde", "azul" o "amarillo", de forma aleatoria.

#!----------------------------------------------------------------------------------------------------------


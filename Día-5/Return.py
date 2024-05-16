
#* Como ya vimos en el archivo Funciones.py la sintaxis de una función es:

def mi_funcion(nombre):
    print("Hola", nombre)

mi_funcion("Franco") # Hola Franco

#* Pero la realidad es que nosotros vamos a esperar que la función retorne algo, posiblemente para agregarlo a una variable y poder trabajar con ella. Por ejemplo, la siguiente función nos devolverá el resultado de la suma de dos números.

def sumar(num1, num2):
    return num1 + num2

resultado = sumar(10, 100)

print(resultado) # 110

#* Otra de las cosas que nos podemos encontrar es que, en el cuerpo de la función tengamos una variable interna y después la FN simplemente retorne esa variable interna:

def multiplicar(numero1, numero2):
    total = numero1 * numero2
    return total

print(multiplicar(6, 6)) # 36

	

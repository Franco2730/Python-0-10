
#* Digamos que tenemos dos funciones:

def sumar(num1, num2):
    print(num1 + num2)

sumar(50, 50)


#* y...


def sumar2(num1, num2):
    return num1 + num2

print(sumar2(50, 50))


#* Es clave comprender que la primer función solo PRINTEA el resultado en consola, pasado esa ejecución, dicho resultado no estará disponible para algo mas tarde en nuestro código...
#* Por el contrario, en el segundo código, lo que sucede es que la función RETORNA, devuelve un valor, y nosotros con eso podemos seguir trabajando, podemos manipular ese valor, lo podemos manejar y comparar. 


#! En cuanto a cuál conviene utilizar, depende del contexto y de lo que necesites hacer con el resultado de la suma. Si solo necesitas mostrar el resultado de la suma en la consola una vez, la primera función puede ser más simple y directa. Sin embargo, si necesitas utilizar el resultado de la suma en otras partes de tu programa, la segunda función, que devuelve el resultado en lugar de simplemente imprimirlo, sería más útil.


#* Veamos algo mas detallado: Imagina que estás desarrollando un programa que necesita realizar varias operaciones matemáticas con el resultado de la suma de dos números. Utilizando la primera función que imprime el resultado en la consola, no tendrías acceso al valor de esa suma para utilizarlo en otras partes del programa. Sin embargo, utilizando la segunda función que devuelve el resultado, podrías almacenar ese valor en una variable y luego utilizarlo según lo necesites.

#*  Imagina que estás desarrollando un programa que necesita realizar varias operaciones matemáticas con el resultado de la suma de dos números. Utilizando la primera función que imprime el resultado en la consola, no tendrías acceso al valor de esa suma para utilizarlo en otras partes del programa. Sin embargo, utilizando la segunda función que devuelve el resultado, podrías almacenar ese valor en una variable y luego utilizarlo según lo necesites.

#* Por ejemplo:

def sumar(num1, num2):
    return num1 + num2

# Almacenamos el resultado de la suma en una variable
resultado_suma = sumar(50, 50)

# Ahora podemos utilizar ese resultado en otras partes del programa
resultado_multiplicacion = resultado_suma * 2
print("El resultado de la multiplicación es:", resultado_multiplicacion)


#* En este caso, necesitamos utilizar el resultado de la suma (resultado_suma) en una multiplicación posterior. Utilizando la segunda función que devuelve el resultado, podemos almacenar ese valor en una variable y luego usarlo para realizar otras operaciones. Esto nos da más flexibilidad y control sobre cómo se utilizan los resultados de nuestras funciones en el programa.
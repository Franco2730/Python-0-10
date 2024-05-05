
#* Para crear nuestras propias funciones vamos a necesitar tener una sintaxis muy precisa y el principal elemento de esta sintaxis es la palabra clave " DEF ", esta palabra le dice a Python: Todo lo que voy a escribir a continuación es una función y para recordar esta palabra piénsala como que vamos a crear la DEFINICIÓN de una función luego de esto sigue el nombre que tú elijas para la función que vas a crear puede ser cualquier palabra o palabras que tú elijas y por convención siempre las escribimos con minúsculas Y en vez de espacios con guiones bajo luego de esto viene un par de paréntesis que por ahora nos vamos a dejar vacíos pero los podemos usar para pasar parámetros aunque eso lo veremos un poco más adelante y finalmente dos puntos

# def mi_funcion():

#* Todo esto le dice python que lo que sigue a continuación mientras que esté tabulado hacia la derecha de la palabra DEF está dentro de la función y forma parte de su código luego lo que sigue no es un código obligatorio pero sí forma parte de los buenos hábitos y es escribir una explicación sobre lo que hace la función pero esto encerrándolo entre tres comillas simples antes y después del texto de hecho cada vez que utilices las tres comillas simples en python puedes escribir texto descriptivo que no va a ser ejecutado O sea que lo puedes escribir libremente y sirve para que a ver cualquier persona incluso tú que vea el código puede enterarse con facilidad y el lenguaje humano qué es lo que hace esta función y luego si escribes el código que tú quieres que se ejecute cada vez que llamemos a esta función entonces así se escribe una función.

# def mi_funcion_saluda():
#     '''Esta función se encarga de imprimir un saludo'''
#     print("Hola querido/a: ")

#* ¿ Pero cómo se ejecuta ? bueno cada vez que escribamos en cualquier otra parte de nuestro código el nombre de la función (mi_funcion_saluda) y sus paréntesis, Python va a ejecutar lo que sea que haya dentro de nuestra función.
#* Ahora sí les prestemos atención a los paréntesis como te dije puedes usar los paréntesis para ingresar un parámetro o un argumento dentro de tu función yo por ejemplo aquí puse el parámetro nombre este es una especie de variable interna le podría haber puesto cualquier palabra, yo elegi nombre. Aunque al momento de escribir mi función yo no sé cuál va a ser el valor de este parámetro puede usarlo para que sea cual sea luego Su contenido yo lo pueda invocar desde cualquier lugar dentro de la función por ejemplo para concatenarlo con mi string de "Hola querido/a ..." si luego al momento de invocar la función pongo dentro del paréntesis un valor cualquiera por ejemplo Franco, bueno ahora le estoy dando un contenido a la variable nombre que lo va a poder usar en la concatenación y ahora el resultado de mi función va a ser la impresión de la expresión Hola querido/a Franco. 

# def mi_funcion_saluda(nombre):
#     print("Hola querido/a: ")



#* Por ahora lo estoy manteniendo súper simple para asegurarme de que todos podamos entenderlo con facilidad pero vamos a ver que este abordaje brinda aplicaciones infinitas y muy pero muy útiles veamos este mismo ejemplo pero la pantalla negra para que lo puedas aplicar tú mismo también :) 

#* Supongamos que desarrollamos una función que retorna una función, al momento de invocarla, no se imprimirá nada en pantalla, pero devolverá un valor, y ese valor lo podemos agregar en una variable. Eso nos brinda un mundo de posibilidades. Por ejemplo:

def sumar(num1, num2):
    return num1 + num2


devolverSuma = sumar(10, 100)

print(devolverSuma) # 110
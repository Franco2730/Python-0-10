# def cero_consecutivo(*args):
#     # Utilizamos un bucle for para iterar sobre los índices de los elementos en args. La función len(args) devuelve la cantidad total de argumentos pasados a la función, y range(len(args) - 1) genera una secuencia de números desde 0 hasta len(args) - 2, lo que nos permite iterar sobre los índices de los elementos hasta el penúltimo elemento. 
#     for i in range(len(args) - 1):
#         # En cada iteración del bucle, verificamos si el elemento actual (args[i]) y el siguiente elemento (args[i + 1]) son ambos iguales a cero. Si esto es verdadero, significa que hemos encontrado 
#         if args[i] == 0 and args[i + 1] == 0:
#             return True
#     return False

# print(cero_consecutivo(0, 0, 1, 2, 3, 4, 0, 5, 0, 6))


#* He notado algunos inconvenientes con mis alumnos a la hora de resolver este mensaje. Permítanme explicarles el paso a paso:"

# Cuando utilizamos `range(len(args) - 1)`, estamos creando una secuencia de números desde 0 hasta `len(args) - 2`. Permíteme explicar por qué restamos 1.

# En Python, los índices comienzan desde 0. Entonces, si tenemos una lista de longitud `n`, los índices válidos para esa lista van desde 0 hasta `n - 1`. Por lo tanto, si queremos iterar sobre todos los elementos de una lista `args` usando sus índices, necesitamos asegurarnos de que el índice no supere el último elemento.

# Dado que queremos verificar si hay dos elementos consecutivos, no necesitamos comparar el último elemento con el siguiente, ya que no habrá ningún siguiente para el último elemento. Por lo tanto, no necesitamos iterar hasta el último índice de `args`, sino hasta el penúltimo, para evitar un índice fuera de rango al acceder al siguiente elemento (`args[i + 1]`).

# Por lo tanto, utilizamos `range(len(args) - 1)` para generar una secuencia que itere desde 0 hasta `len(args) - 2`, lo que nos permite iterar sobre los índices de los elementos hasta el penúltimo elemento de `args`.

# Espero que esta explicación haya sido de ayuda mis queridos y queridas chiquis !!! 



#* Vamos a plantear otra alternativa a nuestra consigna:

def ceros_vecinos(*args):

    contador = 0

    for num in args:

        if contador + 1 == len(args):
            return False
        elif args[contador] == 0 and args[contador + 1] == 0:
            return True
        else:
            contador = contador + 1

    return False

# print(ceros_vecinos(1, 2, 3, 0, 5, 6, 9, 10, 0)) # => False

print(ceros_vecinos(1, 0, 0, 5, 6, 9, 10, 0)) # => True
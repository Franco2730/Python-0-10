def letras_unicas_ordenadas(str):
    # Utilizamos la función set() para convertir el str en un conjunto. Un conjunto en Python solo contiene elementos únicos, eliminando cualquier duplicado. Esto significa que obtenemos todas las letras únicas de el str.
    # Usamos la función sorted() para ordenar alfabéticamente las letras únicas obtenidas del paso anterior. Esto nos asegura que las letras estén en orden alfabético.
    letras_unicas = sorted(set(str))
    # Utilizamos "".join() para concatenar las letras únicas ordenadas en una sola cadena. Esto nos da la representación final de las letras únicas en orden alfabético.
    return "".join(letras_unicas)

# Ejemplo de uso
str = "entretenido"
resultado = letras_unicas_ordenadas(str)
print("Letras únicas en orden alfabético:", resultado)




#* Vamos con otra forma de llevar esto a cabo:



def letras_unicas(word):
    # almacenamos todo dentro de un set para que sean elementos unicos:
    mi_set = set()
    # Hacemos un bucle y decimos que vaya agregando cada letra de la palabra a la variable mi_set
    for letra in word:
        mi_set.add(letra)

    # Ahora debemos ordenarlos ya que los sets no son conjuntos ordenados y antes de ordenarlos y mostrarlos, debemos convertirlos a una lista, necesitamos hacerle un casting a lista
    mi_list = list(mi_set)
    # Una vez que ya hicimos el casting, con el metodo SORT propio de las listas, vamos a ordenar los elementos
    mi_list.sort()

    return mi_list

# print(letras_unicas("entretenido"))
# ['d', 'e', 'i', 'n', 'o', 'r', 't']

print(letras_unicas("cascarrabia"))
# ['a', 'b', 'c', 'i', 'r', 's']

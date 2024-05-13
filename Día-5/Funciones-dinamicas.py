# Vamos a hacer algo que ya sabemos: Vamos a crear una fn que se encargara de chequear si un número (que le pasamos por parametro) esta en un rango de 100 y 1000 (el mil no entra, asique del 100 al 999)

def chequear_3_cifras(numero):
    return numero in range(100,1000)

# A continuación vamos a crear una variable llamada resultado que será igual a la función anteriormente realizada con su respectivo parametro.

# resultado = chequear_3_cifras(103) # True
# resultado2 = chequear_3_cifras(190) # True
# resultado3 = chequear_3_cifras(13) # False
# resultado4 = chequear_3_cifras(1001) # False

# print(resultado4)

#* Ahora supongamos que necesito, en vez de pasarle un solo número, necesito pasarle muchos números y que ahi nos diga si alguno de esos neros tiene 3 cifras

# def chequear_lista(lista):
#     for i in lista:
#         if i in range(100, 1000):
#             return True
#         else:
#             pass
#     return False

# resultado = chequear_lista([50, 91, 1, 1005, 10000]) # None => ninguno
# resultado = chequear_lista([50, 91, 1, 104]) # True
# print(resultado)

#* A continuación haremos lo mismo que en el ejercicio anterior, pero ahora, agregaremos los elementos que cumplan la condición en una variable aparte. 

def corroborar_lista(lista): # [10, 100, 200, 300, 800, 1000, 2000]
    lista_3_cifras = []

    for i in lista: # Por cada elemento en la lista...
        if i in range(100, 1000): # decimos SI ese elemento está en un rango de 100 a 999...
            lista_3_cifras.append(i) # Si se cumple esa condición, sumaremos ese elemento a lista_3_cifras
        else:
            pass

    return lista_3_cifras

resultado2 = corroborar_lista([10, 100, 200, 300, 800, 1000, 2000])

print(resultado2) # [100, 200, 300, 800]
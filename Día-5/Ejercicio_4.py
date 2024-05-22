
#* Esta función nos solicita MOSTRAR en pantalla los números primos y por otro lado DEVOLVER el total de números primos

def contar_primos(numero):
    # Vamos a crear una lista que acumule los n primos, de paso inicia con el número 2 ya que el 0 y el 1 no lo son
    primos = [2]

    # La sig. variable va a tener el numero que va a ir chequeando desde el 0 hasta el valor que necesitemos llegar (el parametro que le pasemos), vamos a inicializar la misma en 3 ya que 0 y 1 no son primos y dos si.
    iteracion = 3

    # La siguiente condicion dice que si el numero ingresado es menor a 0 directamente retornamos 0
    if numero < 2:
        return 0

    # Vamos a hacer un bucle que diga que MIENTRAS que el valor de la variable iteracion sea menor o igual al numero pasado por parametro:
    while iteracion <= numero:

        for n in range(3, iteracion, 2):

            if iteracion % n == 0:
                iteracion = iteracion + 2
                break
        else:
            primos.append(iteracion)
            iteracion = iteracion + 2
    print(primos)
    return len(primos)


print(contar_primos(50))




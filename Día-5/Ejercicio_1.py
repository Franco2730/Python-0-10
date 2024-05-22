def devolver_distintos(num1, num2, num3): 

    suma = num1 + num2 + num3

    if suma > 15:
        return max(num1, num2, num3)
    elif suma < 10:
        return min(num1, num2, num3)
    else:
        lista_numeros = [num1, num2, num3]
        lista_numeros.sort()
        return lista_numeros[1]

    
print(devolver_distintos(1, 3, 10))



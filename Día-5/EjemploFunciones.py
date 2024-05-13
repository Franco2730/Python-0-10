
#* Vamos a ver SIN LAS FUNCIONES como hacer algo para desempaquetar Tuples:

precios_cafe = [('Capuchino', 1200),('Te', 4500), ('Expresso', 1350), ('Moka', 1500)]

# for cafe, precio in precios_cafe: # Así desempaqueto un tupple, Colocando dos elementos in...
    # print(precio / 2)

# Capuchino
# Expresso
# Moka

#* Como hacemos para sacar el costo de ganancia de cada café? Sabemos que el costo de ganancia es del 45% del producto, entonces debemos multiplicar su valor por 0.45

# for cafe, precio in precios_cafe: 
#     print(precio * 0.45)

# 540.0
# 607.5
# 675.0

#* Ahora, como podemos averiguar cual es el café mas caro ?? Necesitamos una función que retenga el primero y vaya comparando.

def cafe_mas_caro(lista_precios):
    precio_mayor = 0
    cafe_caro = ''

    for cafe, precio in lista_precios:
        if precio > precio_mayor:
             precio_mayor = precio
             cafe_caro = cafe
        else:
            pass

    return(cafe_caro, precio_mayor)

print(cafe_mas_caro(precios_cafe)) # ('Te', 4500)


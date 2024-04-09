 #* Si tenemos en cuenta lo que hemos hecho hasta el momento, cuando hemos necesitado una lista de elementos, hemos creado una variable con una lista y a partir de ello, lo recorríamos, como en el siguiente ejemplo:

# lista = [1, 2, 3, 4, 5,]

# for numero in lista:
#     print(numero)

# 1 
# 2
# 3
# 4
# 5

#* Pero esto, claramente, no es lo mas útil para realizar. Deberíamos:

for numero in range(1, 11, 2):
    print(numero)

# 1
# 2
# 3
# 4
# 5

#* Range también acepta un tercer parámetro, si bien no es obligatorio, el tercer parámetro es la cantidad de números que va a omitir al efectuar el rango, es decir, si en el ejemplo anterior colocamos: (1, 11) nos imprimirá desde el 1 hasta el 10. Pero si hubiésemos colocado (1, 11, 2) el resultado hubiese sido: 

# 1
# 3
# 5
# 7
# 9

#* Si hubiésemos querido que saliera: 2, 4, 6, 8, 10 los parámetros hubiesen tenido que ser: (0, 11, 2)

#todo esto para que nos puede servir en la vida real? Muy fácil. Imaginemos que debemos crear una lista de 100 números y almacenarla en una variable. Con range es SUPER fácil y sería aplicando un casting a un range:

lista = list(range(0, 101))

print(lista)

# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]


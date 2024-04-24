
#* Supongamos que tenemos una variable llamada palabra con un valor de 'python'. Si yo quisiera hacer una lista por cada elemento de nuestra variable podríamos tener en mente usar el método append que sirve para agregar, un bucle for que, por cada recorrido del mismo, se agregue cada elemento de dicho string a una lista vacía. Lo podríamos hacer de la siguiente forma

palabra = 'python'
lista = []

for letra in palabra:
    lista.append(letra)

# print(lista)

# ['p', 'y', 't', 'h', 'o', 'n']

#* Pero mira cuantas líneas de código nos ha tomado llevar a cabo algo simple, algo que con, comprensión de listas hubiésemos acortado, por ejemplo: vamos a declarar una variable llamada otraPalabra que será igual a un str. Luego...

otraPalabra = 'programacion'

#*... le decimos a python: Quiero que la variable lista2 sea igual a una lista (por eso los corchetes) donde cada elemento sea una letra de cada letra que haya en la variable otraPalabra
lista2 = [letra for letra in otraPalabra] # recordar que letra es una variable interna

# print(lista2)

# ['p', 'r', 'o', 'g', 'r', 'a', 'm', 'a', 'c', 'i', 'o', 'n']

#* También es bueno recordar que no necesitariamos tener una variable, tan solo con la variable con la lista ya estaríamos listos para alimentar una nueva lista. Por eje:

lista3 = [i for i in 'Estudiando programacion']

# print(lista3)

# ['E', 's', 't', 'u', 'd', 'i', 'a', 'n', 'd', 'o', ' ', 'p', 'r', 'o', 'g', 'r', 'a', 'm', 'a', 'c', 'i', 'o', 'n']

#* Como podríamos crear una lista con números pares del 1 al 20 ?

# lista4 = [n for n in range(2, 21, 2)]
# print(lista4)

# [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

#* Cabe aclarar que podríamos modificar cada uno de esos números antes de agregarlos a la lista diciendo, por ejemplo:

lista4 = [n / 2 for n in range(0, 10)] # 0 / 2 = 0.0 - 1 / 2 = 0.0 - 2 / 2 = 1.0 - 3 / 2 = 1.5 - 4 / 2 = 2.0 - 5 / 2 = 2.5 - 6 / 2 = 3.0 - 7 / 2 = 3.5 - 8 / 2 = 4.0 - 9 / 2 = 4.5 
# print(lista4)

# [0.0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5] 

#* O....

lista5 = [n * 2 for n in range(0, 10)] # 0 * 2 = 0 / 1 * 2 = 2 / 2 * 2 = 4 / 3 * 2 = 6 / 4 * 2 = 8 / 5 * 2 = 10 / 6 * 2 = 12 / 7 * 2 = 14 / 8 * 2 = 16 / 9 * 2 = 18 
# print(lista5)

# [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

#* Podríamos hacer algo de la vida cotidiana. Como todos sabemos, en la república Argentina, tener divisa UsD no siempre es tarea sencilla, con lo cual, debemos tomarnos la tarea de primero comprar dicha moneda, para eso debemos saber el costo:

dolar = [1, 10, 100, 1000, 10000]
pesoArgetino = [usd * 1000 for usd in dolar] # 1 * 1000 = 1000 / 10 * 1000 = 10000 / 100 * 1000 = 100000 / 10000 = 10000000

print(pesoArgetino) 

# [1000, 10000, 100000, 1000000, 10000000]


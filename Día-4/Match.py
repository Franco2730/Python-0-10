 #* A partir de la versión de Python 3.10 se acuatlizó algo que le estaba faltando. Todos los lenguajes cuentan con el condicional IF. Y ademas algunos cuentan con otra variedad de este condicional que, como ya sabemos, nos permite elegir una opcion dentro de una variedad de opciones. En otros lenguales esta erramienta se suele llamar Switch o Switch case y en Python a partir de la V 3.10 se llama Match (coincidencia) esto no solamente iguala la capacidad de otros lenguajes, si no, que lo supera. Bien amigo Python !!! 

#* Como ya dijimos, no solamente vamos a poder elegir una opcion dentro de varias, si no, que ademas vamos a poder implementar que nuestro codigo haga algo distinto de acuerdo a algun patron de información que estemos recibiendo. En el siguiente ejemplo veremos el tipico condicional que ya sabemos usar:

# serie = 'N-02'

# if serie == 'N-01':
#     print('Samsung')
# elif serie == 'N-02':
#     print('Iphone')
# elif serie == 'N-03':
#     print('Motorola')
# elif serie == 'N-03':
#     print('Nokia')
# else:
#     print('No se que celular es')

#* Veamos como quedaria el ejemplo anterior pero con la version match:
#* Primero debemos colocar match serie: Es decir, en lectura sería algo como: Necesitamos tener una coincidencia con la variable serie (la información que utiliza python para comparar) 
#* Luego, en vez de cada if o elif, colocamos case, que vendria siendo como en caso de que sea tal cosa...

# match serie:
#     case 'N-01':
#         print('Samsung')
#     case 'N-02':
#         print('Iphone')
#     case 'N-03':
#         print('Motorola')
#     case 'N-03':
#         print('Nokia')
#     case _:
#         print('No se que celular es')

#* Pero ese no es todo el poder de nuestro querido match. Veamos en el siguiente ejemplo algo para poder estrujar su verdadero poder:

#* Vamos a tener dos diccionarios. El primero se llamara cliente donde tendra datos de mi persona y el segundo diccionario tendrá el nombre de pelicula y tendra un diccionario en su interior que será la ficha tecnica de si mismo. 

cliente = {'Nombre': 'Franco',
           'Edad': 30,
           'Ocupacion': 'Instructor',
           'Origen': 'Argentino'}

pelicula = {'Titulo': 'Titanic',
            'Ficha tecnica': {'Protagonista': 'Leonardo DiCaprio y Kate Winslet',
                              'Director': 'James Cameron',
                              'Estreno': 1997}}

#* Ahora vamos a crear una variable que contendrá una lista con ambos diccionarios y un string que no existe en ningun lado
elementos = [cliente, pelicula, 'Hola']

for elemento in elementos:
    match elemento:
        case {'Nombre': Nombre,
             'Edad': Edad,
             'Ocupacion': Ocupacion,
             'Origen': Origen}:
            print("Coincide con la estructura de cliente")
            print(f'Y dicho cliente es: {cliente}')
        case {'Titulo': Titulo,
              'Ficha tecnica': {'Protagonista': Protagonista,
                                'Director': Director,
                                'Estreno': Estreno}}:
            print("Coincide con la estructura de una pelicula")
            print(f'Y esa pelicula es: {pelicula}')
        case _:
            print("No se que demonios significa 'Hola'")

# Coincide con la estructura de cliente
# Y dicho cliente es: {'Nombre': 'Franco', 'Edad': 30, 'Ocupacion': 'Instructor', 'Origen': 'Argentino'}

# Coincide con la estructura de una pelicula
# Y esa pelicula es: {'Titulo': 'Titanic', 'Ficha tecnica': {'Protagonista': 'Leonardo DiCaprio y Kate Winslet', 'Director': 'James Cameron', 'Estreno': 1997}}

# No se que demonios significa 'Hola'
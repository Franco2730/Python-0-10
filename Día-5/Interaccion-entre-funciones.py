from random import shuffle
#* En el siguiente código veremos la interacción de funciones entre si creando el famoso juego de los palitos. En el mismo, los participantes sacan un palito a elección y aquel participante con el palito más cortito, deberá... lavar los platos, por ejemplo:

#* Lista inicial con todos los palitos:
palitos = ['-', '--', '---', '----', '-----']

#* Mezclar los palitos después de haber importado esto desde random
def mezclar(lista):
    shuffle(lista) 
    return lista

#* Fn que le pida al usuario que elija uno de los palitos:
def probar_suerte():
    intento = ''

    while intento not in ['1', '2', '3', '4', '5']:
        intento = input("Elige un numero del 1 al 5: ")

    return int(intento)

#* Fn que corrobore la elección del participante: 
def chequear_intento(lista, intento):
    if lista[intento - 1] == '-':
        print("A lavar los platos")
    else:
        print("Esta vez te has salvado")
    print(f"Te ha tocado {lista[intento - 1]}")

palitos_mezclados = mezclar(palitos)
seleccion = probar_suerte()
chequear_intento(palitos_mezclados, seleccion)



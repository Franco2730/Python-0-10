
#* Esta es una forma un poco mas "visual" de darle solución a nuestro proyecto del día.

from random import *
 
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    RANDOM = '\33[101m'
    RANDOMGREEN = '\33[102m'
    PALEGREEN = '\33[4m'
    RANDOMPALEGREEN = '\33[7m'
    ORANGY = '\33[93m'
    UNDERLINE = '\033[4m'
 
    CEND = '\33[0m'
    CBOLD = '\33[1m'
    CITALIC = '\33[3m'
    CURL = '\33[4m'
    CBLINK = '\33[5m'
    CBLINK2 = '\33[6m'
    CSELECTED = '\33[7m'
 
    CBLACK = '\33[30m'
    CRED = '\33[31m'
    CGREEN = '\33[32m'
    CYELLOW = '\33[33m'
    CBLUE = '\33[34m'
    CVIOLET = '\33[35m'
    CBEIGE = '\33[36m'
    CWHITE = '\33[37m'
 
    CBLACKBG = '\33[40m'
    CREDBG = '\33[41m'
    CGREENBG = '\33[42m'
    CYELLOWBG = '\33[43m'
    CBLUEBG = '\33[44m'
    CVIOLETBG = '\33[45m'
    CBEIGEBG = '\33[46m'
    CWHITEBG = '\33[47m'
 
    CGREY = '\33[90m'
    CRED2 = '\33[91m'
    CGREEN2 = '\33[92m'
    CYELLOW2 = '\33[93m'
    CBLUE2 = '\33[94m'
    CVIOLET2 = '\33[95m'
    CBEIGE2 = '\33[96m'
    CWHITE2 = '\33[97m'
 
    CGREYBG = '\33[100m'
    CREDBG2 = '\33[101m'
    CGREENBG2 = '\33[102m'
    CYELLOWBG2 = '\33[103m'
    CBLUEBG2 = '\33[104m'
    CVIOLETBG2 = '\33[105m'
    CBEIGEBG2 = '\33[106m'
    CWHITEBG2 = '\33[107m'
 
seis_vidas = f"{bcolors.CBEIGE} VIDAS\n_______\n   |{bcolors.ENDC}"
cinco_vidas = seis_vidas + f"{bcolors.ORANGY}{bcolors.BOLD}\n  ( ){bcolors.ENDC}"
cuatro_vidas = cinco_vidas + f"{bcolors.ORANGY}\n   |{bcolors.ENDC}"
tres_vidas = cinco_vidas + f"{bcolors.ORANGY}\n  /|{bcolors.ENDC}"
dos_vidas = tres_vidas + f"{bcolors.ORANGY}\\{bcolors.ENDC}"
una_vida = dos_vidas + f"{bcolors.ORANGY}\n  /{bcolors.ENDC}"
cero_vidas = una_vida + f"{bcolors.ORANGY} \\{bcolors.ENDC}"
array_vidas = [cero_vidas, una_vida, dos_vidas, tres_vidas, cuatro_vidas, cinco_vidas, seis_vidas]
 
def palabra_random():
    palabras = ["cocodrilo", "señoria", "bungaloo", "amanecer",
                "ronquido", "silbar", "defensa", "tomate",
                "siete", "helicoptero", "edificio", "periquito",
                "escalera", "escondite", "neumatico", "congelado"]
    return choice(palabras)
 
def diccionar_palabra(palabra):
    mi_dic = {}
    contador = 0
    for letra in list(palabra):
        mi_dic[contador] = letra
        contador += 1
    return mi_dic
 
def print_vidas(vidas):
    print(array_vidas[vidas] + "\n")
 
def pintar_lineas(palabra):
    return list("_"*len(palabra))
 
def pintar_palabra(letra_usuario, letras_palabra, lineas):
    resultado = lineas
    comprobador = False
    for indice,letra in letras_palabra.items():
        if (letra == letra_usuario):
            resultado[indice] = letra
            comprobador = True
    return resultado, comprobador
 
def separador():
    print(f"{bcolors.CVIOLET}======================================================================================================{bcolors.ENDC}")
 
 
def jugar():
    vidas = 6
    palabra = palabra_random()
    letras_palabra = diccionar_palabra(palabra)
    lineas = pintar_lineas(letras_palabra)
    while vidas > 0:
        print_vidas(vidas)
        print(f"{bcolors.CITALIC}Palabra: {bcolors.BOLD}{bcolors.CYELLOW2}{''.join(lineas)}{bcolors.ENDC}")
        letra = input("Escribe tu letra: ")
        print("\n")
        separador()
        print("\n")
        resultado, comprobador = pintar_palabra(letra, letras_palabra, lineas)
        if comprobador == False:
            vidas -= 1
            if vidas <= 0:
                print_vidas(vidas)
                print(f"{bcolors.CRED}¡LÁSTIMA! HAS PERDIDO")
                print(f"La palabra era {palabra}")
                break
        elif comprobador == True and '_' not in resultado:
            print(f"{bcolors.OKGREEN}¡FELICIDADES! HAS GANADO")
            print(f"La palabra era {palabra}")
            break
 
 
jugar()
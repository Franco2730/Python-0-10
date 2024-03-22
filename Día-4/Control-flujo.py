# Este será un paso significativo en tu carrera como programador de Python ya que acá veras el germen de la inteligencia artificial ya que aprenderemos a que el programa tome sus propias decisiones con sentencias tales como: IF – ELIF y ELSE.
# IF significa Si (Si pasa tal cosa...)
# Elif sifnicia Si no (si no pasa eso entonces...)
# else significa entonces(Si no se ha cumplido ninguna condición, entonces haz tal cosa...)
# Esto significa:

if 5 == 2:
    print('5 es igual a 2') # Esta parte del código no se imprimirá, porque esa condición es claramente falsa.
else:
    print('5 es mayor a 2') # Se imprimirá este mensaje



mascota = 'perro'

if mascota == 'gato':
    print('Tu tienes un lindo gatito')
elif mascota == 'Hamster':
    print('Tu tienes un lindo ratoncito')
elif mascota == 'pez':
    print("Debes tener un hermoso acuario")
elif mascota == 'dinosaurio':
    print("WOW, Debes gastar mucho dinero en vacas para su almuerzo")
else:
    print("No se que mascota tienes")



SeCumpleCondicion1 = False
SeCumpleCondicion2 = False
SeCumpleCondicion3 = False

if SeCumpleCondicion1:
    print("Se ejecutará este primer codigo")
elif SeCumpleCondicion2:
    print("Se ejecutará este segundo codigo")
elif SeCumpleCondicion3:
    print("Se ejecutará este tercer codigo")
else:
    print("Si ninguna condición se ha cumplido, mis alumnos son los mejores!")

#* Como no se cumple ninguna condición (todas las condiciones tienen un valor de False) se ejecutará: Si ninguna condición se ha cumplido, mis alumnos son los mejores!
    

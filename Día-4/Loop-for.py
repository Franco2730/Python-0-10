# Como ya habíamos mencionado, los loops for son aquellos bucles que se repiten una cantidad DEFINIDA de iteraciones. Supongamos que tenemos el siguiente escenario:

nombres = ['Juan', 'Agustina', 'Marcos', 'Carlos', 'Belen', 'Fran']

# Ahora pensemos que queremos colocar: Hola, como estas? por cada nombre que haya en la lista llamada nombres. En castellano diriamos algo como:

#* por cada ELEMENTO en NOMBRES:
#*     imprimir("Hola")

#! La sentencia anterior es en español, veamos como se vería en código:
# Por cada, en ingles, se dice FOR 
# en, se dice IN
# elemento es una variable interna que le asignamos a los elementos de la lista, pero podriamos haber puesto element, i, ele, perro. Tenemos que saber que eso representa cada uno de nuestros elementos. 

#* FOR elemento IN nombres: 
#*      print("Hola")

#* FOR ele IN nombres: 
#*      print("Hola")

#* FOR i IN nombres: 
#*      print("Hola")



#* Algo SUPER interesante de saber es, como vemos en nuestra lista llamada nombres, tenemos 6 elementos (los 6 nombres), cuando hacemos el bucle for que vimos anteriormente, la variable interna que llamamos elemento, ele o i va a contener (como cajita que es) en su interior, al elemento que este iterando en cada vuelta, es decir, cuando el loop for apenas comienza la variable interna elemento tendrá el valor juan y se imprimirá en consola Hola.
#* Vuelve el loop a comenzar pero en su segunda vuelta, la variable elemento tendrá el valor de Agustin, acto segudo solo se imprimirá Hola en consola, ya que esa es la orden que le dimos, asi con el tercer elemento que es Marcos hasta llegar a Fran e imprimir el sexto Hola en consola:

# Hola 
# Hola 
# Hola 
# Hola 
# Hola 
# Hola 

#* Pero como podemos estar analizando, si elemento contiene un valor (un nombre distinto en cada vuelta) no podriamos realizar un saludo un poco mas personalizado? Veamos !!!

# for elemento in nombres:
#     print('Hola ', elemento, '¿Como estás el día de hoy?')

# Hola  Juan ¿Como estás el día de hoy?
# Hola  Agustina ¿Como estás el día de hoy?
# Hola  Marcos ¿Como estás el día de hoy?
# Hola  Carlos ¿Como estás el día de hoy?
# Hola  Belen ¿Como estás el día de hoy?
# Hola  Fran ¿Como estás el día de hoy?
    
autos = ['chevy', 'falcon', 'dodge', 'peugeot', 'fiat', 'ferrari']

# for autito in autos:
#     print(autito)

# chevy
# falcon
# dodge
# peugeot
# fiat
# ferrari
    
# for autito in autos:
#     print('Me gustaría tener un:',autito)

# Me gustaría tener un: chevy      
# Me gustaría tener un: falcon     
# Me gustaría tener un: dodge      
# Me gustaría tener un: peugeot    
# Me gustaría tener un: fiat       
# Me gustaría tener un: ferrari
    
#* Podemos hacer un loop for con dos variables dentro y que ambas cambien en cada iteración:
    
abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i','j','k', 'l', 'm', 'n', 'ñ','o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

for i in abc:
    numeroDeLetra = abc.index(i) + 1 # aclaramos que sea más uno para no arrancar en cero
    print(f'La letra {numeroDeLetra}: {i}')

# La letra 1: a
# La letra 2: b
# La letra 3: c
# La letra 4: d
# La letra 5: e
# La letra 6: f
# La letra 7: g
# La letra 8: h
# La letra 9: i
# La letra 10: j
# La letra 11: k
# La letra 12: l
# La letra 13: m
# La letra 14: n
# La letra 15: ñ
# La letra 16: o
# La letra 17: p
# La letra 18: q
# La letra 19: r
# La letra 20: s
# La letra 21: t
# La letra 22: u
# La letra 23: v
# La letra 24: w
# La letra 25: x
# La letra 26: y
# La letra 27: z
# En la clase pasada aprendimos como mostrar en pantalla palabras. En Python existen muchos tipos de datos, ahora vamos a ver que es un String. 
# Un string es una cadena de caracteres. Es decir, la palabra HOLA es un conjunto de los caracteres H, O, L, A. Al colocar algo dentro de comillas serán tratados como string, si colocamos números, estos serán tratados como string, no se podrán ser tratados como números y no se podrán efectuar operaciones matemáticas.

# El resultado de la siguiente "operacion" daria como resultado 100 + 50
print("100 + 50")

print(100 + 50) # Acá si son tratados como numeros. La consola mostrará 150

print("Hola" + "chicos" + "soy Franco") # Holachicossoy Franco

print("Hola" + " " "chicos" + " " + "soy Franco") # Hola chicos soy Franco.

# Tenemos una pequeña pero muy útil herramienta que es la barra invertida: \ esta sirve para decirle a nuestro IDE que el siguiente carácter no tiene que ser tratado de forma especial si no, textual. 
# Al principio teníamos un problema que no podíamos poner todas comillas dobles en un print si queríamos mostrar algo en consola que tuviera de por si comillas. Con nuestra barra invertida podemos decirle al ide:  ¡¡Oye !! al siguiente carácter no lo trates como comillas, imprime su forma, pero no su función!

print("Mi nombre es \"Franco\"") # Mi nombre es "Franco"

# ¿Y si te digo que podemos hacer un salto de línea? ¿Como si fuera un punto aparte? Esto lo podemos hacer muy fácil con nuestra barra invertida seguida de una letra n. (\n) 

print("Esta es una línea \nY esta es otra linea.")
# Esta es una línea 
# Y esta es otra linea.

# Ahora veamos que significa: \t. Esto sirve para tabular, 4 espacios, como una sangría. 

print("Comienza un cuento \tY esta oracion tiene sangría")
# Comienza un cuento 	Y esta oracion tiene sangría

# Para que sea una sangría tenemos que agregar un salto de linea:
print("Comienza un cuento \n\tY esta oracion tiene sangría")
# Comienza un cuento 
# 	Y esta oracion tiene sangría

# ¡Un momento! Y si queremos colocar solamente una barra invertida ¿? ¡La computadora explotará por los aires! Para nada ¡! De hecho, es bastante lógico, si colocamos dos barras invertidas, la primera de ellas le dice al ide: ¡Oye! Recuerda que el siguiente carácter lo tienes que tratar por su forma mas no su función. 

print("El siguiente signo: \\ es una barra invertida y muy bonita") # El siguiente signo: \ es una barra invertida y muy bonita
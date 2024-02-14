# Recuerdan en el ejercicio de Casting cuando tuvimos el ejemplo de la edad ?

edad = input("Dime tu edad: ")
print(type(edad)) # <class 'str'>

edad = int(edad)
print(type(edad)) # <class 'int'>

nueva_edad = 1 + edad
print(nueva_edad) # 31

# Si bien tuvimos un éxitoso resultado ya que, para sumar ambos valores, tuvimos que hacerle casting a edad. 
# ¿ Que sucede si queremos imprimir en consola un mensae como: "Tu tienes 30 años, dentro de poco tendrás 31, felicidades!!" ? ¿ Tendremos que volverle a aplicar casting nuevamente para poder concatenar el texto con la variable de tipo int ? Claro que se podría pero no seria muy beneficioso para el programa ya que no es buena practica ir y venir transformando datos. Para esto, vamos a aprender lo siguiente: "Formatear cadenas de texto" Para esto hay dos formas de hacerlo:

# color_auto = "rojo"
# matricula = 15222

# print("Mi auto es de color: {} con la matricula: {}".format(color_auto, matricula)) # Mi auto es de color: rojo con la matricula: 15222

# El metodo .format fue muy utilizado ya que su sintaxis permite realizar una concatenación de cualquier tipo de dato sin importar su tipo. En el mensaje debemos dejar unas llaves vacías por cada variable a remplazar y al finalizar las comillas agregamos el metodo con un punto y entre parentesis las variables en el orden que estan las llaves vacías. 
# Aunque fue muy utilizado, se dejo de usar al poco tiempo ya que a ojos de los programadores, tenemos que mirar desde el principio al fin y nuevamente desde el fin al principio. Es un poco agotador en largas líneas de código y se presta para la confución. }

# Para resolver el inconveniente planteado con la sintaxis anterior, en la versión 3.6 de Python salió algo llamado: Cadenas literales. Y esto hizo un giro de 180° a todos esos inconvenientes. 

# Para implementar las cadenas literales simplemente antes del primer parentesis colocamos una letra f avisandole que será una cadena literal y luego es similar a la sintaxis anterior solamente que el nombre de las variables, irán entre las llaves vacías. Se acabo el format y el desorden. 

color_auto = "rojo"
matricula = 15222

print(f"Mi auto es de color: {color_auto} con la matricula: {matricula}") # Mi auto es de color: rojo con la matricula: 15222

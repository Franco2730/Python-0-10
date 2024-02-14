# Muchas veces nos vamos a encontrar con alguna situación en la que debamos transformar el tipo de dato de una variable a otro. Por ejemplo:
  
#edad = input("Dime tu edad por favor: ") # Si coloco 30

# print(type(edad)) #<class 'str'>


# T0do ingreso de información de usuario (input) es de tipo string, no importa si nosotros colocamos un número entero. 
#  Con lo cual, si queremos hacer una operación matemática con esa edad que el usuario ingreso no sería posible sin antes modificar el tipo de datos. Esta acción se llama CASTING y existen dos tipos de casting: IMPLÍCITAS O EXPLÍCITAS. 
#  La conversión implícita es realizada automáticamente por Python. 
#  La conversión explícita es cuando nosotros de forma explicita y a través de código le decimos a Python que deseamos convertir el tipo de dato a otro. Por ejemplo: 

# Conversión IMPLÍCITAS:
num1 = 20
num2 = 30.5

print(type(num1)) #<class 'int'>
print(type(num2)) #<class 'float'>

#A continuación vamos a ver como Python transforma sin preguntarnos el tipo de dato de la variable num1 ya que, para sumarla con la variable num2 el resultado es float. "No importa el tipo de datos de los valores entrantes, si no, el resultado" la variable num1 ha dejado de ser INT para ser FLOAT.
num1 = num1 + num2
print(type(num1)) #<class 'float'>



# Conversión EXPLÍCITAS:

num1 = 5.8
print(num1) # 5.8
print(type(num1)) # <class 'float'>

# La lectura de la siguiente conversión explícita es: Quiero que num2 sea igual a un integer conformado por el valor de num1
num2 = int(num1)
print(num2) # 5
print(type(num2)) #<class 'int'>

# ---

edad = input("Dime tu edad: ")
print(type(edad)) # <class 'str'>

edad = int(edad)
print(type(edad)) # <class 'int'>

nueva_edad = 1 + edad
print(nueva_edad) # 31

# ---

mi_valor = 1

otro_valor = str(mi_valor)
print(type(otro_valor)) # <class 'str'>

anios = input("Dime tu edad: ")

aniios = int(anios)
print(type(aniios)) #<class 'int'>


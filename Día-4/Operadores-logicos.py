# Que pasa si necesitamos una sola variable para comparar dos comparaciones ?? 
#* Las operaciones logicas en español son:
#* Y  => AND
#* O  => OR
#* NO => NOT

#* Por ejemplo: 
#* Quiero un helado de frutilla AND chocolate (ambas condiciones se deben cumplir)
variable_and = 4 < 5 and 5 < 1   # False porque 5 NO es menor a 1. Una de las condiciones no se cumplió.

variable_and2 = 4 < 5 and 5 < 10 # True ya que AMBAS condiciones se han cumplido.

variable_and3 = 55 == 55 and 'mi perro' == 'mi perro' # True ya que ambas condiciones se cumplen, ambos int son iguales AND ambos strings son iguales.

texto = "Esta es una frase muy breve para mis queridos alumnos de Kodland"
variable_and4 = 'frase' in texto and 'Kodland' in texto # True, ya que AMBAS palabras se encuentran en la variable texto. Tambien se puede encerrar entre parentesis: ('frase' in texto) and ('Kodland' in texto)


#* Quiero un helado de chocolate OR dulce de leche (se pueden cumplir ambas aunque con que se cumpla una de las condiciones dadas, el resultado será True)

variable_or = 10 == 10 or 3 == 3 # True ya que AMBAS condiciones se cumplen aunque SOLO UNA HUBIESE BASTADO

variable_or2 = 10 == 1 or 3 == 3 # True ya que, si bien la primera condicion es falsa (10 no es igual a 1) la segunda condición si es verdadera. Con lo cual, eso basta para nuestro operador OR. XD

texto2 = "Esta es otra frase para mis futuros colegas"

variable_or3 = 'colegas' in texto2 and 'Kodland' in texto2 # False ya que SOLO UNA condicion se cumple y el operador AND pide que ambas se cumplan

variable_or4 = 'colegas' in texto2 or 'Kodland' in texto2 # True ya que utilizamos la condicion OR, con que se cumpla la primera condicion estamos GOD


#* NOT quiero un helado, quiero una gaseosa (No importa la condición, para que el resultado sea True, la condición NO se deberá cumplir.)

mi_bool = 'a' == 'a' # True ya que, obviamente el str 'a' es igual al str 'a'

mi_bool2 = not 'a' == 'a' # False ya que not se fija: SI NO ES VERDAD que el str 'a' es igual al str 'a'

mi_bool3 = not ('a' != 'a') # True ya que NO ES VERDAD que el str 'a' es DISTINTO al str 'a' (no es verdad que es distinto, ya que es igual)

print(mi_bool)
print(mi_bool2)
print(mi_bool3)
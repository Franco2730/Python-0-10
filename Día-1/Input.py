# Ahora vamos a ver lo que es una función INPUT. Ya sabemos que podemos mostrar en pantalla, Pero, un usuario puede brindarnos información ¿? Si le queremos pedir a un usuario que nos diga su nombre sería algo como:

#* Introduce tu nombre.
 
# Claro que sería en inglés, con lo cual quedaría algo como:
# Input y entre paréntesis la explicación, lo que el usuario debe ingresar

#* Input(“Tu nombre”) 

# Esta información se perderá, ya que no la estamos guardando en ningún lugar, en los próximos días, estaremos aprendiendo como retener esa información para luego, hacer algo con ella. Ahora solamente vamos a imprimir lo que el usuario ingrese en consola. 
# Suena difícil ¿? Solamente debemos encerrar todo entre paréntesis y decirle que lo imprima. :D 

#input("Dime tu nombre: ") # En consola se mostrará esa oración y estará a la espera de un ingreso. 

# Cuando le colocamos algo, el sistema olvidó esa información ya que no se ha mostrado, ni guardado. 

print(input("Dime tu nombre: ")) # Si colocamos Franco, aparecerá Franco abajo.
# Dime tu nombre: Franco
# Franco

#  Has podido observar cuando inicias sesión en un divertido juego que este te dice: ¡Oye tú! ¡Soldado! ¿Cómo es tu nombre? Y cuando tu escribes tu nombre, por ejemplo, Agustín. Aparece otra pantalla que dice: ¡Es un placer Agustín! La resistencia te estaba esperando.   
#  Recuerdas que habíamos dicho que todo lo que estuviera entre “o ‘ iba a ser un string ¿ un string no se puede sumar pero se puede concatenar, que sería como juntar. Entonces, lo que vamos a hacer es concatenar los mensajes genéricos, ¡a tu nombre de soldado! Estas listo??

print("Bienvenido a la base soldado " + input("Dime tu nombre: "))

#* Dime tu nombre: Franco
#* Bienvenido a la base soldado Franco



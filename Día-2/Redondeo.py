# Que pasa si necesitamos dividir 90 Usd entre 7 amigos para pagar nuestra cena ? El resultado sería 12.857264... 
# Claramente no es un número apropiado para socializar... Para eso tenemos a nuestro amigo round. Cabe aclarar que si el decimal del número es 5 o mayor a 5, el número se va a redondear para arriba mientras que si dicho decimal es 4, 3, 2 o 1, el número se va a redondear para abajo.

# resultado = round(90/7) 

# print(resultado) # 13

resultado = (90/7)
redondeo = round(resultado)

print(redondeo) # 13

#--------------

# Que pasa si queremos ver únicamente dos decimales ? Algo MUY importante a tener en cuenta es que round nos solicita 2 parametros. El primero es obligatorio y es el número que vamos a redondear y el segundo parametro es justamente esto, es la cantidad de decimales que queremos en nuestro resultado.
valor = round(95.66666666666666666666, 2)

print(valor) # 95.67
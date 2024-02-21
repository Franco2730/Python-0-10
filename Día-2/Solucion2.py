nombre = input("Hola, me podrías decir tu nombre por favor ? ")
saludoVentas = input("Hola " +nombre+" espero que estes muy bien. Me podrias decir cuantas ventas has logrado este mes ? ")

ventas = float(saludoVentas)

comision = round(ventas * 13 / 100, 2)

finPrograma = (f"{nombre} tu comision este mes ha sido de {comision} teniendo en cuenta que tus ventas han sido de: {ventas} segun nos has informado. ¡Felicidades!")

print(finPrograma)

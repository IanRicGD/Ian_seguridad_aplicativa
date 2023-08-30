#Primera actividad
#Generar un código para mostrar una cadena al revés

string="Anita Lava La Tina"

string=string.replace(" ","")

if (string.lower() == (string[::-1].lower())):
    print("Es un palindromo")
else:
    print("No es un palindromo")

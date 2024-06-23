# Funcion que cuenta las vocales de una cadena
def contvocales(cadena: str):
    contador = 0

    for letra in cadena:
        # Vocales sin tilde
        condicional = letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u'
        # Vocales tildadas
        condtilde = letra == 'á' or letra == 'é' or letra == 'í' or letra == 'ó' or letra == 'ú'

        if condicional or condtilde:
            contador+=1
    
    return contador

# Codigo principal
while True:
    cadena1 = str(input('Ingrese una cadena para contar las vocales en ella ("-" para salir): '))
    if cadena1 == '-':
        break
    else:
        cantidad = contvocales(cadena1)
        print(f'Hay {cantidad} vocales en la cadena.')
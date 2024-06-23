# Funcion recursiva para hallar el factorial de un numero
def factnum(num: int): # El parametro debe ser de tipo 'int'
    if num == 0 or num == 1:
        return 1
    else:
        return num*factnum(num-1)

# Codigo principal
while True:
    numero = int(input('Ingrese un numero para encontrar el factorial de este (x<0 para salir): '))
    if numero < 0:
        break
    else:
        factorial = factnum(numero)
        print(f'El factorial de {numero} es {factorial}')
    
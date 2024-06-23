import os       # Se cambia la ubicacion a la carpeta de la consola (por si acaso)
os.chdir('./')  # Y sera el destino del duplicado

### Funcion para encontrar un archivo en la carpeta principal
def AreYouHere(file_name: str): # El parametro debe ser de tipo 'str'
    for file in os.listdir():
        if file == file_name:
            return True
    
    return False

### Funcion para copiar el contenido de un archivo en otro
def FileCopycat(file_1, file_2: str):
    if file_1.closed:
        print('El archivo de origen esta cerrado.')
        return False
    elif AreYouHere(file_2):
        Uconfirm = str(input('El archivo de destino ya existe. Si continua, el duplicado lo reemplazara. (s/y para continuar): '))
        if not(Uconfirm.lower() == 's' or Uconfirm.lower() == 'y'):
            return False
    
    FileIStr = file_1.read()
    FileO = open(file_2, "w")
    FileO.write(FileIStr)
    FileO.close()
    file_1.close()
    return True

### Codigo principal
fileInput = open("./CC112D_proyecto/parte-1/code_1.py", 'r')
fileOut = ''

# Nombre de la copia (sin simbolos, espacios ni mas de veinte caracteres)
fileOutName = str(input("Ingrese un nombre para el duplicado (sin simbolos o espacios): "))
while fileOutName.isalnum() == False or len(fileOutName) > 20:
    fileOutName = str(input("Nombre invalido: "))

# Extension de la copia (sin simbolos, numeros ni espacios)
fileOutExt = str(input("Ingrese un tipo de archivo ('none' para ninguno): "))
while fileOutExt.isalpha() == False:
    fileOutName = str(input("Extension invalida: "))

# Concatenando el nombre y la extension
if fileOutExt.lower() == 'none':
    fileOut = fileOutName
else:
    fileOut = fileOutName + '.' + fileOutExt

if FileCopycat(fileInput, fileOut):
    print(f"Se creo una copia de {fileInput.name} con nombre {fileOut}")
else:
    print('No se pudo crear la copia.')
### Funcion que agrega un contacto nuevo en la lista
def addContact(lista: list, contacto: str, num: int):
    lista[contacto] = num
    print('Contacto agregado')

### Funcion que muestra la lista de contactos
def showContList(lista: list):
    for contact in lista.keys():
        print(f'- {contact}\t{lista[contact]}')

### Funcion que elimina un contacto en la agenda
def delContact(lista: list, contacto: str):
    if lista.get(contacto) != None:
        lista.pop(contacto)
        print(f'Contacto "{contacto}" eliminado')
    else:
        print('Contacto no encontrado')
    
### Funcion que busca por nombre un contacto en la agenda
def searchCont(lista: list, contacto: str):
    if lista.get(contacto) != None:
        print('-', contacto, '(' + str(lista[contacto]) + ')')
    else:
        print('Contacto no encontrado')

### Funcion principal
def runCellphone(agenda: list):
    while True:
        choosing = int(input("""=====Ingrese una opcion=====
                    [1] Agregar nuevo contacto / Actualizar existente: 
                    [2] Mostrar todos los contactos
                    [3] Buscar contacto por nombre
                    [4] Eliminar un contacto
                    [**] Salir
                    :::: """))
        if choosing == 1:
            NewContStr = str(input(('Ingrese un nombre para el contacto: ')))
            NewContInt = int(input('Ingrese el numero del contacto: '))
            addContact(agenda, NewContStr, NewContInt)
        elif choosing == 2:
            print('Mostrando', str(len(agenda)), 'contactos...')
            showContList(agenda)
        elif choosing == 3:
            LookFor = str(input('Ingrese el nombre del contacto: '))
            searchCont(agenda, LookFor)
        elif choosing == 4:
            Goodbye = str(input('Ingrese el nombre del contacto a eliminar: '))
            delContact(agenda, Goodbye)
        else:
            break

### Codigo principal
agendaTelf = {

}
runCellphone(agendaTelf)


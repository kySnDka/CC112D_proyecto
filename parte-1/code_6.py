class BankAcc:
    dinero = 0

    ### Funcion para depositar dinero
    def deposit(self):
        depos = int(input('Ingrese la cantidad que desea depositar: '))
        if depos < 0:
            print('La cantidad no puede ser menor a cero. Transaccion cancelada.')
        else:
            self.dinero+=depos
            print(f'Se ha depositado ${depos} a la cuenta')

    ### Funcion para retirar dinero
    def withdraw(self):
        withd = int(input('Ingrese la cantidad que desea retirar: '))
        if withd < 0:
            print('La cantidad no puede ser menor a cero. Transaccion cancelada.')
        elif (self.dinero-withd) < 0:
            print('Saldo insuficiente. Transaccion cancelada.')
        else:
            self.dinero-=withd
            print(f'Se ha retirado ${withd} de la cuenta.')

### Funcion principal
def runSys(cuenta: BankAcc):
    while True:
        choosing = int(input("""
                    -----Realizar accion-----
                    [1] Retiro de efectivo
                    [2] Deposito a la cuenta
                    [3] Mostrar saldo
                    [**] Salir
                    >>> """))
        if choosing == 1:
            cuenta.withdraw()
        elif choosing == 2:
            cuenta.deposit()
        elif choosing == 3:
            print('Saldo de la cuenta: $' +  str(cuenta.dinero))
        else:
            break

### Codigo principal
CuentaBanco = BankAcc()
runSys(CuentaBanco)
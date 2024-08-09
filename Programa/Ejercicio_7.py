class CuentaBancaria:
    def __init__(self, numero_cuenta, propietarios, balance):
        self.numero_cuenta = numero_cuenta
        self.propietarios = propietarios
        self.balance = balance

    def depositar(self, monto):
        if monto > 0:
            self.balance += monto
            print(f"Depósito {monto}. Nuevo balance{self.balance}.")
        else:
            print("El monto a depositar debe ser positivo.")

    def retirar(self, monto):
        if monto > 0:
            if monto <= self.balance:
                self.balance -= monto
                print(f"retiro a realizar {monto}. Nuevo balance {self.balance}.")
            else:
                print("Fondos insuficientes para realizar el retiro.")
        else:
            print("El monto a retirar debe ser positivo.")

    def aplicar_cuota_manejo(self):
        cuota = self.balance * 0.02
        self.balance -= cuota
        print(f"Cuota de manejo aplicada: ${cuota}. Nuevo balance: ${self.balance}.")

    def mostrar_detalles(self):
        print(f"Número de cuenta: {self.numero_cuenta}")
        print(f"Propietarios: {', '.join(self.propietarios)}")
        print(f"Balance: ${self.balance}")

# Ejemplo de uso
objeto_cuenta = CuentaBancaria("123456789", ["Juan Pérez", "Ana Gómez"], 1000)

objeto_cuenta.mostrar_detalles()
objeto_cuenta.depositar(1230)
objeto_cuenta.retirar(250)
objeto_cuenta.aplicar_cuota_manejo()
objeto_cuenta.mostrar_detalles()

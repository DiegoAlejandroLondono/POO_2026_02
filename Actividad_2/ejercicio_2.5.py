from enum import Enum

class TipoCuenta(Enum):
    AHORROS = 1
    CORRIENTE = 2

class Cuenta_bancaria():

    def __init__(self, nombres: str, apellidos: str, numero_cuenta: int, tipo_de_cuenta: TipoCuenta, interes_mensual: float, saldo: float = 0):
        self.nombres = nombres
        self.apellidos = apellidos
        self.numero_cuenta = numero_cuenta
        self.tipo_de_cuenta = tipo_de_cuenta
        self.saldo = saldo
        self.interes_mensual = interes_mensual/100


    def show(self) -> None:
        print("Nombres: ", self.nombres)
        print("Apellidos: ", self.apellidos)
        print("Número de cuenta: ", self.numero_cuenta)
        print("Tipo de cuenta: ", self.tipo_de_cuenta.name)
        print("Saldo: ", self.saldo)

    def saldo_actual(self)-> float:
        return self.saldo
    
    def consignar(self, monto) -> bool:
        if monto > 0:
            self.saldo += monto
            print(f"Se han consignado ${monto} en la cuenta. El nuevo saldo es ${self.saldo}.")
            return True
        else:
            print("El monto a consignar debe ser mayor a $0")
            return False

    def retirar (self, monto) -> bool:

        if (monto>0 and monto <= self.saldo):
            self.saldo -= monto
            print(f"Se ha retirado ${monto} de la cuenta. El nuevo saldo es {self.saldo}")
            return True
        else:
            print("No se cuenta con suficiente saldo para completar la operación.")
            return False
    
    def aplicar_interes_mensual(self) -> None:
        self.saldo += self.saldo * self.interes_mensual
        print(f"Se ha aplicado un interés mensual del {self.interes_mensual*100}%. El nuevo saldo es {self.saldo}.")

def Main():
    cuenta = Cuenta_bancaria("Pedro","Pérez",123456789,TipoCuenta.AHORROS, 1.25);
    cuenta.show()
    cuenta.consignar(200000);
    cuenta.consignar(300000);
    cuenta.retirar(400000);
    cuenta.aplicar_interes_mensual()


if __name__ == "__main__":
    Main()
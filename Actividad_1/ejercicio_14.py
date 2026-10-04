

class Operaciones:

    #Metodos estaticos para poder acceder a los metodos sin necesidad de instanciar la clase.
    @staticmethod
    def cuadrado(numero):
        return numero ** 2

    @staticmethod
    def cubo(numero):
        return numero ** 3


class Main:
    def __init__(self):

        print("Calculo de cuadrado y cubo de un número!")
        self.numero = float(input("Ingrese un número: "))
        print(f"El cuadrado de {self.numero} es: {Operaciones.cuadrado(self.numero)}")
        print(f"El cubo de {self.numero} es: {Operaciones.cubo(self.numero)}")



if __name__ == "__main__":
    Main()
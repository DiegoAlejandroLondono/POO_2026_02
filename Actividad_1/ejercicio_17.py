import numpy as np


class Circulo:

    @staticmethod
    def area(radio):
        return round(np.pi*(radio ** 2), 4)

    @staticmethod
    def perimetro(radio):
        return round(2 * np.pi * radio, 4)


class Main:
    def __init__(self):
        print("Calculo de area y perimetro de un circulo!")
        self.radio = float(input("Ingrese el radio del circulo: "))
        print(f"El area del circulo es: {Circulo.area(self.radio)}")
        print(f"El perimetro del circulo es: {Circulo.perimetro(self.radio)}")


if __name__ == "__main__":
    Main()

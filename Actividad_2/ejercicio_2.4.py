from enum import Enum
import numpy as np


class TipoTriangulo(Enum):
    EQUILATERO = 1
    ISOSELES = 2
    ESCALENO = 3

class Rectangulo():
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self) -> float:
        return self.base*self.altura

    def perimetro(self) -> float:
        return 2*self.base + 2*self.altura

class Cuadrado():
    def __init__(self, lado):
        self.lado = lado

    def area(self) -> float:
        return self.lado**2

    def perimetro(self) -> float:
        return 4*self.lado

class Rombo():
    def __init__(self, diagonal1, diagonal2):
        self.diagonal1 = diagonal1
        self.diagonal2 = diagonal2

    def area(self) -> float:
        return (self.diagonal1*self.diagonal2)/2
        

    def perimetro(self) -> float:
        return 2*(self.diagonal1**2 + self.diagonal2**2)**0.5

#Ya que no se especifica. Se toma el caso en el que el trapecio es isoseles
class Trapecio():
    def __init__(self, base1, base2, altura):
        self.base1 = base1
        self.base2 = base2
        self.altura = altura


    def area(self) -> float:
        return (self.base1+self.base2)*self.altura/2

    def perimetro(self) -> float:
        return (self.base1 + self.base2)+2*(((self.base1-self.base2)/2)**2 + self.altura**2)**0.5

class Triangulo():
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self) -> float:
        return (self.base*self.altura)/2

    def perimetro(self) -> float:
        return self.hipotenusa() + self.base + self.altura
    
    def hipotenusa(self) -> float:
        return (self.altura**2 + self.base**2)**0.5

    def tipo(self) -> TipoTriangulo:
        if self.base == self.altura:
            return TipoTriangulo.ISOSELES
        else:
            return TipoTriangulo.ESCALENO
        

class Circulo():
    def __init__(self, radio):
        self.radio = radio

    def area(self) -> float:
        return np.pi*(self.radio**2)

    def perimetro(self) -> float:
        return 2*np.pi*self.radio
    

def Main():
    circ = Circulo(2)
    rect = Rectangulo(1,2)
    cuad = Cuadrado(3)
    tria = Triangulo(3,5)
    romb = Rombo(3,4)
    trap = Trapecio(4,3,2)

    print("El area del circulo es: ",circ.area())
    print("El perimetro del circulo es: ", circ.perimetro())
    print()
    print("El area del rectangulo es: ",rect.area())
    print("El perimetro del rectangulo es: ", rect.perimetro())
    print()
    print("El area del cuadrado es: ",cuad.area())
    print("El perimetro del cuadrado es: ", cuad.perimetro())
    print()
    print("El area del triangulo es: ",tria.area())
    print("El perimetro del triangulo es: ", tria.perimetro())
    print("La hipotenusa del triangulo rectangulo es: ",tria.hipotenusa())
    print("Es un triangulo ", tria.tipo().name )
    print()
    print("El area del rombo es: ",romb.area())
    print("El perimetro del rombo es: ", romb.perimetro()) 
    print()
    print("El area del trapecio es: ",trap.area())
    print("El perimetro del trapecio es: ", trap.perimetro()) 

if __name__ == "__main__":
    Main()



from enum import Enum     #En python se debe usar el modulo enum para crear tipo de datos enumerados

#Se crea la clase de dato "TipoPlaneta" de forma que cuando se enumeren se estara usando un objeto de la clase TipoPlaneta
class TipoPlaneta(Enum):
    TERRESTRE = 1 
    GASEOSO = 2
    ENANO = 3



class Planeta():
    #Python identifica dinamicamente los tipos. Se pueden nombrar los "Type hints" de los atributos, pero python no obliga que esto se cumpla.
    #Actuan más como notas para el programador. Por lo que en codigo critico vale la pena hacer checkeadores de tipo antes de dejar seguir al parametro.
    
    #Ya que el ejercicio se planteo en Java. Para asemejarse al planteamiento, se usan valores por defecto, y Type hints.
    def __init__(
        self, 
        nombre: str | None = None,
        satelites: int = 0,
        masa: float = 0.0,
        volumen: float = 0.0,
        diametro: int = 0,
        distancia: int = 0,
        tipo: TipoPlaneta = TipoPlaneta.TERRESTRE,
        observable: bool = False,
        orbita: float = 0,
        rotacion: float = 0 
    ):
        self.nombre = nombre
        self.satelites = satelites
        self.masa = masa
        self.volumen = volumen
        self.diametro = diametro
        self.distancia = distancia
        self.tipo = tipo
        self.observable = observable
        self.orbita = orbita
        self.rotacion = rotacion

    def show(self) -> None:    #Hint de salida
        print(f"Nombre: {self.nombre}")
        print(f"Satélites: {self.satelites}")
        print(f"Masa: {self.masa}")
        print(f"Volumen: {self.volumen}")
        print(f"Diámetro: {self.diametro}")
        print(f"Distancia: {self.distancia}")
        #Se utiliza tipo.name para mostrar el nombre el enumerado. Si se quisiese mostrar el valor, se usaria tipo.value.
        print(f"Tipo de planeta: {self.tipo.name}")
        print(f"Observable: {self.observable}")
        print(f"Periodo orbital: {self.orbita} años")
        print(f"Periodo de rotacion: {self.rotacion} dias")

    def density(self) -> float:
        return self.masa/self.volumen

    def exterior(self) -> bool:
        UA = 149597870     #Dato en kilometros
        distanciakm = self.distancia*1000000  #convertir distancia de Mkm a km
        return distanciakm > 3.4*UA

            

def Main():

    Tierra = Planeta("Tierra", 1, 5.972*10**24, 1.08321*10**12, 12742, 150, TipoPlaneta.TERRESTRE, True, 1, 1)
    Jupiter = Planeta("Jupiter", 79, 1.898*10**27, 1.43128*10**15, 139820, 779, TipoPlaneta.GASEOSO, True, 11.86, 0.42)

    Tierra.show()
    print(f"La densidad de {Tierra.nombre} es {Tierra.density()} kg/km^3")
    if Tierra.exterior():
        print(f"{Tierra.nombre} es un planeta exterior")
    else:
        print(f"{Tierra.nombre} No es un planeta exterior")

    print()

    Jupiter.show()
    print(f"La densidad de {Jupiter.nombre} es {Jupiter.density()} kg/km^3")
    if Jupiter.exterior():
        print(f"{Jupiter.nombre} es un planeta exterior")
    else:
        print(f"{Jupiter.nombre} No es un planeta exterior")


if __name__ == "__main__":
    Main()

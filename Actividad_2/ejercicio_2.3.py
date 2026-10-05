from enum import Enum
import numpy as np
from typing import Any

class TipoTransmision(Enum):
    MANUAL = 1
    AUTOMATICA = 2
    CVT = 3
    DCT = 4

class TipoCombustible(Enum):
    GASOLINA = 1
    BIOETANOL = 2
    DIESEL = 3
    BIODIESEL = 4
    GAS_NATURAL = 5

class TipoAutomovil(Enum):
    CARRO_CIUDAD = 1
    SUBCOMPACTO = 2
    COMPACTO = 3
    FAMILIAR = 4
    EJECUTIVO = 5
    SUV = 6
    DEPORTIVO = 7

class TipoColor(Enum):
    BLANCO = 1
    NEGRO = 2
    ROJO = 3
    NARANJA = 4
    AMARILLO = 5
    VERDE = 6
    AZUL = 7
    VIOLETA = 8

#Se usa _ antes del atributo para indicar AL PROGRAMADOR que son atributos internos y no deberian ser accesibles. Es una convencion, no impide que sean accesibles.
class Automovil():
    def __init__(self, 
        marca: str, 
        modelo: str, 
        motor: float, 
        transmision: TipoTransmision, 
        combustible: TipoCombustible, 
        tipo: TipoAutomovil, 
        puertas: int, 
        asientos: int, 
        maxvel: float, 
        color: TipoColor, 
        velocidad: int = 0
        ):

        self._marca = marca 
        self._modelo = modelo
        self._motor = motor
        self._transmision = transmision
        self._combustible = combustible
        self._tipo = tipo
        self._puertas = puertas
        self._asientos = asientos
        self._maxvel = maxvel
        self._color = color
        self._velocidad = velocidad
        self._multa = 0
        self._vecesmulta = 0


    #En python se puede acceder y modififcar los atributos en cualquier momento
    #Para la actividad se construyen set y get como pide el ejercicio. Se usa getattr y setattr para modificar sabiendo el nombre del atributo.
    #En el estado actual, si se ingresa un atributo que no existe, se crearia un atributo nuevo con dicho valor. Pero se podrian añadir comprobaciones.
    def set(self, atributo, valor) -> None:
        setattr(self, "_" + atributo, valor)

    def get(self, atributo: str) -> Any:     
        return getattr(self, "_" + atributo)

    def acelerar(self, aceleracion: float):
        self._velocidad += np.abs(aceleracion)
        if self._velocidad > self._maxvel:
            self._velocidad = self._maxvel
            self._vecesmulta += 1
            self._multa += (20*self._vecesmulta)
            print("No se puede acelerar tanto. Velocidad maxima fijada")
            print(f"Multa por tratar de superar la velocidad maxima. Se ha agregado ${20*self._vecesmulta} a tus multas")

    def desacelerar(self, aceleracion: float):
        self._velocidad -= np.abs(aceleracion)
        if self._velocidad < 0:
            self._velocidad = 0
            print("No se puede desacelerar mas. Velocidad fijada en 0")

    def es_automatico(self) -> bool:
        return self._transmision != TipoTransmision.MANUAL

    def frenar(self) -> None:
        self._velocidad = 0

    def tiempo_llegada(self, distancia) -> float:
        if self._velocidad != 0:
            return distancia / self._velocidad
        else:
            return (np.inf) 
        
    def show(self) -> None:
        print("Marca: ", self._marca)
        print("Modelo: ", self._modelo)
        print("Motor: ", self._motor)
        print("Transmision: ", self._transmision.name)
        print("Combustible: ", self._combustible.name)
        print("Tipo: ", self._tipo.name)
        print("Puertas: ", self._puertas)
        print("Asientos: ", self._asientos)
        print("Velocidad Máxima: ", self._maxvel)
        print("Color: ", self._color.name)
        print("Velocidad Actual: ", self._velocidad)

    def multas(self) -> bool:
        return self._multa > 0

    def valor_multas(self) -> float:
        return self._multa
    

def Main():

    GTR = Automovil("Nissan", "GT-R 2024", 3.8, TipoTransmision.DCT, TipoCombustible.GASOLINA, TipoAutomovil.DEPORTIVO, 2, 4, 330, TipoColor.ROJO, 0) 

    GTR.show()

    if GTR.es_automatico():
        print("El auto es automatico")
    else:
        print("El auto es manual")

    GTR.set("velocidad", 100)
    GTR.acelerar(20)
    print(f"La velocidad actual es: {GTR.get('velocidad')} km/h")
    GTR.desacelerar(50)
    print(f"La velocidad actual es: {GTR.get('velocidad')} km/h")
    GTR.frenar()
    print(f"La velocidad actual es: {GTR.get('velocidad')} km/h")
    GTR.acelerar(100)
    print(f"La velocidad actual es: {GTR.get('velocidad')} km/h")

    if GTR.multas():
        print("Se tienen multas")
    else:
        print("No se tienen multas")
    GTR.acelerar(300)
    GTR.acelerar(1)
    GTR.acelerar(1)

    if GTR.multas():
        print("Se tienen multas")
        print(f"Se deben ${GTR.valor_multas()} en multas")
    else:
        print("No se tienen multas")

    GTR.desacelerar(500)


if __name__ == "__main__":
    Main()

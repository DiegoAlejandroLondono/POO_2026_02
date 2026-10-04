

class Operaciones:
    def __init__(self):
        self.suma = 0
        self.x = 0
        self.y = 0

    def Operacion1(self):
        self.suma = self.suma + self.x

    def Operacion2(self):
        self.x = self.x + (self.y)**2

    def Operacion3(self):
        self.suma = self.suma + (self.x/self.y)


class Main:
    #Se hace dentro del metodo init para que prueba_escritorio sea una variable local.
    def __init__(self):                                                             
        prueba_escritorio = Operaciones()

        #Se hizo la versión con input para los atributos como en el ejemlo de la clase
        prueba_escritorio.suma = float(input("Ingrese el valor de suma: "))                       
        prueba_escritorio.x = float(input("Ingrese el valor de x: "))

        prueba_escritorio.Operacion1()

        prueba_escritorio.y = float(input("Ingrese el valor de y: "))

        prueba_escritorio.Operacion2()
        prueba_escritorio.Operacion3()

        print(f"EL VALOR DE LA SUMA ES: {prueba_escritorio.suma}")


Main()

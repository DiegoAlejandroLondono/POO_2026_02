
class Persona():
    #Constructor para inicializar los atributos
    def __init__(self, nombre, apellido, id, año, pais, genero):
        self.nombre = nombre
        self.apellido = apellido
        self.id = id
        self.año = año
        self.pais = pais
        self.genero = genero

    #Metodo para mostrar los atributos del objeto
    def show(self):
        print(f"Nombre: {self.nombre}, Apellido: {self.apellido}, Documento: CC {self.id}, Año de nacimiento: {self.año}, Pais: {self.pais}, Genero: {self.genero}")



def Main():

    andres = Persona("Andrés", "Perez", 1004534509, 1995, "Colombia", "H")
    javier = Persona("Javier", "Cardona", 71647398, 1967, "Perú", "H")

    andres.show()
    javier.show()


if __name__ == "__main__":
    Main()
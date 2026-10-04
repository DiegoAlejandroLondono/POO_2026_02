#A diferencia del ejemplo. Decidí almacenar las edades en atributos de instancias en lugar de variables globales. Para eso, debo inicializar una instancia de la clase edades.

class Edades:

    #Con __init__ puedo pasar un argumento a la clase y guardarlo en un atributo de instancia
    def __init__(self, edad_Juan):                                      
        self.edad_juan = edad_Juan

    # Debo pasar self como argumento para poder acceder a los atributos de instancia
    def edad_Alberto(self):                                             
        # En python puedo definir un atributo de instancia dentro de un método, pero no es recomendable hacerlo. Se recomienda definirlo en el __init__. 
        self.edad_alberto = round(float(self.edad_juan)*2/3, 2)  
        #Hago esto como test, y en futuros codigos lo hare de la forma recomendada.
        return self.edad_alberto                                        

    def edad_Ana(self):
        #Redondear a 2 decimales
        self.edad_ana = round(float(self.edad_juan)*4/3, 2)             
        return self.edad_ana                

    def edad_Mama(self):
        self.edad_mama = self.edad_juan + self.edad_alberto + self.edad_ana
        return self.edad_mama


class Main:
    def __init__(self):
        self.Entrada = float(input("Ingrese la edad de Juan: "))

        #Creo una instancia de la clase edades como atributo de main y le paso la edad de Juan como argumento
        self.edades = Edades(self.Entrada)                               

        #Llamo al método edad_Alberto y no hace falta pasarle la instancia de la clase edades como argumento, ya que el metodo accede a los atributos de instancia a través de self.
        self.edades.edad_Alberto()                               

        #Llamo al método edad_Ana
        self.edades.edad_Ana()                                   

        #Llamo al método edad_Mama. Ya que los valores son atributos, esta debia ser llamada después de las otras dos.
        self.edades.edad_Mama()                                  

        print(f"La edad de Juan es: {self.edades.edad_juan}")
        print(f"La edad de Alberto es: {self.edades.edad_alberto}")
        print(f"La edad de Ana es: {self.edades.edad_ana}")
        print(f"La edad de la mamá es: {self.edades.edad_mama}")


Main()

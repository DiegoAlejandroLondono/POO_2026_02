

class Empleado:
    #Se piden los datos de atributo al momento de iniciar la instancia de la clase
    def __init__(self, sueldo_por_hora, horas_por_semana, porcentaje_rete_fuente):
        self.sueldo_por_hora = sueldo_por_hora
        self.horas_por_semana = horas_por_semana
        self.porcentaje_rete_fuente = porcentaje_rete_fuente

        #Se definen los atributos a calcular como None, para que no tengan un valor inicial y se puedan calcular posteriormente
        self.salario_bruto = None
        self.salario_neto = None
        self.rete_fuente = None                                                    

    def calcular_salario_bruto(self):
        self.salario_bruto = self.sueldo_por_hora * self.horas_por_semana
        return self.salario_bruto

    def calcular_rete_fuente(self):
        self.rete_fuente = self.calcular_salario_bruto() * (self.porcentaje_rete_fuente / 100)
        return self.rete_fuente

    def calcular_salario_neto(self):
        self.salario_neto = self.calcular_salario_bruto() - self.calcular_rete_fuente()
        return self.salario_neto


class Main:
    def __init__(self, ):

        #Se instancia con los valores que da el ejercicio, pero se puede cambiar por input() para que el usuario ingrese los valores.
        empleado1 = Empleado(5000, 48, 12.5)

        print(f"Salario bruto: ${empleado1.calcular_salario_bruto()}")
        print(f"Rete fuente: ${empleado1.calcular_rete_fuente()}")
        print(f"Salario neto: ${empleado1.calcular_salario_neto()}")


#Sirve para que el código solo se ejecute si se ejecuta el archivo directamente, y no si se importa como módulo en otro archivo
if __name__ == "__main__":                                              
    Main()


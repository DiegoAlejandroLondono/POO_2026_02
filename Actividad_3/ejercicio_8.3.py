
import tkinter as tk
from tkinter import ttk, messagebox
import numpy as np
import os


class FiguraGeometrica():
    def __init__(self):
        self.volumen = None
        self.superficie = None


#Las clases hijas heredan los atributos de FiguraGeometrica. super() permite ejecutar el constructor de la clase padre.
class Cilindro(FiguraGeometrica):
    def __init__(self, radio: float, altura: float):
        super().__init__()
        self.radio = radio
        self.altura = altura

    def calcular_volumen(self) -> float:
        self.volumen = np.pi*self.radio**2*self.altura
        return self.volumen

    def calcular_superficie(self) -> float:
        self.superficie = 2*np.pi*self.radio*(self.radio+self.altura)
        return self.superficie


class Esfera(FiguraGeometrica):
    def __init__(self, radio: float):
        super().__init__()
        self.radio = radio

    def calcular_volumen(self) -> float:
        self.volumen = (4/3)*np.pi*self.radio**3
        return self.volumen

    def calcular_superficie(self) -> float:
        self.superficie = 4*np.pi*self.radio**2
        return self.superficie


class Piramide(FiguraGeometrica):
    def __init__(self, base: float, altura: float, apotema: float):
        super().__init__()
        self.base = base
        self.altura = altura
        self.apotema = apotema

    def calcular_volumen(self) -> float:
        self.volumen = self.base**2*self.altura/3
        return self.volumen

    def calcular_superficie(self) -> float:
        self.superficie = self.base**2 + 2*self.base*self.apotema
        return self.superficie


class Cubo(FiguraGeometrica):
    def __init__(self, lado: float):
        super().__init__()
        self.lado = lado

    def calcular_volumen(self) -> float:
        self.volumen = self.lado**3
        return self.volumen

    def calcular_superficie(self) -> float:
        self.superficie = 6*self.lado**2
        return self.superficie


#Asumo prisma rectangular ya que no se especifico  
class Prisma(FiguraGeometrica):
    def __init__(self, largo: float, ancho: float, altura: float):
        super().__init__()
        self.largo = largo
        self.ancho = ancho
        self.altura = altura

    def calcular_volumen(self) -> float:
        self.volumen = self.largo*self.ancho*self.altura
        return self.volumen

    def calcular_superficie(self) -> float:
        self.superficie = 2*(self.largo*self.ancho + self.largo*self.altura + self.ancho*self.altura)
        return self.superficie


#os.path permite construir rutas independientemente de la carpeta desde la que se ejecuta
RUTA = os.path.dirname(os.path.abspath(__file__))


class VentanaCilindro():
    def __init__(self, ventana_padre):

        #Toplevel crea una ventana secundaria sin crear otra aplicación Tk.
        self.ventana = tk.Toplevel(ventana_padre)
        self.ventana.title("Cilindro")
        self.ventana.geometry("350x430")
        self.ventana.resizable(False, False)

        self.marco = ttk.Frame(self.ventana, padding=20)
        self.marco.pack(fill="both", expand=True)

        self.titulo = ttk.Label(self.marco, text="Cilindro", font=("Arial", 16, "bold"))
        self.titulo.pack(pady=5)

        #PhotoImage permite cargar imágenes PNG y utilizarlas en un Labe, y la imagen se guarda como atributo para mantener su referencia.
        self.imagen = tk.PhotoImage(file=os.path.join(RUTA, "cilindro.png"))

        #subsample reduce el tamaño de la imagen utilizando factores enteros. width() y height() obtienen sus dimensiones originales en píxeles. realiza división entera y max(1, ...) evita que el factor de reducción sea menor a 1.
        self.imagen = self.imagen.subsample(max(1, (self.imagen.width()+179)//180),max(1, (self.imagen.height()+139)//140))
        self.etiqueta_imagen = ttk.Label(self.marco, image=self.imagen)
        self.etiqueta_imagen.pack(pady=10)

        self.radio = ttk.Label(self.marco, text="Radio (cm):")
        self.radio.pack(anchor="w")
        self.campo_radio = ttk.Entry(self.marco)
        self.campo_radio.pack(fill="x", pady=4)

        self.altura = ttk.Label(self.marco, text="Altura (cm):")
        self.altura.pack(anchor="w")
        self.campo_altura = ttk.Entry(self.marco)
        self.campo_altura.pack(fill="x", pady=4)

        self.boton_calcular = ttk.Button(self.marco, text="Calcular", command=self.calcular)
        self.boton_calcular.pack(pady=12)

        self.resultado_volumen = ttk.Label(self.marco, text="Volumen: ")
        self.resultado_volumen.pack(anchor="w", pady=5)

        self.resultado_superficie = ttk.Label(self.marco, text="Superficie: ")
        self.resultado_superficie.pack(anchor="w", pady=5)

    def calcular(self):
        try:
            radio = float(self.campo_radio.get())
            altura = float(self.campo_altura.get())

            #Comprobacion de que las dimensiones sean positivas y finitas
            if not (0 < radio < float("inf") and 0 < altura < float("inf")):
                raise ValueError

            cilindro = Cilindro(radio, altura)

            self.resultado_volumen.config(text=f"Volumen: {cilindro.calcular_volumen():.2f} cm³")
            self.resultado_superficie.config(text=f"Superficie: {cilindro.calcular_superficie():.2f} cm²")

        except ValueError:
            messagebox.showerror("Error", "Ingrese valores numéricos positivos en todos los campos.")


class VentanaEsfera():
    def __init__(self, ventana_padre):

        self.ventana = tk.Toplevel(ventana_padre)
        self.ventana.title("Esfera")
        self.ventana.geometry("350x390")
        self.ventana.resizable(False, False)

        self.marco = ttk.Frame(self.ventana, padding=20)
        self.marco.pack(fill="both", expand=True)

        self.titulo = ttk.Label(self.marco, text="Esfera", font=("Arial", 16, "bold"))
        self.titulo.pack(pady=5)

        self.imagen = tk.PhotoImage(file=os.path.join(RUTA, "esfera.png"))
        self.imagen = self.imagen.subsample(max(1, (self.imagen.width()+179)//180), max(1, (self.imagen.height()+139)//140))
        self.etiqueta_imagen = ttk.Label(self.marco, image=self.imagen)
        self.etiqueta_imagen.pack(pady=10)

        self.radio = ttk.Label(self.marco, text="Radio (cm):")
        self.radio.pack(anchor="w")
        self.campo_radio = ttk.Entry(self.marco)
        self.campo_radio.pack(fill="x", pady=4)

        self.boton_calcular = ttk.Button(self.marco, text="Calcular", command=self.calcular)
        self.boton_calcular.pack(pady=12)

        self.resultado_volumen = ttk.Label(self.marco, text="Volumen: ")
        self.resultado_volumen.pack(anchor="w", pady=5)

        self.resultado_superficie = ttk.Label(self.marco, text="Superficie: ")
        self.resultado_superficie.pack(anchor="w", pady=5)

    def calcular(self):
        try:
            radio = float(self.campo_radio.get())

            if not (0 < radio < float("inf")):
                raise ValueError

            esfera = Esfera(radio)

            self.resultado_volumen.config(text=f"Volumen: {esfera.calcular_volumen():.2f} cm³")
            self.resultado_superficie.config(text=f"Superficie: {esfera.calcular_superficie():.2f} cm²")

        except ValueError:
            messagebox.showerror("Error", "Ingrese un radio numérico positivo.")


class VentanaPiramide():
    def __init__(self, ventana_padre):

        self.ventana = tk.Toplevel(ventana_padre)
        self.ventana.title("Pirámide")
        self.ventana.geometry("350x480")
        self.ventana.resizable(False, False)

        self.marco = ttk.Frame(self.ventana, padding=20)
        self.marco.pack(fill="both", expand=True)

        self.titulo = ttk.Label(self.marco, text="Pirámide", font=("Arial", 16, "bold"))
        self.titulo.pack(pady=5)

        self.imagen = tk.PhotoImage(file=os.path.join(RUTA, "piramide.png"))
        self.imagen = self.imagen.subsample(max(1, (self.imagen.width()+179)//180), max(1, (self.imagen.height()+139)//140))
        self.etiqueta_imagen = ttk.Label(self.marco, image=self.imagen)
        self.etiqueta_imagen.pack(pady=10)

        self.base = ttk.Label(self.marco, text="Base (cm):")
        self.base.pack(anchor="w")
        self.campo_base = ttk.Entry(self.marco)
        self.campo_base.pack(fill="x", pady=4)

        self.altura = ttk.Label(self.marco, text="Altura (cm):")
        self.altura.pack(anchor="w")
        self.campo_altura = ttk.Entry(self.marco)
        self.campo_altura.pack(fill="x", pady=4)

        self.apotema = ttk.Label(self.marco, text="Apotema (cm):")
        self.apotema.pack(anchor="w")
        self.campo_apotema = ttk.Entry(self.marco)
        self.campo_apotema.pack(fill="x", pady=4)

        self.boton_calcular = ttk.Button(self.marco, text="Calcular", command=self.calcular)
        self.boton_calcular.pack(pady=12)

        self.resultado_volumen = ttk.Label(self.marco, text="Volumen: ")
        self.resultado_volumen.pack(anchor="w", pady=5)

        self.resultado_superficie = ttk.Label(self.marco, text="Superficie: ")
        self.resultado_superficie.pack(anchor="w", pady=5)

    def calcular(self):
        try:
            base = float(self.campo_base.get())
            altura = float(self.campo_altura.get())
            apotema = float(self.campo_apotema.get())

            if not (0 < base < float("inf") and 0 < altura < float("inf") and 0 < apotema < float("inf")):
                raise ValueError

            piramide = Piramide(base, altura, apotema)

            self.resultado_volumen.config(text=f"Volumen: {piramide.calcular_volumen():.2f} cm³")
            self.resultado_superficie.config(text=f"Superficie: {piramide.calcular_superficie():.2f} cm²")

        except ValueError:
            messagebox.showerror("Error", "Ingrese valores numéricos positivos en todos los campos.")


class VentanaCubo():
    def __init__(self, ventana_padre):

        self.ventana = tk.Toplevel(ventana_padre)
        self.ventana.title("Cubo")
        self.ventana.geometry("350x390")
        self.ventana.resizable(False, False)

        self.marco = ttk.Frame(self.ventana, padding=20)
        self.marco.pack(fill="both", expand=True)

        self.titulo = ttk.Label(self.marco, text="Cubo", font=("Arial", 16, "bold"))
        self.titulo.pack(pady=5)

        self.imagen = tk.PhotoImage(file=os.path.join(RUTA, "cubo.png"))
        self.imagen = self.imagen.subsample(max(1, (self.imagen.width()+179)//180), max(1, (self.imagen.height()+139)//140))
        self.etiqueta_imagen = ttk.Label(self.marco, image=self.imagen)
        self.etiqueta_imagen.pack(pady=10)

        self.lado = ttk.Label(self.marco, text="Lado (cm):")
        self.lado.pack(anchor="w")
        self.campo_lado = ttk.Entry(self.marco)
        self.campo_lado.pack(fill="x", pady=4)

        self.boton_calcular = ttk.Button(self.marco, text="Calcular", command=self.calcular)
        self.boton_calcular.pack(pady=12)

        self.resultado_volumen = ttk.Label(self.marco, text="Volumen: ")
        self.resultado_volumen.pack(anchor="w", pady=5)

        self.resultado_superficie = ttk.Label(self.marco, text="Superficie: ")
        self.resultado_superficie.pack(anchor="w", pady=5)

    def calcular(self):
        try:
            lado = float(self.campo_lado.get())

            if not (0 < lado < float("inf")):
                raise ValueError

            cubo = Cubo(lado)

            self.resultado_volumen.config(text=f"Volumen: {cubo.calcular_volumen():.2f} cm³")
            self.resultado_superficie.config(text=f"Superficie: {cubo.calcular_superficie():.2f} cm²")

        except ValueError:
            messagebox.showerror("Error", "Ingrese un lado numérico positivo.")


class VentanaPrisma():
    def __init__(self, ventana_padre):

        self.ventana = tk.Toplevel(ventana_padre)
        self.ventana.title("Prisma rectangular")
        self.ventana.geometry("350x500")
        self.ventana.resizable(False, False)

        self.marco = ttk.Frame(self.ventana, padding=20)
        self.marco.pack(fill="both", expand=True)

        self.titulo = ttk.Label(self.marco, text="Prisma rectangular", font=("Arial", 16, "bold"))
        self.titulo.pack(pady=5)

        self.imagen = tk.PhotoImage(file=os.path.join(RUTA, "prisma.png"))
        self.imagen = self.imagen.subsample(max(1, (self.imagen.width()+179)//180), max(1, (self.imagen.height()+139)//140))
        self.etiqueta_imagen = ttk.Label(self.marco, image=self.imagen)
        self.etiqueta_imagen.pack(pady=10)

        self.largo = ttk.Label(self.marco, text="Largo (cm):")
        self.largo.pack(anchor="w")
        self.campo_largo = ttk.Entry(self.marco)
        self.campo_largo.pack(fill="x", pady=4)

        self.ancho = ttk.Label(self.marco, text="Ancho (cm):")
        self.ancho.pack(anchor="w")
        self.campo_ancho = ttk.Entry(self.marco)
        self.campo_ancho.pack(fill="x", pady=4)

        self.altura = ttk.Label(self.marco, text="Altura (cm):")
        self.altura.pack(anchor="w")
        self.campo_altura = ttk.Entry(self.marco)
        self.campo_altura.pack(fill="x", pady=4)

        self.boton_calcular = ttk.Button(self.marco, text="Calcular", command=self.calcular)
        self.boton_calcular.pack(pady=12)

        self.resultado_volumen = ttk.Label(self.marco, text="Volumen: ")
        self.resultado_volumen.pack(anchor="w", pady=5)

        self.resultado_superficie = ttk.Label(self.marco, text="Superficie: ")
        self.resultado_superficie.pack(anchor="w", pady=5)

    def calcular(self):
        try:
            largo = float(self.campo_largo.get())
            ancho = float(self.campo_ancho.get())
            altura = float(self.campo_altura.get())

            if not (0 < largo < float("inf") and 0 < ancho < float("inf") and 0 < altura < float("inf")):
                raise ValueError

            prisma = Prisma(largo, ancho, altura)

            self.resultado_volumen.config(text=f"Volumen: {prisma.calcular_volumen():.2f} cm³")
            self.resultado_superficie.config(text=f"Superficie: {prisma.calcular_superficie():.2f} cm²")

        except ValueError:
            messagebox.showerror("Error", "Ingrese valores numéricos positivos en todos los campos.")


class VentanaPrincipal():
    def __init__(self):

        self.ventana = tk.Tk()
        self.ventana.title("Figuras geométricas")
        self.ventana.geometry("350x340")
        self.ventana.resizable(False, False)

        self.marco = ttk.Frame(self.ventana, padding=20)
        self.marco.pack(fill="both", expand=True)

        self.titulo = ttk.Label(self.marco, text="Figuras geométricas", font=("Arial", 16, "bold"))
        self.titulo.pack(pady=(0, 15))

        self.boton_cilindro = ttk.Button(self.marco, text="Cilindro", command=self.abrir_cilindro)
        self.boton_cilindro.pack(fill="x", pady=6)

        self.boton_esfera = ttk.Button(self.marco, text="Esfera", command=self.abrir_esfera)
        self.boton_esfera.pack(fill="x", pady=6)

        self.boton_piramide = ttk.Button(self.marco, text="Pirámide", command=self.abrir_piramide)
        self.boton_piramide.pack(fill="x", pady=6)

        self.boton_cubo = ttk.Button(self.marco, text="Cubo", command=self.abrir_cubo)
        self.boton_cubo.pack(fill="x", pady=6)

        self.boton_prisma = ttk.Button(self.marco, text="Prisma", command=self.abrir_prisma)
        self.boton_prisma.pack(fill="x", pady=6)

    def abrir_cilindro(self):
        VentanaCilindro(self.ventana)

    def abrir_esfera(self):
        VentanaEsfera(self.ventana)

    def abrir_piramide(self):
        VentanaPiramide(self.ventana)

    def abrir_cubo(self):
        VentanaCubo(self.ventana)

    def abrir_prisma(self):
        VentanaPrisma(self.ventana)

    def ejecutar(self):
        self.ventana.mainloop()


def Main():
    ventana = VentanaPrincipal()
    ventana.ejecutar()


if __name__ == "__main__":
    Main()

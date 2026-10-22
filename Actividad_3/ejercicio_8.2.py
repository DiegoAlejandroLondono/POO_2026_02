
import tkinter as tk
from tkinter import ttk, messagebox


class Notas():
    def __init__(self):

        #Se inicializa una lista de 5 posiciones con valor 0.
        self.lista_notas = [0.0]*5

    def calcular_promedio(self) -> float:
        suma = 0

        for nota in self.lista_notas:
            suma += nota

        return suma/len(self.lista_notas)

    def calcular_desviacion(self) -> float:
        prom = self.calcular_promedio()
        suma = 0

        for nota in self.lista_notas:
            suma += (nota-prom)**2

        return (suma/len(self.lista_notas))**0.5

    def calcular_mayor(self) -> float:
        return max(self.lista_notas)

    def calcular_menor(self) -> float:
        return min(self.lista_notas)


class VentanaPrincipal():
    def __init__(self):

        #Tk crea la ventana de la interfaz
        self.ventana = tk.Tk()
        self.ventana.title("Calculadora de notas")

        #geometry define el tamaño inicial de la ventana en pixeles (ancho x alto)
        self.ventana.geometry("380x440")

        #resizable permite definir si el usuario puede cambiar el ancho y alto de la ventana
        self.ventana.resizable(False, False)

        #Con ttk se pueden utilizar mejores estilo. Frame crea un contenedor en el que se pueden organizar elementos. padding define el espacio de los bordes del contenedor
        self.marco = ttk.Frame(self.ventana, padding=20)

        #pack posiciona un componente dentro de su contenedor. fill="both" permite ocupar el espacio completo en horizontal y vertical. expand=True permite que reciba espacio adicional del contenedor
        self.marco.pack(fill="both", expand=True)

        #Label permite mostrar texto. El primer argumento indica el contenedor padre. font recibe el tipo de letra, tamaño y estilo
        self.titulo = ttk.Label(
            self.marco,
            text="Calculadora de notas",
            font=("Arial", 16, "bold")
        )

        #pady agrega espacio vertical. El primer argumento es espacio arriba, el segundo espacio abajo
        self.titulo.pack(pady=(0, 15))

        #Se utiliza una lista para almacenar los campos de entrada
        self.campos = []

        for i in range(5):

            #Se crea un Frame para agrupar la etiqueta y el campo de cada nota
            fila = ttk.Frame(self.marco)

            #fill="x" hace que el contenedor ocupe el ancho completo del contenedor
            fila.pack(fill="x", pady=4)

            #width define el ancho  de la etiqueta en unidades de caracteres
            etiqueta = ttk.Label(
                fila,
                text=f"Nota {i+1}:",
                width=12
            )

            #side="left" posiciona los elementos de izquierda a derecha dentro del Frame
            etiqueta.pack(side="left")

            #Entry permite ingresar texto. Y su contenido se puede leer con el método get()
            campo = ttk.Entry(fila)

            #El campo se ubica a la derecha y se expande para ocupar el ancho restante
            campo.pack(side="right", fill="x", expand=True)

            self.campos.append(campo)

        #Se crea otro contenedor para mantener los dos botones en una fila
        self.marco_botones = ttk.Frame(self.marco)
        self.marco_botones.pack(pady=18)

        #command recibe la referencia al método que se ejecuta cuando se presiona el botón (El metodo se pone sin parentesis)
        self.boton_calcular = ttk.Button(
            self.marco_botones,
            text="Calcular",
            command=self.calcular
        )

        #padx agrega espacio horizontal a los lados del botón
        self.boton_calcular.pack(side="left", padx=8)

        self.boton_limpiar = ttk.Button(
            self.marco_botones,
            text="Limpiar",
            command=self.limpiar
        )
        self.boton_limpiar.pack(side="left", padx=8)

        #Separator crea una línea divisoria. orient="horizontal" indica su orientación
        #Se utiliza directamente sin almacenarlo porque no necesitamos modificarlo después
        ttk.Separator(
            self.marco,
            orient="horizontal"
        ).pack(fill="x", pady=8)

        self.resultado_promedio = ttk.Label(
            self.marco,
            text="Promedio: "
        )

        #anchor="w" alinea el elemento hacia west
        #pady=5 agrega cinco pixeles de espacio arriba y abajo
        self.resultado_promedio.pack(anchor="w", pady=5)

        self.resultado_desviacion = ttk.Label(
            self.marco,
            text="Desviación estándar: "
        )
        self.resultado_desviacion.pack(anchor="w", pady=5)

        self.resultado_mayor = ttk.Label(
            self.marco,
            text="Nota mayor: "
        )
        self.resultado_mayor.pack(anchor="w", pady=5)

        self.resultado_menor = ttk.Label(
            self.marco,
            text="Nota menor: "
        )
        self.resultado_menor.pack(anchor="w", pady=5)

    def calcular(self):

        notas = Notas()

        for i, campo in enumerate(self.campos):

            #enumerate permite recorrer los elementos de una lista obteniendo su índice y su valor
            #strip elimina los espacios al inicio y final del texto
            texto = campo.get().strip()

            #Se verifica que todas las notas estén ingresadas.
            if texto == "":
                messagebox.showerror(
                    "Error",
                    f"Debe ingresar la nota {i+1}."
                )
                return

            #try permite manejar errores sin bloquear la ejecucion
            try:
                nota = float(texto)

            except ValueError:
                #showerror muestra una ventana emergente con un mensaje de error
                messagebox.showerror(
                    "Error",
                    f"La nota {i+1} debe ser un valor numérico."
                )
                return

            #Se verifica que la nota sea un número finito.
            if not (-float("inf") < nota < float("inf")):
                messagebox.showerror(
                    "Error",
                    f"La nota {i+1} debe ser un número finito."
                )
                return

            notas.lista_notas[i] = nota

        #config permite modificar las propiedades de los componentes graficos
        self.resultado_promedio.config(
            #:.2f muestra los resultados con dos decimales.
            text=f"Promedio: {notas.calcular_promedio():.2f}"
        )

        self.resultado_desviacion.config(
            text=f"Desviación estándar: {notas.calcular_desviacion():.2f}"
        )

        self.resultado_mayor.config(
            text=f"Nota mayor: {notas.calcular_mayor():.2f}"
        )

        self.resultado_menor.config(
            text=f"Nota menor: {notas.calcular_menor():.2f}"
        )

    def limpiar(self):

        #delete(0, tk.END) elimina todo el contenido de los campos de entrada.
        #El indice 0 indica el inicio y tk.END representa el final del texto
        for campo in self.campos:
            campo.delete(0, tk.END)

        self.resultado_promedio.config(text="Promedio: ")
        self.resultado_desviacion.config(text="Desviación estándar: ")
        self.resultado_mayor.config(text="Nota mayor: ")
        self.resultado_menor.config(text="Nota menor: ")

    def ejecutar(self):
        self.ventana.mainloop()


def Main():
    ventana = VentanaPrincipal()
    ventana.ejecutar()


if __name__ == "__main__":
    Main()

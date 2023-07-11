#Importamos las librerias de entorno grafico y funciones de hora

from tkinter import *
from time import strftime

#Declaramos e inicializamos la variables del entorno grafico
ventana = Tk()
#Agregamos un titulo a nuestra ventana
ventana.title("Reloj GPS")
#Personalizamos el logotigo
ventana.iconbitmap("ICO\LogoPena.ico")

#Crearmos una funcion para mostrar la hora
def hora():
#Creamos una variable para almacenar el format de salida de la hora
    hora_actual = strftime("%H:%M:%S %p")
#Configuramos el parametro Clock para que se muestre en nuestra variable
    clock.config(text = hora_actual)
#Le decimos a nuestro parametro Clock a cada cuento se va actualizar nuestra hora
    clock.after(1000, hora)

#Creamos una etiqueta donde se mostrara la hora y le damos formato
clock = Label(ventana, font = ("arial", 40, "bold"), background = "Blue", foreground = "White")
#Anclamos la etiqueta dentro de nuestra ventaba principal
clock.pack(anchor = "center")

#Llamamos a nuestra funcion
hora()

#Creamos un Loop para que nuestra ventana no se cierre
mainloop()
    

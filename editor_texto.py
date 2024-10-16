import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import filedialog as FileDialog

global ruta # Esta variable nos permitirá almacenar en ella la ruta del fichero

def nuevo() -> None:
    'Esta función permite abrir un nuevo fichero'

    global ruta
    mensaje.set("Nuevo fichero")
    ruta = ""
    texto.delete(1.0, "end")
    root.title("Notepad")

def abrir() -> None:
    'Esta función permite abrir un fichero'

    global ruta
    mensaje.set("Abrir fichero")
    ruta = FileDialog.askopenfilename(initialdir='.', 
        filetypes=(("Ficheros de texto", "*.txt"),),
        title="Abrir un fichero de texto"
    )
    mensaje.set('Editor de Texto en python')

    # Verifica si la ruta no está vacía para indicar que la ruta de archivo seleccionada es válida
    if ruta != "":
        fichero = open(ruta, 'r')
        contenido = fichero.read()
        texto.delete('1.0', END)
        texto.insert('insert', contenido)
        fichero.close()
        root.title(ruta + 'Notepad')

# Ventana principal
root = Tk()
root.title("Notepad")
root.geometry("800x500")

# Barra de menú
menubar = Menu(root) # Se instancia la barra menú
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Nuevo", command=nuevo)
filemenu.add_command(label="Abrir", command=abrir)
filemenu.add_command(label="Salir", command=root.quit)
menubar.add_cascade(menu=filemenu, label="Archivo") 

# Caja de texto central
texto = Text(root)
texto.pack(fill="both", expand=1)


# Monitor inferior
mensaje = StringVar()
mensaje.set("Bienvenido a tu Editor")
monitor = Label(root, textvar=mensaje, justify='left')
monitor.pack(side="left")

root.config(menu=menubar)

# Bucle de la aplicacion
root.mainloop()
